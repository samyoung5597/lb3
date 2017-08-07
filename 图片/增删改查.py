
def menu():
    menu = {"1": "增加", "2": "删除", "3": "修改", "4": "查询", "5": "退出"}
    mm = list(sorted(zip(menu.keys(), menu.values())))
    for i in mm:
        print('%s-----%s' % (i[0], i[1]))



def search():
    l = []
    flag = True
    while flag:
        url = input("please input url you want to search:").strip()  # 输入想要查询的域名
        with open("haproxy.conf", encoding="utf8") as s:  # 打开文件
            for line in s:
                if line.startswith("backend") and url in line:  # 第一步，读到想要查询的域名所在的行，改变标志位状态
                    flag = False
                    continue
                if line.startswith("backend") and flag == False:  # 第三步，再次读取域名所在的行后，本次循环结束
                    break

                if flag == False:  # 第二步，将域名下的ip所在行写入列表中
                    l.append(line)
        for i in l:  # 第四步，打印需要查询的域名下的ip地址所在的行
            print(i.strip())
        break


def delete():
    flag = True
    l = []
    url = input("input url you want to delete:").strip()  # 输入想删除的ip地址所对应的域名
    ip = input("input ip you want to delete:").strip()  # 输入想要删除的域名
    while flag:
        with open("haproxy.conf") as d, \
                open("haproxy.conf_delete", "w+") as d_2:  # 打开原文档haproxy.conf ，创建删除后的文档haproxy.conf_delete
            for line in d:
                if line.startswith("backend") and url in line:  # 第二步，当读取到想删除的ip地址对应的域名所对应的行
                    d_2.writelines(line)  # 将该行写入haproxy.conf_delete文档中
                    flag = False
                    continue
                if flag:  # 第三步，将域名下所对应的ip行写入列表中
                    d_2.writelines(line)
                if line.startswith("backend") and flag == False:
                    # 第四步，第二次读到域名行，将列表里的内容写入haproxy.conf_delete文档中，要删除的ip行不写入文档中
                    flag = True
                    l.append(line)
                    for line in l:
                        if ip in line:
                            continue
                        d_2.writelines(line)
                if flag == False:  # 第三步，将域名下所对应的ip行写入列表中
                    l.append(line)
                    print(l)
        break


def add():
    url = input("please input url you want to add:").strip()  # 输入想要增加ip所在的域名和增加的ip所在行
    ip = input("please input ip you want to add:")
    with open("haproxy.conf") as a, open("haproxy.conf_add", "w") as a_2:  # 打开文档haproxy.conf，新建文档haproxy.conf_add
        for line in a:
            a_2.writelines(line)  # 循环写入读取到的行到文档haproxy.conf_add中
            if line.startswith("backend") and url in line:
                a_2.writelines(ip)  # 当读取到ip所在的域名，将要加入的ip所在的行写入文档haproxy.conf_add中
                a_2.writelines("\n")


def change():
    l = []
    flag = True
    url = input("please input url you want to change:").strip()  # 输入想要修改ip所在的域名
    ip = input("please input ip you want to change:")  # 输入想要修改ip所在行
    ip_changed = input("please input ip you want to changed:")  # 输入想要修改过ip所在行
    with open("haproxy.conf") as c, open("haproxy.conf_change", "w") as c_2:  ##打开文档haproxy.conf，新建文档haproxy.conf_change
        for line in c:
            if line.startswith("backend") and url in line:
                c_2.writelines(line)  # 第二步，读到想要修改ip所在的域名的行将该行写入文档haproxy.conf_change
                flag = False  # 改变标志位状态
            if line.startswith("backend") and flag == False:
                for line in l:  # 第四步，循环到列表中需要改变的ip地址，将修改过的ip地址写入文档haproxy.conf_change中
                    if line == ip:
                        c_2.writelines(ip_changed)
                        continue
                    c_2.writelines(line)  # 将列表中其他内容写入文档haproxy.conf_change中
                flag = True
            if flag:  # 第一步，将读到的行写入文件haproxy.conf_change中
                c_2.writelines(line)
            if flag == False:  # 第三步，将域名所在的行放入列表中
                l.append(line)


def main():
    while True:
        menu()
        choice = int(input("input your choice:"))
        if choice == 1:
            add()
        elif choice == 2:
            delete()
        elif choice == 3:
            change()
        elif choice == 4:
            search()
        elif choice == 5:
            break


main()