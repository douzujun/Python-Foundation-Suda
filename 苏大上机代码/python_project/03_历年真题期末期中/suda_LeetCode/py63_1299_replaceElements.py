# -*- coding: utf-8 -*-

class Solution:
    def replaceElements(self, arr):
        alen = len(arr)
        ans = [0]*alen
        ans[alen - 1] = -1
        # [alen-2, 0] 逆序
        for i in range(alen - 2, -1, -1):
#            print('ans[i+1]:', ans[i+1], ' arr[i+1]:', arr[i + 1])
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans
    
s = Solution()
print(s.replaceElements(arr = [17,18,5,4,6,1]))

