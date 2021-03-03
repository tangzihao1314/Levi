"""
定义函数，正确返回成绩（0-100）
"""


def get_score():
    while True:
        try:
            value = int(input("输入成绩："))
        except:
            print("输入有误，请检测后重新输入")
            continue
        if 100 > value > 0:
            print(value)
            break
        else:
            print("超出范围，请重新输入")
get_score()