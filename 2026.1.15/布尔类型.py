# 布尔类型：True 和 False

# flase的情况 false 、 0 、 空的类型、None、空字符串、空列表、空字典、空元祖、空集合、空范围
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(0j)) # False
print(bool(None)) # False
print(bool('')) # False
print(bool([])) # False
print(bool({})) # False
print(bool(())) # False
print(bool(set())) # False
print(bool(range(0))) # False

# true的情况 true 、 非0的数字、非空的类型、非空的字符串、非空的列表、非空的字典、非空的元祖、非空的集合、非空的范围
print(bool(True)) # True
print(bool(1)) # True
print(bool(0.1)) # True
print(bool(0j)) # True
print(bool(None)) # True