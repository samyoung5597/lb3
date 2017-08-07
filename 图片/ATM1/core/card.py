from core import log
from conf import setting
from core import auth
import json

def transfer(user_name): #转账
    name = input("转账给：").strip()
    with open('%s\\user'%setting.DATABASE_PATH,'r+') as f1:
        for line in f1 :
            if name == json.loads(line)['name']:
                break
        else:
            print("无此账户！")
            return
    money = int(input("转账金额：").strip())
    # pay_passwd = input("请输入支付密码：").strip()
    money_list = []
    with open('%s\\user'%setting.DATABASE_PATH,'r+') as f:
        for line in f :
            if user_name == json.loads(line)['name']:
                user_dic = json.loads(line)
                user_dic['limit'] -= money
                money_list.append(user_dic)
            elif name == json.loads(line)['name']:
                user1_dic = json.loads(line)
                user1_dic['limit'] += money
                money_list.append(user1_dic)
            else:
                money_list.append(json.loads(line))
        f.seek(0)
        for l in money_list:
            f.write(json.dumps(l) + '\n')
        print("转账成功！")
        log.log('%s\\log\\card_log' % setting.BASE_DIR, '%s transfer to %s :$%s successsful!' % (user_name,name,money))
        return
def withdraw(user_name): #提现
    try:
        money = int(input("请输入提现金额：").strip())
    except TypeError as e:
        print("type must be int!")
    pay_passwd = input("请输入支付密码：").strip()
    money_list = []
    with open('%s\\user' % setting.DATABASE_PATH, 'r+') as f:
        for line in f:
            if user_name == json.loads(line)['name']:
                if pay_passwd == json.loads(line)['pay_mm']:
                    user_dic = json.loads(line)
                    if user_dic['limit'] >= -15000:
                        user_dic['limit'] -= money*(1+setting.POUNDAGE)
                    else:
                        print("信用额度已超出！请及时还款！")
                        return
                    money_list.append(user_dic)
                else:
                    print("支付密码错误！")
                    return
            else:
                money_list.append(json.loads(line))
        f.seek(0)
        for l in money_list:
            f.write(json.dumps(l) + '\n')
    print("本次提现：$%s"%money)
    log.log('%s\\log\\card_log' % setting.BASE_DIR, '%s withdraw :$%s successsful!' % (user_name,money))
    return
def refund(): #还款
    pass

@auth.auth(user_type='user')
def card(user_name):
    while True:
        print(('信用卡中心-%s'%user_name).center(100,'*'))
        print("1.转账\t\t\t2.提现\t\t\t3.还款\t\t\t4.退出".center(70))
        choice = input('>:').strip()
        if not choice:continue
        if choice == '1':
            transfer(user_name)
        elif choice == '2':
            withdraw(user_name)
        elif choice == '3':
            refund()
        elif choice == '4':
            return