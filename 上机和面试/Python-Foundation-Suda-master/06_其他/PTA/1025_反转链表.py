"""
给定一个常数 K 以及一个单链表 L，请编写程序将 L 中每 K 个结点反转。
例如：给定 L 为 1→2→3→4→5→6，K 为 3，则输出应该为 3→2→1→6→5→4；
如果 K 为 4，则输出应该为 4→3→2→1→5→6，即最后不到 K 个元素不反转。

第一行  结点1地址 结点总个数  反转的子链个数

两个测试点报错
"""




if __name__ == "__main__":
    firstadd, total, relength = map(int, input().split())
    
    # 生成链表
    d = dict()
    for i in range(total):
        add, data, next = map(int, input().split())
        d[add] = [data, next]

    # 反转
    d[-2] = [0, firstadd]   # 假头
    current, privchain = firstadd, -2
    priv = -2
    for _ in range(int(total//relength)):
        for _ in range(relength):
            next = d[current][1]
            d[current][1] = priv
            priv = current
            current = next
        temp = d[privchain][1]
        d[temp][1] = current
        d[privchain][1] = priv
        privchain = priv = temp

    # 输出
    next = d[-2][1]
    while next!=-1:
        if d[next][1] != -1:
            print('{0:05} {1[0]} {1[1]:05}'.format(next, d[next]))
        else:
            print('{0:05} {1[0]} {1[1]}'.format(next, d[next]))
        next = d[next][1]