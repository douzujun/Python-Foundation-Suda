"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 32ms 91.98%
        stack = []
        ch_d = {'(':')', '[':']', '{':'}'}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif len(stack) > 0:
                if ch != ch_d[stack.pop()]:
                    return False
            else:
                return False
        else:
            return len(stack) == 0


if __name__ == "__main__":
    test = "()[]{}"
    S = Solution()
    print(S.isValid(test))