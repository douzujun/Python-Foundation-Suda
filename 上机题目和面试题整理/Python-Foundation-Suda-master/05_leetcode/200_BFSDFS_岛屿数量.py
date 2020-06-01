"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

类似的题 542 01矩阵 面试题13 
"""


class Solution:
    def numIslands(self, grid: list) -> int:
        # 64ms 96.81%
        count = 0
        queue = []
        # 获取grid的长宽
        m = len(grid)
        if m:
            n = len(grid[0])
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 找到了一块岛屿
                    count += 1
                    # 将这块岛屿置为0
                    queue.append((i, j))
                    while len(queue) > 0:
                        i_t, j_t = queue.pop()
                        grid[i_t][j_t] = '0'
                        # 四个方向扩张
                        if 0 <= i_t-1 < m and grid[i_t-1][j_t] == '1':  # 上
                            queue.append((i_t-1, j_t))
                        if 0 <= j_t+1 < n and grid[i_t][j_t+1] == '1':  # 右
                            queue.append((i_t, j_t+1))
                        if 0 <= i_t+1 < m and grid[i_t+1][j_t] == '1':  # 下
                            queue.append((i_t+1, j_t))
                        if 0 <= j_t-1 < n and grid[i_t][j_t-1] == '1':  # 左
                            queue.append((i_t, j_t-1))
        return count


    def numIslands2(self, grid: List[List[str]]) -> int:
        import collections
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':  # 发现陆地
                    count += 1  # 结果加1
                    grid[row][col] = '0'  # 将其转为 ‘0’ 代表已经访问过
                    # 对发现的陆地进行扩张即执行 BFS，将与其相邻的陆地都标记为已访问
                    # 下面还是经典的 BFS 模板
                    land_positions = collections.deque()
                    land_positions.append([row, col])
                    while len(land_positions) > 0:
                        x, y = land_positions.popleft()
                        for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:  # 进行四个方向的扩张
                            # 判断有效性
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'  # 因为可由 BFS 访问到，代表同属一块岛，将其置 ‘0’ 代表已访问过
                                land_positions.append([new_x, new_y])
        return count




if __name__ == "__main__":
    test = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    test2 = [["1", "1", "1"],
             ["0", "1", "0"],
             ["1", "1", "1"]]

    s = Solution()
    print(s.numIslands(test))
