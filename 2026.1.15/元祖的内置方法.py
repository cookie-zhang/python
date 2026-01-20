# 元祖的定义
# 变量名字 = (元素1, 元素2, 元素3, ...)
# 强调：元祖的定义方式：一个元素的元祖定义时，要在元素后面加一个逗号
num_tuple = (1,)
print(num_tuple) # 打印元祖 (1,)
print(type(num_tuple)) # 打印元祖类型 <class 'tuple'>
# 元祖的元素不能修改
# 元祖的元素可以重复
# 元祖的元素可以嵌套
# 元祖的元素可以为任意类型

# 1. 强制类型转换
print(tuple([1, 2, 3, 4, 5])) # 打印元祖 (1, 2, 3, 4, 5)
print(tuple('hello')) # 打印元祖 ('h', 'e', 'l', 'l', 'o')
print(tuple({'name': 'dream', 'age': 20})) # 打印元祖 ('name', 'age')

# 2. 索引取值 但是不能修改
num_tuple = (1, 2, 3, 4, 5)
print(num_tuple[0]) # 打印元祖的第一个元素 1
print(num_tuple[-1]) # 打印元祖的最后一个元素 1
print(num_tuple[1:3]) # 打印元祖的第二个到第三个元素 (2, 3)
print(num_tuple[:3]) # 打印元祖的前三个元素 (1, 2, 3)
print(num_tuple[3:]) # 打印元祖的第四个到最后一个元素 (4, 5)
print(num_tuple[:]) # 打印元祖的所有元素 (1, 2, 3, 4, 5)

# 3. 切片取值 但是不能修改
num_tuple = (1, 2, 3, 4, 5)
print(num_tuple[::2]) # 打印元祖的每隔一个元素 (1, 3, 5)
print(num_tuple[1::2]) # 打印元祖的第二个到最后一个元素的每隔一个元素 (2, 4)

# 4. 计算长度
print(len(num_tuple)) # 打印元祖的长度 5


# 5 成员运算 in 和 not in


# 6. 遍历元祖
for i in num_tuple:
    print(i) # 打印元祖的每个元素 1 2 3 4 5

# 7. 元祖拼接
num_tuple = (1, 2, 3, 4, 5)
print(num_tuple + (6, 7, 8, 9, 10)) # 打印元祖 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num_tuple * 2) # 打印元祖 (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(num_tuple.__add__((6, 7, 8, 9, 10))) # 打印元祖 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num_tuple.__mul__(2)) # 打印元祖 (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 8. 元祖拆包
num_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = num_tuple
print(a) # 打印元祖的第一个元素 1
print(b) # 打印元祖的第二个元素 2
print(c) # 打印元祖的第三个元素 3
print(d) # 打印元祖的第四个元素 4
print(e) # 打印元祖的第五个元素 5