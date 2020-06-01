# -*- coding: utf-8 -*-

import re

def words(text):
    return re.findall('[a-z]', text.lower())
    
def train(features):
    model = {}
#    print(features)
    for f in features:
        model[f] = model.get(f, 0) + 1
    
    return model    
    

def main():
#    t = open("./file/2005_2.txt").read()
#    print(t)
#    print(words(t))
    statistic = train(words(open("./file/2005_2.txt").read()))
    statistic = list(statistic.items())
    print(statistic)
    statistic.sort(key=lambda x:(x[1], x[0]), reverse=True)
    print(dict(statistic))
    
    

if __name__=='__main__':
    main()