
"""
牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。
在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。
牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
"""

def method1():
    import sys
    import bisect
    lines = sys.stdin.readlines()       # 一次性读取所有输入
    n, m = map(int, lines[0].strip().split())
    task = {}                           # 字典 工作难度为key  报酬为value 目的：确定每种难度工作的最高value
    for line in lines[1:-1]:            # 从第二行到最后一行
        if not line.strip().split():    # 无工作或无员工
            continue
        a, b = map(int, line.strip().split())
        task[a] = max(task.get(a, 0), b)
    arr = sorted(task.keys())           # 对 字典的key列表 进行排序(工作难度)
    for i in range(1, len(task)):       # 难度高的报酬 不如 难度低的 则 更新 高的报酬 为 难度低的
        if task[arr[i]] < task[arr[i - 1]]:
            task[arr[i]] = task[arr[i - 1]]
    skills = map(int, lines[-1].strip().split())    # 获取求职者的技能数 列表
    for skill in skills:
        if skill in task:               # 对应能力的最高报酬
            print(task[skill])
        else:                           # 没有对应的能力数
            ind = bisect.bisect(arr, skill)     # 求得skill在arr中的插入位置
            if ind == 0:                # 能力小于所有工作难度
                print(0)
            else:                       # 求得插入位置前的一个工作的最高报酬
                print(task[arr[ind - 1]])


def method2():
    D = []  # 工作的难度
    P = []  # 每个工作的报酬
    M = []  # 伙伴能力值
    W = []

    n = int(input().split()[0])  # N,M

    # 添加工作
    for i in range(n):
        temp = input().split()
        D.append(int(temp[0]))
        P.append(int(temp[1]))

    # print(D, P)

    # 增加成员
    Mstrlist = input().split()
    M = [int(m) for m in Mstrlist]
    # print(M)

    for m in M:
        tempmax = 0
        i = 0
        # 找出能力范围内最高的工资
        for d in D:
            if d <= m:
                tempmax = P[i] if tempmax < P[i] else tempmax
            i += 1
        W.append(tempmax)

    for pay in W:
        print(pay)

