#! /usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

def get_rare_set(threshold,read_file):
    import pandas as pd
    data = pd.read_csv(read_file,sep =' ',header=None,names=['word','tag'],dtype={'word':'str','tag':'str'},\
                       quoting=3)
    word_count = data.groupby(['word'], as_index=False).count()
    rare_set = set(word_count[word_count['tag'] < threshold]['word'].tolist())

    return rare_set
