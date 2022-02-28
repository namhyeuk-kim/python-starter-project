case = int(input())
for i in range(case):
  x = input()
  score = 0
  sum = 0
  for j in x:
    if(j=='O'):
      score+=1
    
    else:
      score = 0
    sum+=score
  print(sum)
