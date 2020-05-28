# -*- coding: utf-8 -*-

import pickle
import struct


# pickle 写文件
def pickle_file(url):
    with open(url, 'wb') as f:
        pickle.dump([1,2,3], f)
        pickle.dump('python', f)
        pickle.dump(3.14, f)
        pickle.dump({'the':3, 'what':5}, f)
        
def read_file(url):   
    with open(url, 'rb') as f:
        a = pickle.load(f)
        b = pickle.load(f)
        c = pickle.load(f)
        d = pickle.load(f)
        print(type(a), a)
        print(type(b), b)
        print(type(c), c)
        print(type(d), d)
   
# struct
def write_file_struct(url):
    with open(url, 'wb') as f:
        i = 13000000
        a = 99.056
        b = True
        s = '中国人民 123abc'
        data = struct.pack('if?', i, a, b)
        f.write(data)
        f.write(s.encode())


def read_file_struct(url):
    with open(url, 'rb') as f:
        data = f.read(9)
        elem = struct.unpack('if?', data)
        print(elem)     
        s = f.read(19)
        print(s.decode())
        
            
def main():
    url = './file/py01_pickle.txt'
    pickle_file(url)
    read_file(url)
    
    write_file_struct(url)
    read_file_struct(url)
                

main()
















