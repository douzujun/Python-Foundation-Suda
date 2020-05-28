# -*- coding: utf-8 -*-

def solve():
    d, L, R = eval(input())
    ans = 0
    for num in range(L, R+1):
        nstr = str(num)
        if str(d) in nstr:
           ans += nstr.count(str(d))
        
    if ans:
        print(ans)
    else:
        print(None)

solve()
          