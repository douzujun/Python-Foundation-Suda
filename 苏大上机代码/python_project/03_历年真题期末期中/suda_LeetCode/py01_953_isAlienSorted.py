# -*- coding: utf-8 -*-

class Solution:
    def isAlienSorted(self, words, order) -> bool:
#        dic = {}
#        for e in order:
#            dic[e] = dic.get(e, 0) + order.index(e)
#        
#        wlen = len(words)
#        flag = 0
#        for i in range(0, wlen):
#            A = words[i]
#            Alen = len(A)
#            for j in range(i + 1, wlen):
#                B = words[j]
#                Blen = len(B)
#                mlen = Alen if Alen < Blen else Blen     # 小的长度
#                for k in range(mlen):
##                    print(A[k], B[k])
#                    if dic[A[k]] < dic[B[k]]:  
#                        flag = 1
#                        break
#                    elif dic[A[k]] > dic[B[k]]:
#                        return False
#
#        if flag:
#            return True
#        else:
#            return False
        return words == sorted(words, key=lambda w:[order.index(x) for x in w])
        
        
s = Solution()

print(s.isAlienSorted(words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
print(s.isAlienSorted(["iekm","tpnhnbe"], "loxbzapnmstkhijfcuqdewyvrg"))
print(s.isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
, "zkgwaverfimqxbnctdplsjyohu"))
print(s.isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"))