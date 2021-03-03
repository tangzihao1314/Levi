"""
模块相关概念
"""
# __all__变量：定义可导出成员，仅对from xx import *语句有效。
from skill_system import *

# s01 = SkillManager()
# s01.generate()
skill_developer.SkillManager().generate()

# __doc__变量：文档字符串。
print(skill_developer.__doc__)

# __file__变量：模块对应的文件路径名。
print(__file__)

# __name__变量：不是返回模块自身名字，而是主模块的名字，可以判断当前模块是否为主模块。
if __name__ == "main":
    print("主模块")
else:
    print("不执行")
# print(__name__)
