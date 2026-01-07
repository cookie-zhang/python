# PEP8 规范
# print("Hello, World!"*5)
# print(1+ 'hello') # 报错 not int

# 字符串的格式化输出语法
# 方式一：%s 字符串  这个可以兼容所有的类型，其他的只能对应一种类型
# %d 整数  只能对应整数
# %f 浮点数  只能对应浮点数
# %c 字符  只能对应字符
# %o 八进制  只能对应八进制
# %x 十六进制  只能对应十六进制
# %e 科学计数法  只能对应科学计数法
# %g 自动选择 %f 或 %e  只能对应浮点数或科学计数法
sentence = "I am a student，my name is %s，I am %d years old"
print(sentence % ('John', 20))

# 方式二：format格式化输出
sentence = "I am a student，my name is {}，I am {} years old"
print(sentence.format('John', 20))
# key的形式
sentence = "I am a student，my name is {name}，I am {age} years old"
print(sentence.format(name='John', age=20))
# 也可以使用索引
sentence = "I am a student，my name is {0}，I am {1} years old"
print(sentence.format('John', 20))
# 也可以使用关键字参数
sentence = "I am a student，my name is {name}，I am {age} years old"
print(sentence.format(name='John', age=20))
# 也可以使用关键字参数
sentence = "I am a student，my name is {name}，I am {age} years old"
print(sentence.format(name='John', age=20))
# 方式三：f-string格式化输出
name = 'John'
age = 20
sentence = f"I am a student，my name is {name}，I am {age} years old"
print(sentence)



# ⼀、⼋⼤基本数据类型回顾 00:03
# 1. 学习变量的⽬的 00:08
#  核⼼作⽤：在程序运⾏过程中保存数据供后续代码使⽤
#  实现⽅式：通过变量名与内存地址绑定来存储数据
# 2. 学习基本数据类型⽬的 00:29
# 
#  基础地位：是Python程序最基本的组成部分
#  操作依据：不同类型对应不同操作⽅法，实现不同效果
#  分类体系：共7类8种数据类型构成完整体系
# 3. ⼋⼤基本数据类型 01:00
# 1）数字类型 02:32
#  整数类型 02:35
# o
# o 语法格式：变量名 = 整数值，如age = 18
# o 类型验证：print(type(age))输出<class 'int'>
# o 主要功能：进⾏算术运算（加减乘除等）
# o 特殊现象：整数与浮点数运算时精度会发⽣变化
#  浮点数类型 03:23
# o
# o 语法格式：变量名 = ⼩数值，如salary = 100.23
# o 类型验证：print(type(salary))输出<class 'float'>
# o 核⼼优势：⽐整数更精确表示数据
# o 运算特性：⽀持所有算术运算，但会损失⼀定精度
# 2）字符串类型 05:21
# 
#  定义⽅式：
# o 单引号包裹：'text'
# o 双引号包裹："text"
# o 三引号包裹："""text"""或'''text'''
#  索引特性：
# o 正向索引：从0开始从左向右
# o 反向索引：从-1开始从右向左
#  运算规则：
# o 字符串相加：⾸尾拼接
# o 字符串乘整数：重复出现指定次数
# o
#  格式化⽅法：
# o 百分号占位：
#  %s：任意⽂本（默认）
#  %d：整数
#  %f：浮点数
#  %x：⼗六进制数
# o format⽅法：
#  位置传参："{}".format(value)
#  关键字传参："{name}".format(name=value)
# o f-string：

#  特点：直接嵌⼊变量，可读性⾼
# 3）列表类型 12:37
# 
#  语法结构：变量名 = [元素1, 元素2, ...]
#  存储特点：可存储多个同类型或不同类型数据
#  索引规则：
# o 与字符串相同，⽀持正反向索引
# o 嵌套取值时需明确每层索引路径
#  应⽤场景：解决需要存储和操作多个相关数据的场景
# 4）字典类型 15:05
# 
#  语法格式：{key: value}键值对形式
#  键值规范：
# o key：建议使⽤字符串或数字类型
# o value：可以是任意数据类型
#  取值⽅式：
# o 中括号取值：dict[key]（键不存在时报错）
# o get⽅法：dict.get(key)（键不存在返回None）
#  设计⽬的：为数据添加描述性信息，提⾼可读性
#  嵌套示例：{"name":"dream","age":18}
# ⼆、知识⼩结
# 知识点 核⼼内容 考试重点/易
# 混淆点
# 难度系数
# 变量概念 程序运⾏过程中保存数据供后续代码
# 使⽤
# 变量与数据类
# 型的区别
# ⭐
# 基本数据类型 程序最基本的组成部分，最重要的变
# 量类型
# 七类⼋种的分
# 类⽅式
# ⭐⭐
# 数字类型 包括整数类型(int)和浮点数类型(float) 整数与浮点数
# 混合运算的精
# 度问题
# ⭐⭐
# 字符串类型 表示⽂本信息，四种定义语法(单/双/
# 三引号)
# 索引取值的正
# 向/反向规则
# ⭐⭐
# 字符串运算 ⽀持拼接(+)和重复(*)操作 与其他数据类
# 型的运算限制
# ⭐⭐
# 字符串格式化 三种⽅式：百分号占位/format⽅法/f-
# string
# %s/%d/%f的
# 区别应⽤
# ⭐⭐⭐
# 列表类型 存储多个相同/不同类型元素，中括号
# 语法
# 多层嵌套时的
# 索引取值⽅法
# ⭐⭐
# 字典类型 键值对存储⽅式，⼤括号语法 中括号取值与
# get()⽅法的区
# 别
# ⭐⭐⭐
# 数据类型分类 ⼋⼤基本数据类型：
# int/float/str/list/dict/tuple/bool/set
# 七类⼋种的具