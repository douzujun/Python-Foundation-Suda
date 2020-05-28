"""
给定仅有小写字母组成的字符串数组 A，

返回列表中的每个字符串中都显示的 全部字符（包括重复字符）组成的列表。

???
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，

则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def commonChars(self, A: list) -> list:
        result = []
        ch_dict = {}
        for ch in A[0]:
            ch_dict[ch] = ch_dict.get(ch, 0) + 1

        for s in A:
            del_key = []
            for key, value in ch_dict.items():
                k_num = s.count(key)
                if 0< k_num < value:
                    ch_dict[key] = k_num
                elif k_num == 0:
                    del_key.append(key)
            for key in del_key:
                ch_dict.pop(key)
        
        for k, v in ch_dict.items():
            result.extend([k] * v)

        return result

    def commonChars2(self, A: list) -> list:
        result = []
        for w in set(A[0]):
            # 计算w字符在整个A中的出现次数
            count = [s.count(w) for s in A]
            result.extend([w]*min(count))

        return result

if __name__ == "__main__":
    test = ["bella","label","roller"]
    s = Solution()
    print(s.commonChars(test))