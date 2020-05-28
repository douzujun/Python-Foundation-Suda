"""
给定一个Excel表格中的列名称，返回其相应的列序号。
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        # 52ms
        count = 0
        for ch in s:
            count = count*26 +  ord(ch) - 64  # ord('A') == 65
        return count
        
    

if __name__ == "__main__":
    test = "AA"
    s = Solution()
    print(s.titleToNumber(test))