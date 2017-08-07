import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #主目录
sys.path.append(BASE_DIR)



USER_LIMIT = 15000   #用户信用卡限额

POUNDAGE= 0.05       #体现手续费

DATABASE_PATH = '%s\\db'%BASE_DIR  #数据库目录

