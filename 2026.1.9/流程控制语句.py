# if else  elif
age = 18
if age >= 18:
    print("成年")
else:
    print("未成年")

# if elif else
age = 18
if age >= 18:
    print("成年")
elif age >= 12:
    print("青少年")
else:
    print("儿童")

    
# 登录注册
username = input("请输入用户名：")
password = input("请输入密码：")
if username == "admin" and int(password) == 123456:
    print("登录成功")
else:
    print("登录失败")


# 循环结构 while
count = 0
while count < 10:
    print(count)
    count += 1

# 循环结构 for   range 指定区间的整数序列 默认从0开始 到 10 不包括10 range(1,10,2) 步长为2
for i in range(10):
    print(i)

# 循环结构 for 遍历列表
for i in [1,2,3,4,5]:
    print(i)

# 循环结构 for 遍历字典