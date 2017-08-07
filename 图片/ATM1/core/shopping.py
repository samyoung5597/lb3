import os
import sys

import json
from conf import setting
from core import login

def shopping():
    print("商品列表".center(100, '*'))
    with open('%s\\db\\shoppings'%setting.BASE_DIR,'r') as f:
        for line in f:
            product_list = eval(str(line))
    shopping_cart = []
    total_money = 0
    while True:
        index = 0
        for product in product_list:
            print(index, "---", product)
            index += 1
        print('s','---','结账')
        print('q','---','退出')
        choice = input(">>:").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice <= len(product_list):
                product = product_list[choice]  # 取到商品
                shopping_cart.append(product)  # 加入购物车
                total_money += product[1]  # 累计价钱
                print("已将" + product[0] + "添加到你的购物车")
            else:
                print("商品不存在!")
        elif choice == "s":
            with open('%s\\db\\shop_cart'%setting.BASE_DIR,'w') as f:
                f.write(json.dumps(shopping_cart))
                f.write('\n')
                f.write(json.dumps({'total_money':total_money}))
            print("-------已购买商品列表--------")
            for i in shopping_cart:
                print(i)
            print("总价:", total_money)
            print("------------end------------")
            # 登录系统
            login.login(total_money,shopping_cart)
            break
        elif choice == 'q':
            print("欢迎下次光临！")
            exit()