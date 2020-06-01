import time

def my_max(L):
    # 计算列表中的最大值
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], my_max(L[1:]))


# 递归实现斐波那契
def fibonacci(n):
    # F0 = 1 F1=1 Fn = Fn-1 + Fn-2
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 改进版  一次返回两个值Fn Fn-1 避免重复计算
def fibonacci2(n):
    if n<=1:
        return (1,1)
    else:
        (a, b) = fibonacci2(n-1)
        return (a+b, a)

if __name__ == "__main__":
    n = int(input())
    start = time.perf_counter()
    print(fibonacci(n))
    print("use:",time.perf_counter()-start)

    start = time.perf_counter()
    print(fibonacci2(n)[0])
    print("use:",time.perf_counter()-start)
