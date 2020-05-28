from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = set('qwertyuiop')
        line2 = set('asdfghjkl')
        line3 = set('zxcvbnm')

        ans = []
        for word in words:
            wset = set(word.lower())
            if wset < line1 or wset < line2 or wset < line3:
                ans.append(word)
        return ans 

def main():
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))

if __name__ == "__main__":
    main()