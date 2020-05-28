# -*- coding: utf-8 -*-
class Solution:
    def stringMatching(self, words):
        ans = []
        wlen = len(words)
        for i in range(wlen):
            for j in range(wlen):
                ss = words[i]
                subs = words[j]
                if ss != subs and ss.find(subs) != -1:
                    ans.append(subs)

        return list(set(ans))
                
s = Solution()

print(s.stringMatching(words = ["mass","as","hero","superhero"]))

print(s.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
