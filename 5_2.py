#!/usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

import numpy as np
from get_param_e import get_param_e
from get_param_q import get_param_q
from count_freqs import simple_conll_corpus_iterator,sentence_iterator

if __name__ == "__main__":
    count_file = 'ner_rare.counts'
    dev_file = 'ner_dev.dat'
    out_file = '5_2.txt'

    q_tbl = get_param_q(count_file)
    q_dic = {}
    for index, row in q_tbl.iterrows():
        q_dic[(row['y_i'],row['y_i1'],row['y_i2'])] = row['log_q']

    e_tbl = get_param_e(count_file)
    e_dic = {}
    for index, row in e_tbl.iterrows():
        e_dic[(row['Word'],row['Tag'])] = row['log_E']

    tag_list = list(set(e_tbl['Tag'].tolist()))
    vocab = set(e_tbl['Word'].tolist())

    with open(out_file,'w') as f:
        sentences =[sentence for sentence in sentence_iterator(simple_conll_corpus_iterator(file(dev_file,"r")))]
        
        for sentence in sentences:
            n = len(sentence)
            
            tag_dic ={}
            tag_dic[-1] = ['*']
            tag_dic[0] = ['*']
            for k in range(1,n+1):
                tag_dic[k] = list(tag_list)
            
            pi = {}
            bp = {}
            pi[(0,'*','*')]=np.log(1.)/np.log(2)
            
            for k in range(1,n+1):
                for u in tag_dic[k-1]:
                    for v in tag_dic[k]:
                        tmp_max = float("-Inf")
                        tmp_bp = None
                        for w in tag_dic[k-2]:
                            if sentence[k-1][1] in vocab:
                                try:
                                    e = e_dic[(sentence[k-1][1],v)]
                                except KeyError:
                                    continue
                            else:
                                try:
                                    e = e_dic[('_RARE_',v)]
                                except KeyError:
                                    continue
                            try:
                                tmp_pi = pi[(k-1,w,u)]+q_dic[(v,u,w)]+e
                                if tmp_pi > tmp_max:
                                    tmp_max = tmp_pi
                                    tmp_bp = w
                            except KeyError:
                                continue
                        if tmp_bp is not None:
                            pi[(k,u,v)] = tmp_max
                            bp[(k,u,v)] = tmp_bp
        
            y = {}
            p = {}
            tmp_max = float("-Inf")
            if n == 1:
                for v in tag_list:
                    try:
                        tmp = pi[(n,'*',v)]+q_dic[('STOP',v,'*')]
                        if tmp > tmp_max:
                            tmp_max = tmp
                            y=v
                    except KeyError:
                        continue
                f.write(sentence[0][1] + ' ' + y + ' ' + str(tmp_max) + '\n')
                f.write('\n')
            else:
                for u in tag_list:
                    for v in tag_list:
                        try:
                            tmp = pi[(n,u,v)]+q_dic[('STOP',v,u)]
                            if tmp > tmp_max:
                                tmp_max = tmp
                                y[n] = v
                                y[n-1] = u
                        except KeyError:
                            continue
                for k in range(n-2,-2,-1):
                    y[k] = bp[(k+2,y[k+1],y[k+2])]
                for k in range(n,0,-1):
                    p[k] = pi[k,y[k-1],y[k]]
                
                for k in range(1,n+1):
                    f.write(sentence[k-1][1] + ' ' + y[k] + ' ' + str(p[k]) + '\n')
                f.write('\n')
