N = int(input())
origin_n = N
cnt = 0

while True:
  x = N//10
  y = N%10
  N = 10*y + (x+y)%10
  cnt+=1;
  
  if(N == origin_n):
    break

print(cnt)