# if 条件语句
# x = input("请输入一个数字:")
# x = int(x)
# if x>200: # 条件
#   print("x大于200")
# elif x>100:
#   print("x大于100")
# else: # 条件不成立
#   print("x小于100")

# 四则运算
n1 = int(input("请输入第一个数字:"))
n2 = int(input("请输入第二个数字:"))
op = input("请输入运算符: +, -, *, /: ")
if op == "+":
  print(n1+n2)
elif op == "-":
  print(n1-n2)
elif op == "*":
  print(n1*n2)
elif op == "/":
  print(n1/n2)
else:
  print("运算符错误")

