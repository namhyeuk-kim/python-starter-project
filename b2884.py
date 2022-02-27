#원래 시간이 주어지면 -45분으로 시간 맞추기
data = input().split()
h = int(data[0])
m = int(data[1])
if(h != 0):
  if(m >= 45):
    print(h,m-45)
  elif(m < 45):
    print(h-1,m+15)

if(h == 0):
  if(m >= 45):
    print(h,m-45)
  elif(m < 45):
    print(23,m+15)