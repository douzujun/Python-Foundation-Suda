# -*- coding: utf-8 -*-

class Solution:
    def oddCells(self, n, m, indices) -> int:
        ans = [[0]*m for i in range(n)]
        
        for b in indices:
            row = b[0]
            col = b[1]
            
            cnt = len(ans[0])
            for i in range(cnt):
                ans[row][i] += 1
                
            cnt = len(ans)
            for i in range(cnt):
                ans[i][col] += 1
            
        ans = [e for ei in ans for e in ei if e % 2 == 1]
        
        return len(ans)
        
    
s = Solution()
print(s.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
print(s.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))
print(s.oddCells(2, 2, [[1,1],[0,0]]))
