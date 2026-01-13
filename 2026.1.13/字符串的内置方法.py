# + 拼接
print("hello" + "world")

# * 重复
print("hello" * 3)

# in 判断是否包含
print("h" in "hello")

# not in 判断是否不包含
print("h" not in "hello")

# len 计算长度
print(len("hello"))

# max 计算最大值
print(max("hello"))

# min 计算最小值
print(min("hello"))

# str 转换为字符串
print(str(123))

# int 转换为整数  
print(int("123"))

# float 转换为浮点数
print(float("123"))

# bool 转换为布尔值
print(bool("123"))

# list 转换为列表
print(list("hello"))

# tuple 转换为元组  
print(tuple("hello"))

# dict 转换为字典
print(dict(hello=123))

# set 转换为集合
print(set("hello"))

# frozenset 转换为不可变集合
print(frozenset("hello"))

# strip 去除字符串两端的空格 默认去除空格、换行符、制表符
print("  hello  ".strip())
print("$hello$".strip("$"))

# lstrip 去除字符串 左 端的空格
print("  hello  ".lstrip())

# rstrip 去除字符串 右 端的空格
print("  hello  ".rstrip())

# split 分割字符串 默认分割空格、换行符、制表符
print("hello world".split())
print("hello$world".split("$"))