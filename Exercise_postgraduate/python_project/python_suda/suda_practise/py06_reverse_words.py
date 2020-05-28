# -*- coding: utf-8 -*-

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        print(data)
    return data

def main():
    data = readFile('./file/file06_reverse.txt')
    words = data.split()
    print(" ".join(words[::-1]))
    
    
if __name__=='__main__':
    main()