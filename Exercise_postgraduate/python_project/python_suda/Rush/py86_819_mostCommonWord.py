from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        words = re.findall('[a-z]+', paragraph.lower())
        wmax = ''
        for word in words:
            if word not in banned and words.count(wmax) < words.count(word):
                wmax = word 
        return wmax

s = Solution()
print(s.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))