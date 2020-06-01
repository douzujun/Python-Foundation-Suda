# -*- coding: utf-8 -*-

import re

def solve():
    # one two::three,FOUR..,five
    words = input() # 'hello!world,Computer.class,54,5w'
    wli = re.split('[^a-zA-Z0-9]', words)
    
    ans = []
    for word in wli:
        if word:
           if len(word) <= 5:
               ans.append(word)
           else:
               word = word[0]+'*'*len(word[1:-1])+word[-1]
               ans.append(word)
        
    print(' '.join(ans))

solve()
