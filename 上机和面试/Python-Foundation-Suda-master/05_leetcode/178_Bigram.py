"""
给出第一个词 first 和第二个词 second，

考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，

其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

"""
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        third = []
        text_list = text.split()
        if len(text_list) > 2:
            for index in range(len(text_list)-2):
                if text_list[index:index+2] == [first,second]:
                    third.append(text_list[index+2])
        return third
    
    def findOcurrences2(self, text: str, first: str, second: str) -> list:
        import re
        return re.findall(fr"(?<=\b{first} {second} )(\w+)", text)



if __name__ == "__main__":
    s = Solution()
    text = "alice is a good girl she is a good student"
    first, second = "a", "good"
    print(s.findOcurrences(text, first, second))