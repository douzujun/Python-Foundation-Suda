# -*- coding: utf-8 -*-
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
         charSetN = set(name)
         charSetT = set(typed)
         for item in charSetN:
             if item not in charSetT:
                 return False
         for item in charSetT:
            if item not in charSetN:
                return False
        
         i, j = 0, 0
         while i < len(name) and j < len(typed):
             if name[i] == typed[j]:
                i += 1
                j += 1
             else:
                 if j > 0 and typed[j] == typed[j-1]:
                     j += 1
                 else:
                     return False
         if i == len(name):
             return True
         else:
             return False
        
s = Solution()
print(s.isLongPressedName(name = "alex", typed = "aaleex"))
print(s.isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(s.isLongPressedName('abc', 'aaxbc'))
print(s.isLongPressedName("zlexya", "aazlllllllllllllleexxxxxxxxxxxxxxxya"))