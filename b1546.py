subject = int(input())
score = list(map(int,input().split()))
m = max(score)
n_score = []
for i in range(len(score)):
  n_score.append(score[i]/m*100)

avg = sum(n_score) / subject
print(avg)