# -*- coding: utf-8 -*-
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        st = re.findall('[a-zA-Z0-9]', s.lower())
        slen = len(st)
        for i in range(slen):
            if st[i] != st[slen - i - 1]:
                return False
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))