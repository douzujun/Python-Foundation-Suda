# -*- coding: utf-8 -*-

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = s[n:] + s[:n]
        return s