"""
判断一个整数是否是回文数。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # 字符串法分析
        x_str = str(x)
        rts_x = ''.join(reversed(x_str))
        
        if x_str != rts_x:
            return False
        elif len(x_str) > 1 and rts_x[0] == 0:
            # 数字长度大于1 且个位为0
            return False
        else: 
            return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(10))