# -*- coding: utf-8 -*-

class Solution:
    def groupAnagrams(self, strs):
        combs = {}
        for s in strs:
            st =  ''.join(sorted(s))
            if st not in combs:
                combs[st] = []
            combs[st].append(s)
        
        ans = []
        for k, v in combs.items():
            ans.append(sorted(v))

        return ans

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        