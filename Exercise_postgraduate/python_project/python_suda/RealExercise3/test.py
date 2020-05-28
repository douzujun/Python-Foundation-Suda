# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:06:08 2020

@author: douzi
"""

def is_prime(num):
    if num < 2:
        return False
    import math
    top = int(math.sqrt(num))
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True

ls = [1,1,2,4,4,5,5,6,6,7,0,8,0]
res = []
length = len(ls)

flag = [0]*length

for i in range(length):
    ps = []
    notps = []
    if flag[i] == 0 and is_prime(ls[i]):
        for j in range(i, length):
            if flag[j] == 0 and is_prime(ls[j]):
                ps.append(ls[j])
                flag[j] = 1
            else:
                break
        if ps:
            res.append(ps)
    elif flag[i] == 0:
        for j in range(i, length):
            if flag[j] == 0 and not is_prime(ls[j]):
                notps.append(ls[j])
                flag[j] = 1
            else:
                break
        if notps:
            res.append(notps)
            
print(res)

#y = ['90', '87', '93']
#l = ''
#with open('./file/a.txt', 'w+') as f:
#    for z in y:
#        l += "'{}'".format(z) + ','
#    f.write(l.strip(','))
#    
#    data = f.read()
#    print(data)
#    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    