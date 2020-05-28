# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nlen = len(nums)
        self.t = [0]*self.nlen

        self.visit = [0] * self.nlen
        def dfs(nums, cur):
            if cur == self.nlen:
                self.ans.append(self.t.copy())
                return

            for i in range(self.nlen):
                if not self.visit[i]:
                    self.t[cur] = nums[i]
                    self.visit[i] = True       # 回溯
                    dfs(nums, cur + 1)  
                    self.visit[i] = False      # 回溯
        dfs(nums, 0)
        return self.ans

    # In [6]: list(permutations([1,2,3], 3))
    # Out[6]: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    def permute2(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        ans = [list(x) for x in permutations(nums, len(nums))]
        return ans 

s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute2([1, 2, 3]))