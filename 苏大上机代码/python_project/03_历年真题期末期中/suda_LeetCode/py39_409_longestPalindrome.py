# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)                
        
        res, odd_flag = 0, 0   # 结果, 奇数次flag设置为0
        for k, v in counter.items():
            res += (v // 2) * 2  # 偶数则偶数次；奇数，则小于奇数的最大偶数
            if v % 2 == 1:       # 有奇数，则最后再+1
                odd_flag = 1
                
        return res + odd_flag

        
s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("bananas"))
