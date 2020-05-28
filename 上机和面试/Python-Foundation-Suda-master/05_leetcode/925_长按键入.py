"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # 双指针 44ms  42.57%
        index_t = 0
        for index, ch in enumerate(name):
            if index_t >= len(typed) or typed[index_t] != ch:
                # 输入已比对完 或字符不匹配
                return False
            elif index+1 < len(name) and name[index+1] == ch:
                # 名字中有连续字符
                index_t += 1
            else:
                # index_t 字符与 ch一致且ch不连续
                while index_t < len(typed) and typed[index_t] == ch:
                    index_t += 1
        else:
            # name部分已经被打出
            if index_t < len(typed):
                # typed结尾有不同的字符
                return False

        return True


    def isLongPressedName2(self, name, typed):
        # 按块分组
        import itertools
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        print(g1)
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))





if __name__ == "__main__":
    name, typed = "saeed", "ssaaedd"
    # name, typed = "saeed", "ssaaeedd"
    s = Solution()
    print(s.isLongPressedName2(name, typed))
    