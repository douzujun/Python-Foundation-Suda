"""
环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。

我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按 顺时针和逆时针 的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distance-between-bus-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 68ms 30%
        d1, d2 = 0, 0
        if start > destination:
            start, destination = destination, start
        d1 = sum(distance[:start]) + sum(distance[destination:])
        d2 = sum(distance[start:destination])
        return min(d1, d2)

    def distanceBetweenBusStops2(self, distance, start, destination):
        sum_distance = sum(distance)
        if start <= destination:
            first_distance = sum(distance[start:destination])
        else:
            first_distance = sum(distance[destination:start])
        return min(first_distance, sum_distance-first_distance)


if __name__ == "__main__":
    distance = [1,2,3,4]
    start = 0
    destination = 1
    S = Solution()
    print(S.distanceBetweenBusStops(distance, start, destination))