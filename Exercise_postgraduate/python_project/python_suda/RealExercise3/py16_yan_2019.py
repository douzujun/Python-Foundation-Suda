# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:04:02 2020

@author: douzi
"""

import re

def get_record(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        data = data.split('\n')
        
#    print(data[:-1])
    print(len(data[:-1]))
    return data[:-1]

def get_v(vehicle_lst):
    veh_set = set()
    for veh in vehicle_lst:
        vid = veh.split('|')[0]
        veh_set.add(vid)
   
    print(len(veh_set))
    return veh_set

# 构造车辆进出校园次数的字典
def count_v(vehicle_lst, vehicle_set):
    freq = {}
    for veh in vehicle_lst:
        vid = veh.split('|')[0]
        freq[vid] = freq.get(vid, 0) + 1
    
    freq = sorted(freq.items(), key=lambda x:(x[1]), reverse=True)
    
    print(freq[:5])
    return freq[:5]
    
def calcTime(time):
    h, m, s = time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)

# 构造车辆累计停留时间的字典
def count_t(vehicle_lst, vehicle_set):
    vehs = {}
    for veh in vehicle_lst:
        vid = veh.split('|')[0]
        start, end = re.findall('[0-9]+:[0-9]+:[0-9]+', veh)
        diff = calcTime(end) - calcTime(start)
        vehs[vid] = vehs.get(vid, 0) + diff
    
    inter_dict = sorted(vehs.items(), key=lambda x:(x[1]), reverse=True)
    
    print(dict(inter_dict[:5]))
    return inter_dict[:5]

def write_to_file(vehicle_lst, fre_dict, inter_dict, url):
    with open(url, 'w', encoding='utf8') as f:
        f.write('记录条数: {0}\n'.format(len(vehicle_lst)))
        f.write('车辆数: {0}\n'.format(len(fre_dict)))
        f.write('进校次数最多的5辆车（单位：次）\n')
        for veh in fre_dict:
            f.write('{0}, {1}\n'.format(veh[0], veh[1]))
        f.write('累计停留时间最长的5辆车（单位：秒）\n')
        for veh in inter_dict:
            f.write('{0}, {1}\n'.format(veh[0], veh[1]))

def main():
    # 读文件，获取全部ETC记录，构成列表
    vehicle_lst = get_record("./file/file_2019_input.txt")  
   
    # 获取全部不同的ETC编号，构成集合
    vehicle_set = get_v(vehicle_lst)
    
    # 构造车辆进出校园次数的字典
    fre_dict = count_v(vehicle_lst, vehicle_set)    
    
    # 构造车辆累计停留时间的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)   
                
    # 输出结果到文件中
    write_to_file(vehicle_lst, fre_dict, inter_dict, "./file/file_2019_report.txt") 
   
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    