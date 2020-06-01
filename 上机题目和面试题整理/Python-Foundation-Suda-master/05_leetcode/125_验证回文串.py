"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
空字符有效回文串
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 68ms 41%
        front, rear = 0, len(s) - 1
        while front < rear:
            if not (s[front].isalpha() or s[front].isdigit()):
                front += 1
                continue
            if not (s[rear].isalpha() or s[rear].isdigit()):
                rear -= 1
                continue
            if s[front].lower() == s[rear].lower():
                front += 1
                rear -= 1
            else:
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        # 56ms 67%
        front, rear = 0, len(s) - 1
        while front < rear:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[rear].isalnum():
                rear -= 1
                continue
            if s[front].lower() == s[rear].lower():
                front += 1
                rear -= 1
            else:
                return False
        return True

    def isPalindrome3(self, s: str) -> bool:
        # 正则 52ms 76%
        import re
        #p=''.join(re.findall(r'[\w\d]+',s))
        p=''.join(re.findall(r'[a-zA-Z0-9]+',s))
        p=p.lower()
        return True if p==p[::-1] else False

    def isPalindrome4(self, s):
        s=[i for i in s.lower() if i.isalnum()]
        return s==s[::-1]



if __name__ == "__main__":
    test = "A man, a plan, a canal: Panama"
    # test = "0P"
    S = Solution()
    print(S.isPalindrome(test))