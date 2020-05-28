# -*- coding: utf-8 -*-

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for s in S:
            if s in J:
                res += 1
        return res


s = Solution()
print(s.numJewelsInStones('aA', 'aAAbbbb'))
print(s.numJewelsInStones('z', 'ZZ'))
        