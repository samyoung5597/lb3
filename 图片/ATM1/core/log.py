#coding:utf-8
import logging

def log(file_path,info):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(file_path)
    fm = logging.Formatter('%(asctime)s-%(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(fm)
    logger.addHandler(fh)
    logger.info(info)
    logger.removeHandler(fh)

