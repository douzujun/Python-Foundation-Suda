# -*- coding: utf-8 -*-

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        return num.replace('6', '9', 1)
    
    
s = Solution()
print(s.maximum69Number(9669))
print(s.maximum69Number(9996))
print(s.maximum69Number(9999))