# 集合的特点：无序、不重复、无索引
# 集合的定义：set = {元素1, 元素2, 元素3, ...}

# 强制转换
# 可以讲起他的类型转换为 集合

print(set([1, 2, 3, 4, 5])) # 打印集合 {1, 2, 3, 4, 5}
print(set((1, 2, 3, 4, 5))) # 打印集合 {1, 2, 3, 4, 5}
print(set({'name': 'dream', 'age': 20})) # 打印集合 {'name', 'age'}
print(set(range(1, 10))) # 打印集合 {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set('hello')) # 打印集合 {'h', 'e', 'l', 'o'}

# 添加元素
set_num = {1, 2, 3, 4, 5}
set_num.add(6) # 添加元素6 
print(set_num) # 打印集合 {1, 2, 3, 4, 5, 6}

# 删除元素
set_num.remove(6) # 删除元素6 
print(set_num) # 打印集合 {1, 2, 3, 4, 5}

# 清空集合
set_num.clear()
print(set_num) # 打印集合 {}

# 删除集合
del set_num
print(set_num) # 打印集合 {}

# 集合的运算
set_num1 = {1, 2, 3, 4, 5}
set_num2 = {4, 5, 6, 7, 8}

# 交集
print(set_num1 & set_num2) # 打印集合 {4, 5}

# 并集
print(set_num1 | set_num2) # 打印集合 {1, 2, 3, 4, 5, 6, 7, 8}

# 差集
print(set_num1 - set_num2) # 打印集合 {1, 2, 3}
print(set_num2 - set_num1) # 打印集合 {6, 7, 8}

# 对称差集
print(set_num1 ^ set_num2) # 打印集合 {1, 2, 3, 6, 7, 8}

# 子集
print(set_num1 < set_num2) # 打印集合 False
print(set_num1 > set_num2) # 打印集合 False
