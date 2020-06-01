import math
import random

# 严格按照通项
# pi += pow(-1, i)/(2*i+1)

# 常用表示
# tm = 1
# pi += tm/(2*i+1)*i
# tm = -tm


def count_pi1(n: int):
    """
    莱布尼兹级数交错法
    pi/4 = sum(o~n) -1^n / (2n+1)

    结果确定↑
    """
    pi = 0
    tm = 1
    for i in range(n):
        pi += tm/(2*i+1)
        tm = -tm
    return pi*4


def count_pi2(n=100000):
    """
    蒙特卡洛法
    正方形内相切一个圆 随机产生点 
    计算点与中心距离是否 小于半径
    点的百分比 = 面积比  pir^2 与r^2

    每次结算都有所不同↑
    """
    inside = 0
    for _ in range(n):
        x,y = random.random(),random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    
    return inside / n *4


if __name__ == "__main__":
    for i in [10**i for i in range(1, 8)]:
        pi1 = count_pi1(i)
        print("count_pi1={},error={:.10f}".format(pi1, math.pi-pi1))
    
    sum_dif, k = 0,20
    pi2 = 0
    for i in range(k):
        pi2 += count_pi2()
        dif = abs(pi2-math.pi) / pi2
        sum_dif += dif
    sum_dif /= k
    pi2 /= k
    print("count_pi2={},error={:.10f}".format(pi2, sum_dif))
