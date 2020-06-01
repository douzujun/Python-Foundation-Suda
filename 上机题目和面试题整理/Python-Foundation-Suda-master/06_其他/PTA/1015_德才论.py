"""
“是故才德全尽谓之圣人，才德兼亡谓之愚人，德胜才谓之君子，才胜德谓之小人。凡取人之术，苟不得圣人，君子而与之，与其得小人，不若得愚人。”
《资治通鉴》

现给出一批考生的德才分数，请根据司马光的理论给出录取排名。
第一行 N总数；L最低分数线；H优先录取线
考生信息: 准考证号 德分 才分

德才皆高于L才可考虑录取
1双全： 德才皆高于H 按德才总分高低排序
2德胜才： 德>H 才低于H
3才德兼亡 但德胜才 H>德>才
4其余>L

当某类考生中有多人总分相同时，按其德分降序排列；
若德分也并列，则按准考证号的升序输出。
"""



if __name__ == "__main__":
    N, L, H = map(int,input().split())
    stu_list1,stu_list2,stu_list3,stu_list4 = [],[],[],[]

    for _ in range(N):
        stu_id, d, c = map(int, input().split())
        if d >= L or c >= L:
            if d >= H and c >=H:
                stu_list1.append((stu_id, d, c)) # 双全
            elif d >= H:
                    # 德 >= H > 才
                stu_list2.append((stu_id, d, c))
            elif d >= c:
                stu_list3.append((stu_id, d, c))
            else:
                stu_list4.append((stu_id, d, c))

    print(len(stu_list1)+len(stu_list2)+len(stu_list3)+len(stu_list4))
    for stu_list in stu_list1,stu_list2,stu_list3,stu_list4:
        for stu in stu_list:
            # 总分的情况下再德分，学号排序
            stu_list.sort(key=lambda stu: (stu[1]+stu[2],stu[1],-stu[0]), reverse=True)
            print('{0[0]} {0[1]} {0[2]}'.format(stu))
