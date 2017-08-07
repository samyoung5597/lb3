import os
import sys
from conf import setting
from core import log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import json
def auth(user_type):
    def auth1(func):
        def wrapper(*args,**kwargs):
            if user_type == 'admin':
                admin_list = []
                with open('%s\\db\\admin' % BASE_DIR, 'r+') as f:
                    for line in f:
                        admin_list.append(json.loads(line))
                    flag = True
                    while flag:
                        user_name = str(input("用户名：").strip())
                        password = str(input("密码：").strip())
                        for l in admin_list:
                            if (user_name == l['name']) and (password == l['password']) and (l['login_times'] < 3):
                                print("登录成功！")
                                func(*args, **kwargs)
                                flag = False
                                break
                            elif int(l['login_times']) >= 3:
                                print("账号已锁定！")
                                flag = False
                                break
                            elif (user_name == str(l['name'])) and (password != str(l['password'])):
                                if l['login_times'] == 2:
                                    l['login_times'] += 1
                                    flag = False
                                    print("账号已锁定！")
                                    break
                                else:
                                    l['login_times'] += 1
                                    print("用户名或密码错误，请重新输入！")
                                    break
                        continue
                    f.seek(0)
                    for l in admin_list:
                        f.write(json.dumps(l)+'\n')
            elif user_type == 'user':
                user_list = []
                with open('%s\\db\\user' % BASE_DIR, 'r+') as f:
                    for line in f:
                        try:
                            user_list.append(json.loads(line))
                        except Exception:
                            pass
                    flag = True
                    while flag:
                        user_name = str(input("用户名：").strip())
                        password = str(input("密码：").strip())
                        for l in user_list:
                            if (user_name == l['name']) and (password == l['password']) and (l['login_times'] < 3):
                                print("登录成功！")
                                l['login_status'] = True
                                args_list = list(args)
                                args_list.insert(0,user_name)
                                args = tuple(args_list)
                                func(*args,**kwargs)
                                flag = False
                                break
                            elif user_name == l['name'] and l['login_times'] >= 3:
                                print("账号已锁定！")
                                flag = False
                                break
                            elif user_name == str(l['name']) and password != str(l['password']):
                                if l['login_times'] == 2:
                                    l['login_times'] += 1
                                    flag = False
                                    print("账号已锁定！")
                                    break
                                else:
                                    l['login_times'] += 1
                                    print("用户名或密码错误，请重新输入！")
                                    break
                        continue
                    f.seek(0)
                    for l in user_list:
                        f.write(json.dumps(l)+'\n')
            return
        return wrapper
    return auth1