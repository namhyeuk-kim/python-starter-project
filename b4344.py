test_case = int(input())

for _ in range(test_case):
  x = list(map(int,input().split()))
  avg = sum(x[1:])/ x[0]
  cnt = 0
  for score in x[1:]:
    if (score > avg):
      cnt+=1
  rate = cnt/x[0] * 100
  print(f'{rate:0.3f}%')