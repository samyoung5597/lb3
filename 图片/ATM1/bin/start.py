#_*_ coding:utf-8 _*_
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import manage
from core import shopping
from core import login
from core import card

if __name__ == '__main__':
    while True:
        print("欢迎光临！<东升商城>".center(100, '*'))
        print("1.进入商城\t\t\t2.登录系统\t\t\t3.我的信用卡\t\t\t4.后台管理".center(80, ))
        choice = input(">:").strip()
        if not choice: continue
        if choice == '1':
            shopping.shopping()
        elif choice == '2':
            login.login()
        elif choice == '3':
            card.card()
        elif choice == '4':
            manage.manage()
