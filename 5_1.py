#! /usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

from get_param_q import get_param_q

if __name__ == "__main__":
    count_file = 'ner_rare.counts'
    in_file = 'trigrams.txt'
    out_file = '5_1.txt'

    data = get_param_q(count_file)
    q_dic = {}
    for index, row in data.iterrows():
        q_dic[(row['y_i'],row['y_i1'],row['y_i2'])] = row['log_q']

    lines = [line.strip('\n') for line in open(in_file)]
    with open(out_file,'w') as f:
        for line in lines:
            y_i2, y_i1, y_i = line.split(' ')
            try:
                log_q = str(q_dic[(y_i,y_i1,y_i2)])
                line = line + ' ' + log_q
            except KeyError:
                pass
            f.write(line + '\n')
