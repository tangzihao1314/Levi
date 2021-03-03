"""
包
在day01中创建两个包，然后在每个包中创建一个m0x的文件
在每个文件中创建一个函数，然后调用

导入是否成功的条件：
系统路径（sys.path）+ 导入路径 == 真实路径
"""
# 导入方式 1 :import 路径.模块名 as 别名
# 使用：别名.成员
"""import package01.m01 as m
# import package01.package02.m02 as m2
# m2.fun02()
m.fun01()"""

# 导入方式 2 ： from 路径.模块名 import 成员
"""from package01.package02.m02 import fun02

fun02()"""

# 导入方式 3 ： from 路径.模块名 import *
# 直接使用成员
from package01.package02.m02 import *

fun02()
