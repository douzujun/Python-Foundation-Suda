# -*- coding: utf-8 -*-


def main():
    words = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi',
         'ba', 'jiu']
    n = input()
    num = list(map(int, n))
    s = sum(num)
    nums = list(map(int, list(str(s))))
    
    res= []
    for e in nums:
        res.append(str(words[e]))
    
    print(' '.join(res))

main()