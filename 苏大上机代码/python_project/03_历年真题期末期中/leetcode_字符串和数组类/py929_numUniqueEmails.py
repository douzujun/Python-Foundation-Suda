# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:11:40 2020

@author: douzi
"""

#    输入：["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#    输出：2
#    解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。

class Solution:
    def numUniqueEmails(self, emails):
        import re
        eset = set()
        for email in emails:
            s = email.split('@')
#            print('email.split(\'@\')', s)
            
            s = s[0].replace('.', '') + '@' + s[1]
#            print('\nreplace: ', s, '\n')
            
            # 替换 所有正则表达式 为 子串 
            # \+ 代表是 + 符号，遇到@ 停止匹配，期间的字符都删除
            s = re.sub(r'\+.*@', '@', s)
            eset.add(s)
            
        print(eset) 
        return len(eset)
        
        
    
s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
