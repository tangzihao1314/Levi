"""
导入
"""
# 导入方式 1：选择文件夹右键 mark import 模块
# 使用：模块名.成员
# 本质：创建一个变量模块地址
# 适用性：面向过程的函数，全局变量
"""import module01
module01.fun()
module01.Myclass.fun03()
c01 = module01.Myclass()"""


# 导入方式 2：from 模块 import 成员
# 使用：直接使用成员
# 本质：将其他模块成员导入到当前作用域中
# 特别如果该文件中需要用到的函数与模块中的函数重合，则该文件里面的函数会将其覆盖
# 适用性：面向对象的类
"""from module01 import Myclass
from module01 import fun
c01 = Myclass()
"""

# 导入方式 3:
# 使用：可以使用模块中所有成员
# 本质：将其他成员导入到当前作用域
# 适用性：当模块中方法过多时
"""from module01 import *
from module01 import fun
c01 = Myclass()
"""

