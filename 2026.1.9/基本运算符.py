# is  == 的区别
# is 是判断两个对象的内存地址是否相同
# == 是判断两个对象的值是否相同
a = [1,2,3]
b = [1,2,3]
print(a is b) # False
print(a == b) # True
print(id(a))
print(id(b))
print(a is not b) # True
print(a != b) # False
print(a is not b) # True