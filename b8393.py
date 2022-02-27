def addNum(n): 
  sum = 0
  for n in range(1,n+1):
    sum += n
  
  return sum

x = int(input())
print(addNum(x))