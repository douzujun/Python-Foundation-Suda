#-*- coding: utf8 -*-

class Solution:
    def isAlienSorted(self, words, order) -> bool:
        # 可以按列表大小 来排序的
        return words == sorted(words, key=lambda word: [order.index(x) for x in word])


s = Solution()
print(s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))