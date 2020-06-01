import datetime

def anyd():
    # x年x月x日是星期几
    # 方法1
    anyday = datetime.datetime(2019,7,17).weekday()+1
    print(anyday)
    # 方法2
    anyday = int(datetime.datetime(2020,2,26).strftime("%w"))
    print(anyday)


def disx():
    today = datetime.date.today()
    d = int(input())
    newday = today + datetime.timedelta(days=d)
    print(newday.weekday()+1)

if __name__ == "__main__":
    disx()