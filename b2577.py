a = int(input())
b = int(input())
c = int(input())
x = a*b*c
result = list(str(x))

for i in range(0,10):
  print(result.count(str(i)))
  