# -*- coding: utf-8 -*-
class Solution:
    def diagonalSort(self, mat):
        import collections
        import itertools
        row = len(mat)
        col = len(mat[0])
        
        # 初始化字典值为 []
        dic = collections.defaultdict(list)
        for i, j in itertools.product(range(row), range(col)):
            print(i, j)
            dic[i - j].append(mat[i][j])
        print(dic)
        
        dic = {k: iter(sorted(v)) for k, v in dic.items()}
        print(dic)
        for i, j in itertools.product(range(row), range(col)):
            mat[i][j] = next(dic[i - j])
        return mat
    
    def dig(self, mat):
        m, n = len(mat), len(mat[0])
        tmp = []
        for line in range(m+n-1):
            i, j = m-1-line, 0
            tmp.clear()
            while j < n:
                if 0 <= i < m and 0 <= j < n:
                    tmp.append(mat[i][j])
                i += 1
                j += 1
            print(tmp)
        

s = Solution()
#print(s.diagonalSort(mat = [[3,3,1,1], [2,2,1,2], [1,1,1,2]]))
print(s.dig(mat = [[3,3,1,1], [2,2,1,2], [1,1,1,2]]))
