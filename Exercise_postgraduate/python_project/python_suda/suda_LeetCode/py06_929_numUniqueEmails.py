# -*- coding: utf-8 -*-

class Solution:
    def numUniqueEmails(self, emails) -> int:
        import re
        eset = set()
        
        for email in emails:
            s = email.split('@')
            
            s = s[0].replace('.', '') + '@' + s[1]
            
            s = re.sub('\+.*@', '@', s)
            eset.add(s)
            
        print(eset)
        return len(eset)
    
s = Solution()

print(s.numUniqueEmails(["test.email+alex@leetcode.com",
                         "test.e.mail+bob.cathy@leetcode.com",
                         "testemail+david@lee.tcode.com"]))
        