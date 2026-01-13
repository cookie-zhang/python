# 整数值
num = 10

# 1. 强制类型转换
# 可以将符合整数类型的字符串强制转换成整数类型
str_num = "100"
print(type(str_num))
print(type(int(str_num)))

# 进制转换
print(bin(num))
print(oct(num))
print(hex(num))

# 二进制转换
print(int(0b1010)) # 10
print(int(0o12)) # 10
print(int(0x12)) # 10 

# 八进制转换
print(oct(10)) # 0o12
print(hex(10)) # 0xa
 
# 十六进制转换
print(hex(10)) # 0xa
print(hex(10)) # 0xa