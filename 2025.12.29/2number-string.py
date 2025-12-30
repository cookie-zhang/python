# 数字运算
# 加法
x = 10 + 5
print('x = ', x)
# 减法
x = 10 - 5
print('x = ', x)
# 乘法
x = 10 * 5
print('x = ', x)
# 除法 包含小数
x = 10 / 5
# 整除 不会出现小数
x = 10 // 3 # 结果为 3
x = 3 // 6 # 结果为 0
print('x = ', x)
# 取余
x = 10 % 3
print('x = ', x)
# 幂运算
x = 2 ** 3
print('x = ', x)
# 字符串
s='hello'
s2='world'
s3=s+s2
s4 = """换行
 换行"""
s5 = " hello \n world "
s6 = "hello"*3+"world" # hello字符串重复3次+world字符串
print('s6 = ', s6)
# 字符串会自动对内部进行编号（索引），索引从0开始
s7 = "hello"
print('s7[0] = ', s7[0]) # h
print('s7[1] = ', s7[1]) # e
print('s7[2] = ', s7[2]) # l
print('s7[3] = ', s7[3]) # l
print('s7[4] = ', s7[4]) # o
print('s7[-1] = ', s7[-1]) # o
print('s7[1:3] = ', s7[1:3]) # el