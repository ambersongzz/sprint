import os
import sys
import json

from flask import request
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger(directory, prefix, name, log_file, level=logging.INFO):
    """setup multiple loggers as we want"""

    handler = TimedRotatingFileHandler(directory + prefix + log_file, when = "m", interval = 2, backupCount = 10000)
    handler.setLevel(logging.INFO)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def logger_info(raw_logger, proc_logger):
    """
    save logger info into raw_logger
    check the validity of JSON data, and save valid JSON data into proc_logger
    """
    raw_logger.info(request.get_data())
    extract_name_age(request.get_data(), proc_logger) # extract valid, and save into proc.txt

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError()
        elif v is not None:
           d[k] = v
    return d    

def extract_name_age(line, logger):
    """
    extract the name and age from one json line if it is valid
    """
    # if not os.path.exists(directory + prefix):
    #     os.makedirs(directory + prefix)
    # w = open(directory + prefix + file, 'w')
    try:
        j_content = json.loads(line, object_pairs_hook=dict_raise_on_duplicates)
        name = j_content['name']
        age = j_content['prop']['age']
        if type(age) is int and age >= 0:
            result = name + '\t' + str(age)
            logger.info(result)
    except:
        pass

# extract_name_age(directory = '/srv/runme/', prefix = sys.argv[1])
