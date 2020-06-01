"""
本题要求计算 A/B，其中 A 是不超过 1000 位的正整数，B 是 1 位正整数。
你需要输出商数 Q 和余数 R，使得 A=B×Q+R 成立。
"""

if __name__ == "__main__":
    A, B = map(int, input().split())
    Q = A // B
    R = A % B
    print('{} {}'.format(Q,R))