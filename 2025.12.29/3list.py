# 列表
# list  tuple 
# list 有序可变列表
grades = [95, 88, 92, 77, 90]
grades[0] = 100 # 修改列表中的元素
print('grades[1:4] = ', grades[1:4]) # 切片 从1到4（不包括4）
grades[1:4] = [] # 删除列表中的元素
grades.append(100) # 添加元素
grades.insert(0, 99) # 插入元素 在0位置插入99
grades = grades + [1,2,3] # 串接列表
grades.extend([4,5,6]) # 扩展列表
grades.remove(100) # 删除元素 删除第一个100
grades.pop() # 删除元素 删除最后一个元素
print('grades = ', grades)
print('列表的长度 = ', len(grades))
print('列表的最大值 = ', max(grades))
print('列表的最小值 = ', min(grades))
print('列表的和 = ', sum(grades))
print('列表的平均值 = ', sum(grades) / len(grades))
print('列表的排序 = ', sorted(grades))
print('列表的倒序 = ', sorted(grades, reverse=True))
print('列表的反转 = ', reversed(grades))
print('列表的复制 = ', grades.copy())
print('列表的清空 = ', grades.clear())
# tuple 有序不可变列表
gradesTuple = (95, 88, 92, 77, 90)
gradesTuple[1:4] = (100, 101, 102) # 修改元组中的元素 报错--不能修改
print('gradesTuple = ', gradesTuple)