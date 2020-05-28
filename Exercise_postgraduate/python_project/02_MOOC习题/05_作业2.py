"""
n个小朋友围一圈，小朋友从1~n编号。顺时针方向123...n12
游戏开始从1号开始顺时针报数，每个小朋友报上个小朋友数+1
若一个小朋友的数为k的倍数或其个位数为k，则该小朋友出去，不再参加以后的报数
当游戏中只剩下一个小朋友的时候该小朋友获胜
"""


class Solution:
    def Circleplay(self, n, k):
        player = [i for i in range(n)]
        num = 0
        current = 0
        while len(player) > 1:
            num += 1
            if num%k == 0 or num%10 ==k:
                # 小朋友滚的时候不需要移动current
                del player[current]
                current = current % len(player)
            else:
                current = (current+1) % len(player)
        return player[0] + 1 # 小朋友是从1开始编号

if __name__ == "__main__":
    test_1 = (5, 2)
    test_2 = (7, 3)
    
    s = Solution()
    print(s.Circleplay(*test_1))
    print(s.Circleplay(*test_2))