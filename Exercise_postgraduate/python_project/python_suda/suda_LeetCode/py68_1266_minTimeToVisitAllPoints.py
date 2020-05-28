# -*- coding: utf-8 -*-
class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        x0, x1 = points[0][0], points[0][1]
        ans = 0
        plen = len(points)
        for i in range(1, plen):
            y0, y1 = points[i][0], points[i][1]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = y0, y1
        return ans

s = Solution()
print(s.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
print(s.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))
