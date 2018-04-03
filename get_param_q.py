#!/usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

def get_param_q(count_file):
    import pandas as pd
    data = pd.read_csv(count_file,sep =' ',names=['a','b','c','d','e'],quoting=3)
    trigram = data[data.b == '3-GRAM'][['a','c','d','e']].rename(columns={'a':'Count','c':'y_i2','d':'y_i1','e':'y_i'})
    bigram = data[(data.b == '2-GRAM')&(data.d!='STOP')][['a','c','d']].rename(columns={'a':'Count','c':'y_i2','d':'y_i1'})
    
    import numpy as np
    data = trigram.merge(bigram,how='left',left_on=['y_i2','y_i1'],right_on=['y_i2','y_i1'],suffixes=('_trigram', '_bigram'))
    data['log_q'] = np.log(data['Count_trigram']/data['Count_bigram'])/np.log(2)
    
    return data
