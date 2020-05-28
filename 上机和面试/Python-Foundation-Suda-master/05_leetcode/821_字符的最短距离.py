"""
给定一个字符串 S 和一个字符 C。
返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""
class Solution:
    def shortestToChar(self, S: str, C: str) -> list:
        C_loc = [i for i in range(len(S)) if S[i] == C ]
        distance = []

        head = 0
        # 更新 第一个 C 前面的距离
        for i in range(C_loc[head]):
            distance.append(C_loc[head] - i)
        # S 中只有一个 C 的情况
        if len(C_loc) == 1:
            for i in range(0, len(S) - C_loc[head]):
                distance.append(i)
        else:
            # 处理两个 C 中间的距离
            tail = 1
            while tail <= len(C_loc)-1:
                mid = (C_loc[head] + C_loc[tail]) // 2
                for i in range(0, mid - C_loc[head] + 1):
                    distance.append(i)
                for i in range(C_loc[tail] - mid - 1, 0, -1):
                    distance.append(i)
                head += 1
                tail += 1
            else:
                for i in range(0, len(S) - C_loc[-1]):
                    distance.append(i)
        return distance

    def shortestToChar2(self, S: str, C: str) -> list:
        # 左右指针
        left = 0
        result = [float('inf') for i in S]

        for right in range(0, len(S)):
            if S[right] is C:
                for i in range(left, right + 1):
                    result[i] = min(result[i], right - i)
                left = right
            elif S[left] is C:
                result[right] = min(result[right], right - left)

        return result

if __name__ == "__main__":
    # S = "loveleetcod"
    S = "eaaeabcbaeabbae"
    C = "e"
    s = Solution()
    print(s.shortestToChar(S, C))