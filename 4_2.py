#! /usr/bin/python

__author__="Jiada Chen <jc4730@columbia.edu>"

from get_param_e import get_param_e

if __name__ == "__main__":
    count_file = 'ner_rare.counts'
    dev_file = 'ner_dev.dat'
    write_file = '4_2.txt'
    
    data = get_param_e(count_file)
    lines = [line.strip('\n') for line in open(dev_file)]
    rare_word = data[data.Word == '_RARE_'].sort_values(by='log_E',ascending=False).iloc[0]
    rare_tag = rare_word['Tag']
    rare_log_e = str(rare_word['log_E'])

    with open(write_file,'w') as f:
        for line in lines:
            if line == '':
                pass
            else:
                try:
                    r = data[data.Word == line].sort_values(by='log_E',ascending=False).iloc[0]
                    tag   = r['Tag']
                    log_e = r['log_E']
                    line = line + ' ' + tag + ' ' + str(log_e)
                except:
                    line = line + ' ' + rare_tag + ' ' + rare_log_e
            f.write(line + '\n')
