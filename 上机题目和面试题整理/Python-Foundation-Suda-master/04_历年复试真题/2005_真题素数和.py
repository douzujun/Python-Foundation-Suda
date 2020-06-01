# 将一个数拆分成多个素数之和
import math

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

def find_primes(n):
    prime_list = [i for i in range(n,1,-1) if is_prime(i)] # 生成0~n的所有素数

    def DFS(n, index, sum, prime_list, current=[]):
        """
        n: 求解的数， index：下一个要判断的在prime_list中的索引
        sum：当前的和  prime_list: 0~n的素数列表  current：当前的求解组合
        """
        if sum > n or index >= len(prime_list):
            return False
        if sum == n:
            print(current)
            return True
        else:
            current.append(prime_list[index])
            if DFS(n, index+1, sum+prime_list[index], prime_list, current):
                return True
            else:
                current.pop()
                return DFS(n, index+1, sum, prime_list, current)

    DFS(n, 0, 0, prime_list)
        
if __name__ == "__main__":
    find_primes(int(input()))


"""
def equal_prime(n):
    '''n拆分成素数之和'''
    plist = [i for i in range(n + 1) if is_prime(i)] # 0~n的所有素数
    DFS(n, 0, 0, plist, S=set())
    
def DFS(n, index=0, sum=0, primes=[], L=[], S=set()):
    # 当前的和已经超过目标素数
    if (sum > n):
        return
    # sum==n 找到了这样的一组数字
    if index < len(primes):
        # 未遍历完素数列表
        if (sum == n):
            if (tuple(L) not in S): # 避免重复输出 S 储存结果
                print(L)
                S.add(tuple(L))
        L.append(primes[index])
        DFS(n, index + 1, sum + primes[index], primes, L, S)
        L.pop()
        DFS(n, index + 1, sum, primes, L, S)

"""