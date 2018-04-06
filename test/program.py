import os
import sys
import json

# def integrity_checker(s):

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError()
        elif v is not None:
           d[k] = v
    return d    

def extract_name_age(directory, prefix):
    try:
        w = open(directory + prefix +'.txt', 'w')
    except:
        return
    for fname in os.listdir(directory):
        if fname.startswith(prefix):
            f = open(directory + fname, 'r')
            for line in f:
                try:
                    j_content = json.loads(line, object_pairs_hook=dict_raise_on_duplicates)
                    name = j_content['name']
                    age = j_content['prop']['age']
                    if type(age) is int and age >= 0:
                        w.write(name + '\t' + str(age) + '\n')
                except:
                    continue
            f.close()  
    w.close()

extract_name_age(directory = '/home/ec2-user/whatever/data/', prefix = sys.argv[1])


    