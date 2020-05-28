# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:13:00 2020

@author: douzi
"""

# 输入： nums = [1,2,3]
# 输出：
#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#]
class Solution:
    def subsets(self, nums):
        result = []
        result.append([])
        for i in nums:
            print(i)
            length = len(result)
            j = 0
            while j < length:
                result.append(result[j] + [i])
                j += 1
                
        return result
    
s = Solution()
print(s.subsets([1, 2, 3]))