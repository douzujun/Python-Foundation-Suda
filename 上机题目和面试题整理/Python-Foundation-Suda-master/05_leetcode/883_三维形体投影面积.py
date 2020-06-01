"""
在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def projectionArea(self, grid: list) -> int:
        xy, xz, yz = len(grid)**2, 0, 0

        for item in grid:
            xz += max(item)
        
        for i in range(len(grid)):
            yz += max([item[i] for item in grid])

        for item in grid:
            xy -= item.count(0)

        return xy+xz+yz


if __name__ == "__main__":
    test = [[1,2],[3,4]]
    s1 = Solution()
    print(s1.projectionArea(test))