# -*- coding: utf-8 -*-

# 现有一个文本文件data.txt，其中记录了车辆进出校园时在自动收费系统ETC中记录下的ETC编号和时间信息。
# 每个ETC编号唯一地对应于一辆机动车。试用python语言编写程序，按要求从该数据文件中提取所需的信息。
#
# 说明：
# 1. 一个ETC编号由5部分构成，本别是：两个大写字母、一个短横线、三位数字、一个短横线、三位数字。
#    如：“FG-102-934”、“BA-724-433”等都是合法的ETC编号。
# 2. 时间信息的记录格式为：2016-01-08#07:21:31。
# 3. 整条ETC记录的格式由5部分构成，分别是：ETC编号、字符“|”、入校时间、字符“|”，离校时间。
#    如：“BA-724-433|2016-01-08#07:21:31|2016-01-08#17:01:09”就是一条结构完整的ETC记录。
# 4. 数据文件中每一行为一个ETC记录。
# 5. 车辆进入校园后都是在当天离开校园的，即每条ETC记录中出入校园的日期是相同的。
# 6. ETC记录中出现的字符都是英文符号，无汉字和中文标点符号。
#
# 要求：
# 1. 从文件中识别ETC记录，计算总的ETC记录的条数。提示：读取文件，并将ETC记录放入列表中。
# 2. 计算ETC记录中共有多少辆不同的车。提示：通过正则表达式（或字符串分片）识别每条ETC记录中的ETC编号，
#    并将ETC编号放入集合中。
# 3. 找出进出校园次数最多的5辆车。提示：构建ETC编号和出现次数的字典。
# 4. 找出在校园中累计停留时间最长的5辆车。提示：构建ETC编号和累计停留时间的字典。
#    可通过正则表达式（或字符串分片）识别时间字符串及其中的时、分、秒信息。
#    为简化计算，可将时间转化成以零点开始计算的秒数。可以把计算时间差作为一个独立的函数。
#5.	 将上述计算结果按“report.txt文件内容示例”（见最后一页）所示的要求输出到report.txt文件中。

import re

# 读文件，获取全部ETC记录，构成列表
def get_record(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        data = data.split('\n')
    return data[:-1]
 
# 获取全部不同的ETC编号，构成集合
def get_v(vehicle_lst): 
    veh_set = set()
    for elem in vehicle_lst:
        veh = elem.split('|')[0]
        veh_set.add(veh)

    # 共有多少辆不同的车
#    print(len(veh_set))
    return veh_set

# 构造车辆进出校园次数的字典  
def count_v(vehicle_lst, vehicle_set):
    vehicles = {}
    for elem in vehicle_lst:
        veh = elem.split('|')[0]
        vehicles[veh] = vehicles.get(veh, 0) + 1      # 遇到一次编码, 次数+1, 默认为0
    vehicles = sorted(vehicles.items(), key=lambda x:(x[1]), reverse=True)[:10]
    
    # 进出校园次数最多的5辆车
    print(vehicles[:5])
    return vehicles[:5]


# 问题4: 
# 时间 转化成 秒
def time2int(time : str):
    time = time.split(':')
    hour = int(time[0])*3600
    minu = int(time[1])*60
    sec = int(time[2])
    return hour + minu + sec

# 计算时间差
def calcTimeDiff(start, end):
    return int(time2int(end) - time2int(start))

# 得到秒后，再 转化成 时间
def sec2time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{0}:{1:02d}:{2:02d}".format(h, m, s)
    
# 构造车辆累计停留时间的字典
def count_t(vehicle_lst, vehicle_set):
    vehicles = {}
    for elem in vehicle_lst:
        veh = elem.split('|')[0]
        time = re.findall('[0-9]+:[0-9]+:[0-9]+', elem)
        diff = calcTimeDiff(time[0], time[1])
        vehicles[veh] = vehicles.get(veh, 0) + diff   # 累加停留的所有时间
    
    vehicles = sorted(vehicles.items(), key=lambda x:(x[1]), reverse=True)
    # 如果要把 秒 转化成 时:分:秒
#    vehicles = [(elem[0], sec2time(elem[1])) for elem in vehicles]

    # 累计停留时间最长的5辆车
    print(vehicles[:5])      
    return vehicles[:5]
        

# vehicle_lst: 总的ETC记录的条数
# fre_dict: 进出校园次数最多的5辆车
# inter_dict: 进出校园次数最多的5辆车
def write_to_file(vehicle_lst, fre_dict, inter_dict, url):
    with open(url, 'w+', encoding='utf8') as f:
        # 总的 ETC记录的 条数
        f.write("记录条数: " + str(len(vehicle_lst)) + '\n')
        # 共有多少辆不同的车
        f.write("车辆数: " + str(len(get_v(vehicle_lst))) + '\n')
        # 进出校园次数最多的5辆车
        f.write("进校次数最多的5辆车（单位：次）\n")
        for elem in fre_dict:
            f.write("{0}, {1}\n".format(str(elem[0]), str(elem[1])))
        # 在校园中累计停留时间最长的5辆车
        f.write("累计停留时间最长的5辆车（单位：秒）\n")
        for elem in inter_dict:
            f.write("{0}, {1}\n".format(str(elem[0]), str(elem[1])))
    

def main():
    vehicle_lst = get_record("./file/file_2019_input.txt")			                # 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)				                                # 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)	            	                # 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)		                            # 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "./file/file_2019_report.txt")	# 输出结果到文件中
    return


main()	# 调用main函数






























