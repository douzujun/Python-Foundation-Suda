# -*- coding: utf-8 -*-


from typing import List

class Solution:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import math
        ans = []
        def distance(s, e):
            return math.sqrt( (s[0]-e[0])**2 + (s[1]-e[1])**2 )
        
        dis = []
        for p in points:
            dis.append((p, distance(p, (0,0))))
            
        dis.sort(key=lambda x:x[1])
        
        for i in range(K):
            ans.append(dis[i][0])
    
        return ans
    
s = Solution()
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))
