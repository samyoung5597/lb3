import json
import re
from core import db_handler
from conf import settings
from core import accounts
from core import logger
import logging
import time

def login_required(func):
    "验证用户是否登录"

    def wrapper(*args,**kwargs):
        if args[0].get('is_auth'):
            return func(*args,**kwargs)
        else:
            exit("User is not auth.")
    return wrapper


tran_logger = logger.logger('access')

def make_transaction(tran_logger,user_data,tran_type,amount_money):
    amount_money = float(amount_money)
    if tran_type in settings.TRANSACTION_TYPE:
        intertest = amount_money * settings.TRANSACTION_TYPE[tran_type]['interest'] # 算的利息
        old_money = user_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == "plus":
            new_balance = old_money + amount_money + intertest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == "minus":
            new_balance = old_money - amount_money - intertest
            if new_balance < 0:
                print("余额不足")
                return
        user_data['balance'] = new_balance
        new_balance = user_data
        accounts.account_dump(new_balance)
        tran_logger.debug("this trans is success and you remain %s money" % (new_balance['balance']))

        return new_balance
    else:
        print("输入有误")

def withdraw(user_data):
    user_data = accounts.account_load(user_data['id'])
    print("信用卡现有金额 %s" % (user_data['balance']))

    flag = False
    while not flag:
        withdraw_money = input("输入你想要取的金额>>>>").strip()
        if len(withdraw_money) > 0 and withdraw_money.isdigit():
            new_user_data = make_transaction(tran_logger, user_data, 'withdraw', withdraw_money)
            if new_user_data:
                print("还剩余额%s" % (new_user_data['balance']))
                # tran_logger.debug("this trans is success and you tack %s money" %(withdraw_money) )
            flag = True

def repay(user_data):
    user_data = accounts.account_load(user_data['id'])
    print("信用卡现有金额 %s" % (user_data['balance']))
    flag = False
    while not flag:
        repay_money = input("输入你要存取的金额>>>>").strip()
        if len(repay_money) > 0 and repay_money.isdigit():
            new_user_data = make_transaction(tran_logger, user_data, 'repay', repay_money)
            if new_user_data:
                print("信用卡金额%s" % (new_user_data['balance']))
                # tran_logger.debug("this trans is success and you save %s money" % (repay_money))
            flag = True
def transfer(user_data):
    user_data = accounts.account_load(user_data['id'])
    print("信用卡金额%s" % (user_data['balance']))
    flag = False
    while not flag:
        tran_id = input("请输入对方信用卡ID>>>>>").strip()
        tran_money = input("请输入要转的金额>>>>").strip()
        if tran_id.isdigit():
            if len(tran_money) > 0 and tran_money.isdigit():
                new_user_data = make_transaction(tran_logger,user_data, 'transfer', tran_money)
                if new_user_data:
                    print("信用卡剩余金额%s" % (new_user_data['balance']))
                    # tran_logger.debug("this trans is success and you transfer %s money to %s" % (tran_money,tran_id))
                flag = True

def spend():
    db_path = settings.BASE_DIR
    new_user_file = "%s\log\\access.log" % (db_path)
    f = open(new_user_file,'r')
    a = f.read()
    print(a)
    f.close()
def xiaofei(shop_price,counts):
    flag = False
    while not flag:
        xiaofei_money = shop_price
        db_path = db_handler.db_handler(settings.DATABASE)
        new_user_file = "%s/%s.json" % (db_path,counts)
        with open(new_user_file,"r") as f:
            user_data = json.load(f)
            if user_data['balance'] < shop_price:
                print("余额不足")
            else:
                new_balance = float(user_data['balance']) - float(xiaofei_money)
                user_data['balance'] = new_balance
                new_user_data = user_data

                with open(new_user_file, "w") as f:
                    json.dump(new_user_data, f)
                    print("信用卡中剩余金额", new_user_data['balance'])
                    tran_logger.debug("this trans is success and you spend %s money" % (xiaofei_money))
        flag = True





