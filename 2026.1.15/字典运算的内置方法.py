#  键值对 键：值 

dict = {'name': 'dream', 'age': 20}
# 取值
print(dict['name']) # 打印字典的name键的值 dream
print(dict['age']) # 打印字典的age键的值 20
print(dict.get('name')) # 打印字典的name键的值 dream
print(dict.get('age')) # 打印字典的age键的值 20
print(dict.get('gender')) # 打印字典的gender键的值 None

# 修改
dict['name'] = 'dream2'
print(dict) # 打印字典 {'name': 'dream2', 'age': 20}

# 添加
dict['gender'] = 'male'
print(dict) # 打印字典 {'name': 'dream2', 'age': 20, 'gender': 'male'}

# 删除 
dict.pop('gender')
print(dict) # 打印字典 {'name': 'dream2', 'age': 20}

# 清空
dict.clear()
print(dict) # 打印字典 {}

# 删除字典 按照键删除
del dict['name']
print(dict) # 打印字典 {}