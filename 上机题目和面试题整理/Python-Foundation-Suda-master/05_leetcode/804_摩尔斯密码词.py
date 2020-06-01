"""
国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 
比如: "a" 对应 ".-", "b" 对应 "-...", "c" 对应 "-.-.", 等等。

为了方便，所有26个英文字母对应摩尔斯密码表如下：
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。
例如，"cab" 可以写成 "-.-..--..."，(即 "-.-." + "-..." + ".-"字符串的结合)。

我们将这样一个连接过程称作单词翻译。返回我们可以获得所有词不同单词翻译的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-morse-code-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        # 52ms
        global trans
        code_set = set()
        for word in words:
            code = []
            for ch in word:
                code.append(trans[ord(ch) - 97])
            code_set.add(''.join(code))
        return len(code_set)

    def uniqueMorseRepresentations2(self, word):
        # 44ms
        global trans
        seen = {"".join(trans[ord(c) - ord('a')] for c in word)
                for word in words}  # 集合生成式
        return len(seen)


if __name__ == "__main__":
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(s.uniqueMorseRepresentations(words))