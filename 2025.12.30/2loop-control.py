# break
n=0
while n<10:
  n+=1
  if n==5:
    break
  print(n)
print('退出循环', n)

# continue
n=0
while n<10:
  n+=1
  if n==5:
    print('跳过5')
    continue
  print('当前是',n)
print('退出循环', n)