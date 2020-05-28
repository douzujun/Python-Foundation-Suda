# -*- coding: utf-8 -*-

with open('./test.txt', 'a', encoding = 'utf8') as f:
    # f.write("""Created on Sat May 16 00:14:55 2020 
    #         @author: douzi 
    #         """)
    # ls = ['dou', 'zi', 'is', 'cute']
    # f.writelines(ls)
    f.write('QQ&Wechat\nGoogle & Baidu')
    
with open('./test.txt', 'r', encoding = 'utf8') as f:
    data = f.readlines()
    print(data)
    print(len(data))
    
    
    