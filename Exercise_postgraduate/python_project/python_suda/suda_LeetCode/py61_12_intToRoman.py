# -*- coding: utf-8 -*-

#字符          数值
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
#X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
#C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 
                   90:'XC', 50:'L', 40:'XL',
                   10:'X', 9:'IX', 5:'V' , 4:'IV', 1:'I'}
        ans = ''
        for key in hashmap:
            count = num // key
            if count != 0:
                ans += hashmap[key] * count
                num %= key
        return ans 

s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(4))
print(s.intToRoman(9))
print(s.intToRoman(58))
print(s.intToRoman(1994))