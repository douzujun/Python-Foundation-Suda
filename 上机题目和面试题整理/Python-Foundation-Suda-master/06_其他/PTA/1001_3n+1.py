"""
对任何一个正整数 n，如果它是偶数，那么把它砍掉一半；
如果它是奇数，那么把 (3n+1) 砍掉一半。
这样一直反复砍下去，最后一定在某一步得到 n=1。

而是对给定的任一不超过 1000 的正整数 n，简单地数一下，
需要多少步（砍几下）才能得到 n=1？
输入样例
3
输出样例
3
"""

def count_step(n:int):
    step = 0
    while n!=1:
        if n%2 == 0:
            n = n//2
        else:
            n = (3*n +1)//2
        step += 1
    return step

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            print(count_step(n))
        except:
            break