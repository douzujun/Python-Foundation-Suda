# -*- coding: utf-8 -*-

class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.sort(reverse=True)
        
        print(stones)
        i = 0
        while len(stones) > 1:
            x = stones[i+1]
            y = stones[i]
            if x == y:
                stones.remove(x)
                stones.remove(y)
            if x != y:
                stones.remove(x)
                stones.remove(y)
                stones.append(y - x)
            stones.sort(reverse=True)

        if len(stones) > 0:
            return stones[0]
        else:
            return 0
          
s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
print(s.lastStoneWeight([5,1,8,10,7]))
        
        
        