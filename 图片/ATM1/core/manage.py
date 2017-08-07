import os
import sys
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting
from core import log
from core import auth
'''
1.添加用户
2.删除用户
3.冻结用户
4.调整用户额度
'''
def user_add():
    '添加用户'
    while True:
        user_name = str(input("请输入要创建的用户名：(Q/q)").strip())
        if user_name == 'q' or user_name == 'Q':
            break
        user_password = input("请输入密码：").strip()
        user_dic = {
                    'name':user_name,
                    'password':user_password,
                    'login_status':False,
                    'frost_status':False,
                    'login_times':0,
                    'limit':setting.USER_LIMIT,
                    'pay_mm':'1'
        }
        user_json = json.dumps(user_dic)
        with open('%s\\user'%setting.DATABASE_PATH,'a+') as f:
            for line in f:
                if user_dic['name'] == json.loads(line)['name']:
                    print("该用户已存在！")
                    break
            else:
                f.write('\n')
                f.write(user_json)
                print('创建成功！')
                log.log('%s\\log\\manage_log' % BASE_DIR, 'add user:%s successs'%user_name)

def user_del():
    user_name = input("请输入要删除的用户名：").strip()
    user_list = []
    with open('%s\\user'%setting.DATABASE_PATH,'r+') as f:
        for line in f:
            try:
                if user_name == json.loads(line)['name']:
                    continue
                else:
                    user_list.append(json.loads(line))
            except Exception:
                pass
        f.seek(0)
        for l in user_list:
            f.write(json.dumps(l)+'\n')
        print("删除成功！")
        log.log('%s\\log\\manage_log' % BASE_DIR, 'del user:%s successs' % user_name)

def user_frost():
    user_name = input("需要冻结的用户：").strip()
    user_list = []
    with open('%s\\user' % setting.DATABASE_PATH, 'r+') as f:
        for line in f:
            if user_name == json.loads(line)['name']:
                user_dic = json.loads(line)
                user_dic['frost_status'] = True
                user_list.append(user_dic)
            else:
                user_list.append(json.loads(line))
        f.seek(0)
        for l in user_list:
            f.write(json.dumps(l) + '\n')
        print("冻结成功！")
        log.log('%s\\log\\manage_log' % BASE_DIR, 'frost user:%s successs' % user_name)

def set_limit():
    user_name = input("请输入要修改限额的用户：").strip()
    limit = int(input("设置限额：").strip())
    user_list = []
    with open('%s\\user' % setting.DATABASE_PATH, 'r+') as f:
        for line in f:
            if user_name == json.loads(line)['name']:
                user_dic = json.loads(line)
                user_dic['limit'] = limit
                user_list.append(user_dic)
            else:
                user_list.append(json.loads(line))
        f.seek(0)
        for l in user_list:
            f.write(json.dumps(l)+'\n')
        print("修改用户限额成功！")
        log.log('%s\\log\\manage_log' % BASE_DIR, 'change user:%s limit to:%s' % (user_name,limit))

@auth.auth(user_type='admin')
def manage():
    log.log('%s\\log\\manage_log'%BASE_DIR,'admin login in ')
    while True:
        print("后台管理".center(100, '*'))
        print("1.添加用户\t\t\t2.删除用户\t\t\t3.冻结用户\t\t\t4.设置用户额度\t\t\t5.退出".center(80, ))
        choice = int(input('>:').strip())
        if not choice:continue
        if choice == 1:
            user_add()
        elif choice == 2:
            user_del()
        elif choice == 3:
            user_frost()
        elif choice == 4:
            set_limit()
        elif choice == 5:
            log.log('%s\\log\\manage_log'%BASE_DIR,'admin login out')
            return

