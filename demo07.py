"""
异常处理
"""


def div_apple(apple_count):
    perspn_count = int(input("请输入人数："))
    result = apple_count / perspn_count
    print("每个人分%f个苹果" % result)


# 1.根据不同错误做出不同的处理
try:
    div_apple(10)
except ValueError:
    print("输入必须是整数")
except ZeroDivisionError:
    print("输入不能为0")
# div_apple(6)

# 2.不同的错误相同的处理逻辑

"""try:
    div_apple(10)
# except:
except Exception:
    print("出错了")"""

# 3.如果没有出错可以单独定义逻辑

"""try:
    div_apple(10)
# except:
except Exception:
    print("出错了")
else:
    print("没有出错")"""

# 4.有没有错误都要做
"""try:
    div_apple(10)

finally:
    print("无论是否出错，一定执行的逻辑")"""