"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lemonade-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        # 184ms 47% 模拟情景
        money_dict = {5:0, 10:0, 20:0}
        for bill in bills:
            money_dict[bill] += 1
            change = bill - 5
            while change > 0:
                if 10 <= change and money_dict[10] > 0:
                    change -= 10
                    money_dict[10] -= 1
                elif 5 <= change and money_dict[5] > 0:
                    change -= 5
                    money_dict[5] -= 1
                else:
                    return False
        else:
            return True



if __name__ == "__main__":
    test = [5,5,10,10,20]
    s = Solution()
    print(s.lemonadeChange2(test))