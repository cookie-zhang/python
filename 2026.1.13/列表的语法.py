# 变量名 = [元素1, 元素2, 元素3, ...]
# 列表中的元素可以是任意类型
# 1. 强制类型转换 列表类型 
from typing import Literal


print(list('dream')) # 打印列表 ['d', 'r', 'e', 'a', 'm']
print(list[Literal[1, 2, 3, 4, 5]]((1,2,3,4,5))) # 打印列表 [1, 2, 3, 4, 5]
print(list({1,2,3,4,5})) # 打印列表 [1, 2, 3, 4, 5]
print(list({'name', 20})) # 打印列表 ['name', 'age']
print(list({'name': 'dream', 'age': 20})) # 字典转换为列表时，只转换字典的键 ['name', 'age']

# 四种方式对比：
# remove：按值删除单个元素
# pop：按索引弹出元素（可获取返回值）
# del：按索引删除元素（语句非方法）
# clear：清空整个列表

# 颠倒元素
list.reverse()

# 排序：
list.sort() # 默认升序
list.sort(reverse=True) # 降序
list.sort(key=lambda x: x[1]) # 按第二个元素排序
list.sort(key=lambda x: x[1], reverse=True) # 按第二个元素升序
list.sort(key=lambda x: x[1], reverse=True) # 按第二个元素降序

# sort和sorted的区别：
# sort是列表的方法，只能对列表进行排序
# sorted是内置函数，可以对任何可迭代对象进行排序
# 使用方式
sorted(list) # 返回新的列表
sorted(list, reverse=True) # 返回新的列表
sorted(list, key=lambda x: x[1]) # 返回新的列表
sorted(list, key=lambda x: x[1], reverse=True) # 返回新的列表
