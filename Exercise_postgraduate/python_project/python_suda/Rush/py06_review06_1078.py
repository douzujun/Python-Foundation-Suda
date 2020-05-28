# -*-  coding: utf-8 -*-

def solve():
    # right = input().lower()
    # wrong = input().lower()
    right = '7_This_is_a_test'.lower()
    wrong = '_hs_s_a_es'.lower()

    s1, s2 = set(right), set(wrong)
    out = list(s1 - s2)

    out.sort(key=lambda x: right.index(x))
    print(''.join(out).upper())


if __name__ == "__main__":
    solve()
