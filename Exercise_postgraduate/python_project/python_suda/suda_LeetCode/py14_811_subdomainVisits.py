# -*- coding: utf-8 -*-
class Solution:
    def subdomainVisits(self, cpdomains): 
        if not cpdomains:
            return []
        
        res = {}
        for case in cpdomains:
            time, domain = case.split()
            length = len(domain.split('.'))
            for num in range(length):
                dm = domain.split('.', num)[-1]
                res[dm] = res.get(dm, 0) + int(time)

        return [str(v) + ' ' + k for k, v in res.items()]
    
    
s = Solution()
print(s.subdomainVisits(["9001 discuss.leetcode.com"]))
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# 例子中仅包含一个网站域名："discuss.leetcode.com"。
# 按照前文假设，子域名"leetcode.com"和"com"都会被访问，所以它们都被访问了9001次。

print(s.subdomainVisits(["900 google.mail.com", 
                         "50 yahoo.com", 
                         "1 intel.mail.com", 
                         "5 wiki.org"]))
# ["901 mail.com", "50 yahoo.com", "900 google.mail.com",
#  "5 wiki.org","5 org", "1 intel.mail.com", "951 com"]
# 说明: 
# 按照假设，会访问"google.mail.com" 900次，"yahoo.com" 50次，
# "intel.mail.com" 1次，"wiki.org" 5次。
# 而对于父域名，会访问"mail.com" 900+1 = 901次，"com" 900 + 50 + 1 = 951次，和 "org" 5 次。
    
    
    
    
    
    
    
    
