class Solution:
    def Circleplay(self, n, k):
        player = [i for i in range(n)]   # 0 ~ n-1
        cur = 0     # 当前报号
        num = 0
        while len(player) > 1:
            num += 1
            if num % k == 0 or num % 10 == k:
                del player[cur]
                cur = cur % len(player)    # 小朋友走的时候，不需要移动 cur
            else:
                cur = (cur + 1) % len(player)
        
        return player[0] + 1

s = Solution()
print(s.Circleplay(5, 2))
print(s.Circleplay(7, 3))
