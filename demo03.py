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




# 导入方式 3:
# 使用：可以使用模块中所有成员
# 本质：将其他成员导入到当前作用域
# 适用性：当模块中方法过多时
"""from module01 import *
from module01 import fun
c01 = Myclass()
"""

