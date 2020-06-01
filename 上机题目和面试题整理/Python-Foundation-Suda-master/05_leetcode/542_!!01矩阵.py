"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

曼哈顿距离（横竖到达另一个点走的步数）
https://leetcode-cn.com/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
"""


class Solution:
    def updateMatrix(self, matrix: list) -> list:
        # 780ms  每个元素广度优先搜索 找0
        result = []
        for i, row in enumerate(matrix):
            result.append([])
            for j in range(len(row)):
                # 找到到最近0的距离
                dis = 0
                i_t, j_t = i, j
                step, dirc = 0, 3
                dirction = ((-1, -1), (-1, 1), (1, 1), (1, -1))
                while True:
                    if 0 <= i_t < len(matrix) and 0 <= j_t < len(matrix[0]) \
                            and matrix[i_t][j_t] == 0:
                        # 判断是否找到0
                        result[i].append(dis)
                        break
                    else:
                        if step < dis:
                            # 走一侧
                            i_t += dirction[dirc][0]
                            j_t += dirction[dirc][1]
                            step += 1
                        elif dirc < 3:
                            # 换方向
                            step = 0
                            dirc += 1
                        else:
                            # 换一圈
                            dis += 1
                            step, dirc = 0, 0
                            i_t, j_t = i + dis, j
        return result

    def updateMatrix2(self, matrix: list) -> list:
        # 1268ms  从“超级源点”开始广度优先搜索
        import collections
        # 找到所有的0元素
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)
        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        
        return dist
        
    def updateMatrix3(self, matrix):
        # 动态规划 1288ms
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist

    def updateMatrix4(self, matrix: List[List[int]]) -> List[List[int]]:
        # 860ms
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


if __name__ == "__main__":
    test1 = [[0, 1, 0, 0],
             [1, 1, 1, 1],
             [0, 1, 1, 1],
             [0, 1, 1, 1]]
    s = Solution()
    print(s.updateMatrix3(test1))
