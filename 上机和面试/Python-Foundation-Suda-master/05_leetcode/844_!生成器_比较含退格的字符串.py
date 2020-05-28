"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，
判断二者是否相等，并返回结果。 # 代表退格字符。
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
注意：如果对空文本输入退格字符，文本继续为空。


"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 48ms 26.26%
        S_list = []
        for ch in S:
            if ch != '#':
                S_list.append(ch)
            elif len(S_list) > 0:
                S_list.pop()
        T_list = []
        for ch in T:
            if ch != '#':
                T_list.append(ch)
            elif len(T_list) > 0:
                T_list.pop()
        if S_list == T_list:
            return True
        else:
            return False

    def backspaceCompare2(self, S: str, T: str) -> bool:
        # 48ms
        # 反向遍历 双指针
        import itertools
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

if __name__ == "__main__":
    S, T = "ab##", "c#d#"
    s = Solution()
    print(s.backspaceCompare2(S, T))
