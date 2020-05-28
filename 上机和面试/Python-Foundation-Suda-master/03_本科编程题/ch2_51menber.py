

if __name__ == "__main__":
    menber = {}
    while True:
        try:
            name, number = input("请输入一个姓名,编号：").split(',')
            menber[number] = name
        except Exception as e:
            for num,name in menber.items():
                print(name, num)
            for num,name in menber.items():
                print(num, name)
    