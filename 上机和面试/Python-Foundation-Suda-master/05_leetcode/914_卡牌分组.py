"""
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 48ms 75%   每个卡号重复次数存在大于2的最大公约数 True
        if not (freq_dict:=Counter(deck)):
            return False
        
        temp = min(freq_dict.values())  # 重复数量最小的号码
        if temp < 2:
            return False
        
        # 所有的数字有公约数
        for i in range(2, temp+1):
            for v in freq_dict.values():
                if v % i != 0:
                    break
            else:
                # i 为公约数
                return True
        else:
            return False


if __name__ == "__main__":
    test = [1,1,1,1,2,2,2,2,2]
    S = Solution()
    print(S.hasGroupsSizeX(test))