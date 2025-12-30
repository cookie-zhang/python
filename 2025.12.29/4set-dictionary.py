# 集合运算
s1 = {3,4,5}
print(3 in s1) # 判断3是否在s1中 true
print(2 in s1) # 判断2是否在s1中 false
print(2 not in s1) # 判断2是否不在s1中 true
print(2 not in s1) # 判断2是否不在s1中 true
s2 = {5,6,7}
s3 = s1 & s2 # 交集
print(s3) # {5}
s4 = s1 | s2 # 并集
print(s4) # {3,4,5,6,7}
s5 = s1 - s2 # 差集
print(s1,s2,s5) # {3,4} {5,6,7} {3,4}
s6 = s1 ^ s2 # 对称差集
print(s6) # {3,4,6,7}
# 字典运算