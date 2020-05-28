# -*- coding: utf-8 -*-

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        allLineLens = [len(line.strip()) for line in f]
        longest = max(allLineLens)
        print(longest)
        
def main():
    readFile('./file/file07_longest.txt')
    
    
main()