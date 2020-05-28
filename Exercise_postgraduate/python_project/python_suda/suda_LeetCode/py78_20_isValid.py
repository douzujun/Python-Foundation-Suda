# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for e in s:
            if e in ['(', '[', '{']:
                ans.append(e)
            elif e == ')':
                if ans:
                    t = ans.pop()
                    if t != '(':
                        return False
                else:
                    return False
            elif e == ']':
                if ans:
                    t = ans.pop()
                    if t != '[':
                        return False
                else:
                    return False
            elif e == '}':
                if ans:
                    t = ans.pop()
                    if t != '{':
                        return False
                else:
                    return False
        if ans:
            return False
        else:
            return True
    
s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid(']'))