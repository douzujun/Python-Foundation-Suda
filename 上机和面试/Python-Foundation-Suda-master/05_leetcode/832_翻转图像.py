"""
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
水平翻转图片就是将图片的每一行都进行翻转，即逆序。
例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。
例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flipping-an-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        # 3 min 27 s   60ms
        for index, row in enumerate(A):
            A[index] = [0 if i==1 else 1 for i in row[::-1]]
        return A

    def flipAndInvertImage2(self, A: list) -> list:
        # 84ms
        return [[~i+2 for i in j[::-1]] for j in A]

if __name__ == "__main__":
    A = [[1,1,0],[1,0,1],[0,0,0]]
    s = Solution()
    print(s.flipAndInvertImage2(A))