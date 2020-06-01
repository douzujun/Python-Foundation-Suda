"""
分析uwsgi.log文件
统计访问的ip数量
统计需要登录才可继续访问的次数。
"""
import re

filename='./uwsgi.log'

def count_ip(visit_list):
    ip = set()
    login_str = r'/account/login/?'
    count_login = 0
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    for line in visit_list:
        ipmatch = re.search(pattern, line)
        if ipmatch:
            ip.add(ipmatch.group())
        if login_str in line:
            count_login += 1
    return ip, count_login


if __name__ == "__main__":
    f = open(filename, 'r')
    visit_list = f.readlines()
    f.close()

    ip, count = count_ip(visit_list)
    print("共有",len(ip), "个ip访问了您的网站")
    a = list(ip)
    a.sort()
    print(a)
    print("其中有", count, "次访问被转向至登录")

