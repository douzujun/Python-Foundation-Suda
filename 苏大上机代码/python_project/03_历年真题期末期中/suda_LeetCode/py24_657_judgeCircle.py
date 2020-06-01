# -*- coding: utf-8 -*-

class Solution:
    def judgeCircle(self, moves: str) -> bool:
#        res = 0
#        for e in moves:
#            if e == 'U':
#                res = res + 1
#            elif e == 'D':
#                res = res - 1
#            if e == 'R':
#                res = res + 9999
#            elif e == 'L':
#                res = res - 9999
#        
#        if res == 0:
#            return True
#        else:
#            return False
        return moves.count('D')==moves.count('U') and moves.count('R')==moves.count('L')
        
        
s = Solution()
print(s.judgeCircle('UD'))
print(s.judgeCircle('LL'))
print(s.judgeCircle('RRDD'))

print(s.judgeCircle("UDDUURLRLLRRUDUDLLRLURLRLRLUUDLULRULRLDDDUDDDDLRRDDRDRLRLURRLLRUDURULULRDRDLURLUDRRLRLDDLUUULUDUUUUL"))
        
        
        