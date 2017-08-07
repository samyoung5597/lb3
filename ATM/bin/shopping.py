import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core import main
from core import auth

bash_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(bash_dir)
menu_path = bash_dir + '/db/menu.json'
def show_menu_list():
    with open(menu_path) as f:
        menu_list = json.loads(f.read())
        return menu_list

def add_menu(name,price,number):

    with open(menu_path) as f:
        old_menu_list = json.loads(f.read())
    with open(menu_path,'w') as f:
        old_menu_list[name] = [price,number]
        menu_list_json = json.dumps(old_menu_list)
        f.write(menu_list_json)

def show_menu():
    cart = {}
    menu_list = show_menu_list()
    print('%s %8s %8s' % ('序号', '商品名', '价格'))
    for i,item in enumerate(menu_list,1):
        print('%s %10s %10s'%(i,item[0],item[1]))
    print('输入q 退出！')

    while True:
        chocie = input('Please input : ').strip()
        if chocie.isdigit() or chocie =='q':

            if chocie == 'q':
                return cart
            elif int(chocie) >0 and int(chocie) <= len(menu_list):
                info = menu_list[int(chocie) - 1]
                if cart.get(info[0]):
                    cart[info[0]][1] += 1
                    if cart[info[0]][1] > info[2]:
                        print('商品数量不够！')
                        cart[info[0]][1] -= 1
                else:
                    cart[info[0]] = [info[1],1]
            else:
                print('输出错误 没有该商品！')

def add_all(args):
    sum_price = 0
    print('购物清单'.center(50, '-'))
    print('%s %8s %8s %8s' % ('序号', '商品名', '数量', '总价'))
    for i,key in enumerate(args,1):
        value = args[key]
        print('%s %10s %10s %10s'%(i,key,value[1],value[0]*value[1]))
        sum_price += value[0]*value[1]
    print('合计: %30s'%sum_price)
    print('end'.center(50, '-'))

    return sum_price


def run():
    cart = show_menu()
    sum_price = add_all(cart)
    counts = '1234'
    choose_pay = input('1、现金 2、信用卡 请选择>>: ')
    if choose_pay == '2':
        auth.xiaofei(sum_price,counts)
        return

run()

