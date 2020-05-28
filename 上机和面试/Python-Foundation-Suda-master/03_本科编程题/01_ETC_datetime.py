# 车数, 进出最多，累计停留
import os
import datetime

def staytime(etc_info):
    # 计算停留时间
    # 2016-06-11#21:48:50 时间格式
    in_time = datetime.datetime.strptime(etc_info[1], "%Y-%m-%d#%H:%M:%S")
    out_time = datetime.datetime.strptime(etc_info[2].strip(), "%Y-%m-%d#%H:%M:%S")
    delta = out_time - in_time
    return delta.seconds
    
def get_record(filename):
    # os.chdir('Suda')
    with open(filename, 'r') as f:
        vehicle_lst = f.readlines()
        return vehicle_lst

def get_v(vehicle_lst):
    vehicle_set = set()
    for vehicle in vehicle_lst:
        vehicle_set.add(vehicle.split('|')[0])
    return vehicle_set


def count_v(vehicle_lst, vehicle_set):
    fre_dict = {}
    # fre_dict.fromkeys(vehicle_set)
    for vehicle in vehicle_lst:
        info = vehicle.split('|')
        fre_dict[info[0]] = fre_dict.get(info[0], 0) + 1
    return fre_dict


def count_t(vehicle_lst, vehicle_set):
    inter_dict = {}
    for etc in vehicle_lst:
        etc_info = etc.split('|')
        inter_dict[etc_info[0]] = inter_dict.get(etc_info[0], 0) + staytime(etc_info)
    return inter_dict

def write_to_file(vehicle_lst, fre_dict, inter_dict, filename):
    fre_list = sorted(fre_dict, key=lambda x: fre_dict[x], reverse=True)
    inter_list = sorted(inter_dict, key=lambda x: inter_dict[x], reverse=True)
    etc_sum = len(vehicle_lst)
    vehicle_sum = len(fre_dict)
    
    output = "记录条数：{0}\n车辆数：{1}\n进校次数最多的5辆车（单位：次）：\n".format(etc_sum, vehicle_sum)
    for i in range(5):
        output += fre_list[i] + '，' + str(fre_dict[fre_list[i]]) + '\n'

    output += '累计停留时间最长的5辆车（单位：秒）：\n'
    for i in range(5):
        output += inter_list[i] + '，' + str(inter_dict[inter_list[i]]) + '\n'

    # print(output)
    f = open(filename, 'w+')
    f.write(output)
    f.close()

def main():
    vehicle_lst = get_record("01data.txt")			# 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)				# 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)		# 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)		# 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "01report.txt")	# 输出结果到文件中
    return


main()