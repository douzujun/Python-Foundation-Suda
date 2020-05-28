"""
给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。

另有一个索引数组 indices，indices[i] = [ri, ci] 中的

 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。

请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def oddCells(self, n: int, m: int, indices: list) -> int:
        # 模拟法
        Mat = [[0 for _ in range(m)] for _ in range(n)]
        for i, j in indices:
            Mat[i] = [1 + c for c in Mat[i]]
            for k in range(n):
                Mat[k][j] = Mat[k][j] + 1
        count = 0
        for row in Mat:
            for col in row:
                if col % 2 != 0:
                    count += 1
        return count

    def oddCells2(self, n, m, indices):
        # 模拟+空间优化
        row = [0] * n
        col = [0] * m
        for i, j in indices:
            row[i] += 1
            col[j] += 1
        count = 0
        for i in range(n):
            for j in range(m):
                if (row[i] + col[j]) % 2 != 0:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.oddCells2(2, 3, [[0, 1], [1, 1]]))
