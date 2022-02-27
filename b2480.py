data = input().split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
m = max(data)
if (a==b and b==c):
  print(10000+a*1000)

elif(a==b or b==c):
  print(1000+b*100)

elif(a==c):
  print(1000+a*100)

else:
  print(int(m)*100)