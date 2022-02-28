case = 9
max = 0
x = []
for i in range(case):
  n = int(input())
  x.append(n)
  if(x[i] > max):
    max = x[i]
    cnt = i
print(max)
print(cnt+1)