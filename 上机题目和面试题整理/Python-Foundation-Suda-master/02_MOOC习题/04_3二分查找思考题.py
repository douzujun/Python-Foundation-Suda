def perfect_square():
    # n是完全平方数，用二分查找计算n的平方根
    n = int(input())
    left, right = 1, n//2+1
    while left<=right:
        mid = (left+right) // 2
        temp = mid**2
        if temp == n:
            print(mid)
            return
        elif temp > n:
            right = mid - 1
        else:
            left = mid + 1
    print("不存在")
    return

def count_sqrt2():
    # 用二分查找计算2的平方根
    left, right = 1,2
    while left<=right:
        mid = (left+right)/2
        temp = mid**2
        if abs(temp-2) < 1e-10:
            print(mid)
            return
        elif temp > 2:
            right = mid
        else:
            left = mid
    return 


if __name__ == "__main__":
    while True:
        try:
            perfect_square()
        except:
            break
    
    count_sqrt2()