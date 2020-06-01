#-*- coding: utf8 -*-

import re
import collections

# 1. 统计单词出现次数
# 2. 以列表的形式 返回其中 出现次数最多的三个单词
# 3. 三者按照出现次数 降序排序。【次数相同，对单词按照字典序降序排序】


# 统计单词出现次数
def train(features):
    # 生成值为1的空字典
    model = collections.defaultdict(int)
    for f in features:
        model[f] += 1
    return model


def fun5():
    text = input("输入字符串: ")  # 例: i love python
    print(text)
    freq = train(text.split())

    # 遍历 freq
    print("\n打印字典: ")
    for key, value in freq.items():
        print(key, value)

    print("\n打印排序后结果:")
    # 按value排序(降序)，如果value相同则按key排序(字典序升序)
    freq = sorted(freq.items(), key=lambda x:(x[1], x[0]), reverse=True)
    print(dict(freq))

    # 将单词添加到列表
    res = []
    for key in freq[:3]:
        res.append(key[0])

    # 输出 自动
    print(res)


def main():
    fun5()


if __name__ == "__main__":
    fun5()


