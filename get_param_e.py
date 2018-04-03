#! /usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

def get_param_e(count_file):
    import pandas as pd
    import numpy as np
    
    data = pd.read_csv(count_file,sep =' ',names=['a','b','c','d','e'],quoting=3)

    tag_count = data[data.b == '1-GRAM'][['a','c']].rename(columns={'a':'Tag_Count','c':'Tag'})
    data = data[data.b == 'WORDTAG'][['a','c','d']].rename(columns={'a':'Count','c':'Tag','d':'Word'})

    data = data.merge(tag_count,how='left')

    data['Emission'] = data['Count']/data['Tag_Count']
    data['log_E'] = np.log(data['Emission'])/np.log(2)

    return data
