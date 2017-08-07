import os
import json
import logging
import time
from core import auth
from conf import settings
from core import logger
from core import db_handler
from core.auth import login_required
from core import accounts


user_logger = logger.logger('login_in')

None_user_data = {
        'user_id': None,
        'user_data': None,
        'is_auth': False
}

def show_user(user_data):
    print(user_data)
@login_required
def drow_money(user_data):
    auth.withdraw(user_data)
def repay_money(user_data):
    auth.repay(user_data)
def tran_money(user_data):
    auth.transfer(user_data)
def spend_bill(user_data):
    auth.spend()
def logout(user_data):
    print("欢迎下次光临")
    exit()

def user_menu(user_data):
    print("欢迎来到信用卡操作系统".center(50, "-"))
    menu = '''
        1：显示用户信息
        2：取款
        3：存款
        4：转账
        5：打印账单
        6：退出

    '''
    menu_dic = {
        "1": show_user,
        "2": drow_money,
        "3": repay_money,
        "4": tran_money,
        "5": spend_bill,
        "6": logout
    }
    print(menu)
    flag = False
    while not flag:
        choice = input("请输入要操作的项>>>").strip()
        if choice in menu:
            menu_dic[choice](user_data)
        else:
            print("no exit")


def login_auth(accounts, password):
    db_path = db_handler.db_handler(settings.DATABASE)
    user_file = "%s\%s.json" % (db_path, accounts)

    if os.path.isfile(user_file):
        # print("---------------------")
        with open(user_file, "r") as f:
            accounts_data = json.load(f)  # 打开db里的用户信息
            if accounts_data['password'] == password:

                exp_time_stamp = time.mktime(time.strptime(accounts_data['expire_date'], "%Y-%m-%d"))
                if time.time() > exp_time_stamp:
                    print(
                        "\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % accounts)
                else:
                    return accounts_data
            else:
                print("error")
    else:
        print("no exit!!!")
def login(None_user_data,log_obj):
    count = 0

    while None_user_data['is_auth'] is not True and count < 3:
        accounts = input("输入用户名>>>").strip()
        password = input("输入密码>>>").strip()
        new_user = login_auth(accounts, password)
        if new_user:
            None_user_data['is_auth'] = True
            None_user_data['user_id'] = accounts
            return new_user
        count += 1
    else:
        log_obj.debug("Please check the account number or password")
        exit()


def run():
    # 验证用户名id和密码
    user_data = login(None_user_data, user_logger)
    print(user_data)
    if None_user_data['is_auth']:
        None_user_data['user_data'] = user_data
        user_menu(user_data)


