# -*- coding: utf-8 -*-

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        
        i = j = 0
        m, n = len(str1), len(str2)
        while i < m or j < n:
            # 只有在 S = T + ... + T（T 与自身连接 1 次或多次）时
            if str1[i % m] != str2[j % n]:
                return ''
            i += 1
            j += 1
        
        def gcd(m, n):
            if m < n:
                m, n = n, m      # m--大，n--小
            
            while m % n:
                t = m % n
                m = n
                n = t
            return n
                
        return str1[:gcd(m, n)]
    


s = Solution()
print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
