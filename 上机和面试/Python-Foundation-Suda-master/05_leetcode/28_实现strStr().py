""" 
实现 strStr() 函数。  strstr(str1,str2) 函数用于判断字符串str2是否是str1的子串。

给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # python直接实现  24ms 99.34%
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        # 暴力比对 44ms 55.74%
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        else:
            return -1

    def strStr3(self, haystack: str, needle: str) -> int:
        # Rabin Karp有一种最坏时间复杂度也为 O(N) 的算法。
        # 思路是这样的，先生成窗口内子串的哈希码，然后再跟 needle 字符串的哈希码做比较。
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31
        
        # lambda-function to convert character to integer
        h_to_int = lambda i : ord(haystack[i]) - ord('a')
        needle_to_int = lambda i : ord(needle[i]) - ord('a')
        
        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0
              
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1


if __name__ == "__main__":
    S = Solution()
    haystack = "hello"
    needle = "ll"
    print(S.strStr2(haystack, needle))
