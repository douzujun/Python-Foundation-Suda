"""
0,1,...,n-1这n个数字排成一个圆圈，从数字0开始，
每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，
从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        num_list = [i for i in range(n)]
        current = 0
        while len(num_list) > 1:
            current = (current + m - 1) % len(num_list)
            del num_list[current]
            # num_list.pop(current)
        return num_list[0]
    
    def lastRemaining2(self, n: int, m: int) -> int:
        """
        我们知道，从 f(n - m) 场景下删除的第一个数的序号是 (m - 1) % n，
        那么 f(n - 1, m) 场景将使用被删除数字的下一个数，即序号 m % n 作为它的 0 序号。

        设 f(n - 1, m) 的结果为 x，x 是从 f(n, m) 场景下序号为 m % n 的数字出发所获得的结果，
        因此，我们可以得出：m % n + x 是该数字在 f (n, m) 场景下的结果序号。即：

        f(n, m) = m % n + x
        但由于 m % n + x 可能会超过 n 的范围，所以我们再取一次模：

        f(n , m) = (m % n + x) % n = (m + x) % n
        将 f(n - 1, m) 代回，得到递推公式：

        f(n, m) = (m + f(n - 1, m)) % n
        有了递推公式后，想递归就递归，想迭代就迭代咯~
        """
        return self.f(n, m)

    def f(self, n, m):
        if n == 0:
            return 0
        x = self.f(n - 1, m)
        return (m + x) % n


if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining(5, 3))
    print(s.lastRemaining(10, 17))
