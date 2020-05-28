"""
01data.txt
ETC编号  FG-102-934
时间格式  2016-01-08#07:21:31
整条记录  BA-724-433|2016-01-08#07:21:31|2016-01-08#17:01:09
每行一个ETC
每辆车都是当天出入  日期相同

要求：
识别ETC 记录总条数
计算ETC中有多少辆不同的车  正则 or 切片
找出进出次数最多的5辆车
找出累计停留时间最长的5辆车
将计算结果输出到01report.txt
"""
import re


def get_record(filename):
    f = open(filename, 'r')
    records = f.readlines()
    f.close()
    return records


def get_v(vehicle_lst):
    # 切片法
    vehicle_set = set()
    for record in vehicle_lst:
        vehicle_set.add(record.split('|')[0])
    return vehicle_set


def get_v2(vehicle_lst):
    # 正则法
    pattern = re.compile(r"\w{2}-\d{3}-\d{3}")  # 反复使用 预先编译
    vehicle_set = set()
    for record in vehicle_lst:
        vehicle_set.add(pattern.match(record).group())
    return vehicle_set


def count_v(vehicle_lst, vehicle_set):
    fre_dict = dict.fromkeys(vehicle_set, 0)
    for record in vehicle_lst:
        fre_dict[record.split('|')[0]] += 1
    return fre_dict


def count_t(vehicle_lst, vehicle_set):
    def computtime(ent, out):
        ent = list(map(int, ent[-8::].split(":")))
        out = list(map(int, out[-8::].split(':')))
        ents = (ent[0]*60 + ent[1]) * 60 + ent[2]
        outs = (out[0]*60 + out[1]) * 60 + out[2]
        return outs - ents
    inter_dict = dict.fromkeys(vehicle_set, 0)
    for record in vehicle_lst:
        carid, enter, out = record.strip().split('|')
        inter_dict[carid] += computtime(enter, out)
    return inter_dict

def count_t2(vehicle_lst, vehicle_set):
    # 正则法
    inter_dict = dict.fromkeys(vehicle_set, 0)
    pattern = re.compile(r'#(\d{2}):(\d{2}):(\d{2})')
    for record in vehicle_lst:
        rec_sp = record.strip().split('|', 1)   # 只进行一次分隔
        ent, out = pattern.findall(rec_sp[1])
        ent = list(map(int, ent))
        out = list(map(int, out))
        ents = (ent[0]*60 + ent[1]) * 60 + ent[2]
        outs = (out[0]*60 + out[1]) * 60 + out[2]
        inter_dict[rec_sp[0]] += (outs-ents)
    return inter_dict

def write_to_file(vehicle_lst, fre_dict, inter_dict, filename):
    with open(filename, 'w') as f:
        f.write('记录条数：{}\n'.format(len(vehicle_lst)))
        f.write('车辆数：{}\n'.format(len(fre_dict)))

        f.write('进校次数最多的5辆车（单位：次）：\n')
        fre_list = sorted(
            fre_dict, key=lambda x: fre_dict[x], reverse=True)[:5]
        for car in fre_list:
            f.write('{}， {}\n'.format(car, fre_dict[car]))

        f.write('累计停留时间最长的5辆车（单位：秒）：\n')
        inter_list = sorted(
            inter_dict, key=lambda x: inter_dict[x], reverse=True)[:5]
        for car in inter_list:
            f.write('{}， {}\n'.format(car, inter_dict[car]))


def main():
    vehicle_lst = get_record("./files/01_data.txt")			# 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)				# 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)		# 构造车辆进出校园次数的字典
    inter_dict = count_t2(vehicle_lst, vehicle_set)		# 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict,
                  "./files/01_report.txt")  # 输出结果到文件中
    return


if __name__ == "__main__":
    main()
