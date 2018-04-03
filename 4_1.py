#! /usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

from get_rare_set import get_rare_set

if __name__ == "__main__":
    threshold  = 5
    read_file = 'ner_train.dat'
    write_file = 'ner_train_rare.dat'
    
    rare_set = get_rare_set(threshold,read_file)
    
    lines = [line.rstrip('\n') for line in open(read_file)]

    with open(write_file,'w') as f:
        for line in lines:
            try:
                word, tag = line.split(' ')
                if word in rare_set:
                    word = '_RARE_'
                    line = word + ' ' + tag
            except:
                pass
            f.write(line + '\n')
