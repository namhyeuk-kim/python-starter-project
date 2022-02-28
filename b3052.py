x = []
for _ in range(10):
  num = int(input())
  x.append(num%42)

setX = set(x)
print(len(setX))

