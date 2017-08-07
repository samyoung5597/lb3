import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting
from core import shopping
from core import auth
from core import log
from core import card


def purchase_records(*args,**kwargs):
    '待付款'
    try:
        user_name = args[0][0]
        total_money = args[0][1]
        shopping_list = args[0][2]
    except IndexError:
        print("无订单需支付")
        return
    print("待付款订单为：")
    for l in shopping_list:
        print(l)
    print("待付款金额为：",total_money)
    pay_for = str(input("是否付款？Y/N").strip())
    if pay_for == 'y' or pay_for == 'Y':
        user_list = []
        with open('%s\\db\\user' % BASE_DIR, 'r+') as f1:
            for line in f1:
                try:
                    if user_name == json.loads(line)['name']:
                        user_dic = json.loads(line)
                        user_dic['limit'] -= total_money
                        user_list.append(user_dic)
                    else:
                        user_list.append(json.loads(line))
                except Exception:
                    pass
            f1.seek(0)
            for l in user_list:
                f1.write(json.dumps(l)+'\n')
            print("付款成功！用户余额为：%s"%user_dic['limit'])
        log.log('%s\\log\\shopping_log'%BASE_DIR,'%s pay for %s'%(user_name,total_money))
    elif pay_for == 'n' or pay_for == 'N':
        return

def change_pw(*args):
    user_name = args[0][0]
    old_pw = input("原密码：").strip()
    while True:
        new_pw = input("新密码：").strip()
        new_pw_age = input("请再次输入新密码：").strip()
        if new_pw == new_pw_age:
            break
        else:
            print("两次密码不一致！请重新输入")
            continue
    user_list = []
    with open('%s\\user' % setting.DATABASE_PATH, 'r+') as f:
        for line in f:
            try:
                if user_name == json.loads(line)['name']:
                    if old_pw == json.loads(line)['password']:
                        user_dic = json.loads(line)
                        user_dic['password'] = new_pw
                        user_list.append(user_dic)
                    else:
                        print("原密码输入有误！")
                        return
                else:
                    user_list.append(json.loads(line))
            except Exception:
                pass
        f.seek(0)
        for l in user_list:
            f.write(json.dumps(l)+'\n')
        print("密码修改成功！")
        log.log('%s\\log\\user_log' % BASE_DIR, '%s change password successful! ' % user_name)


@auth.auth(user_type='user')
def login(*args,**kwargs):
    while True:
        print('东升购物系统'.center(100,'*'))
        print("1.待付款订单\t\t\t2.修改密码\t\t\t3.我的信用卡\t\t\t4.退出".center(70))
        choice = int(input('>:').strip())
        if not choice:continue
        if choice == 1:
            purchase_records(args)
        elif choice == 2:
            change_pw(args)
        elif choice == 3:
            card.card(*args)
        elif choice == 4:
            break




