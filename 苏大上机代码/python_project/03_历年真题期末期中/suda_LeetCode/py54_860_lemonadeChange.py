# -*- coding: utf-8 -*-

class Solution:
    def lemonadeChange(self, bills) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
            
s = Solution()

print(s.lemonadeChange([5,5,5,10,20]))
print(s.lemonadeChange([5,5,10]))
print(s.lemonadeChange([10,10]))
print(s.lemonadeChange([5,5,10,10,20]))
print(s.lemonadeChange([5,5,10,10,20]))