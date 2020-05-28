# -*- coding: utf-8 -*-
class Solution:
    def findOcurrences(self, text: str, first: str, second: str): 
        tli = text.split()
        rlen = len(tli)
        ans = []
        for i in range(rlen - 2):
            if tli[i] == first and tli[i + 1] == second:
                ans.append(tli[i + 2])
        return ans


s = Solution()
print(s.findOcurrences(text = "we will we will rock you", first = "we", second = "will"))
