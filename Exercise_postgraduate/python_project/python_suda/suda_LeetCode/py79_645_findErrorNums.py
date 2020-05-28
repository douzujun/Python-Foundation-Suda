# -*- coding: utf-8 -*-

class Solution:
    def findErrorNums(self, nums):
        ans = []
        nlen = len(nums)
        
        counts = [0]*(nlen+1)
        for e in nums:
            counts[e] += 1
        
        print(counts)
        for i in range(1, nlen+1):
            if counts[i] == 0:
                if len(ans) < 1:
                    ans.append(i)
                else:
                    ans.append(i)
                    break
            elif counts[i] == 2:
                if len(ans) < 1:
                    ans.append(i)
                else:
                    ans.append(i)
                    break
                    
        if counts[ans[0]] > 1:
            return ans
        else:
            return ans[::-1]
        
s = Solution()
print(s.findErrorNums([3,2,3,4,6,5]))
