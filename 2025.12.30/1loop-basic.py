# range 生成一个连续的数字列表 range(10) 生成一个从 0 到 9 的列表 
# while 循环
  # n=1
  # sum=0
  # while n<=10:
  #   sum+=n
  #   n+=1
  # print(sum) # 1+2+3+4+5+6+7+8+9+10=55
# for in 循环
for i in range(1,11):
  print(i)

for i in "hello":
  print(i)

  # break continue  跳出循环和跳过当前循环 
  # 区别：break是跳出整个循环，continue是跳过当前循环继续执行下一个循环。
  for i in range(1,11):
    if i==5:
      print('退出循环')
      break
    print(i)
  for i in range(1,11):
    if i==5:
      print('跳过5')
      continue
    print('当前是',i)
 