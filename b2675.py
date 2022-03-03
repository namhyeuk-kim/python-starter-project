test_case = int(input())
for _ in range(test_case):
  x, word = input().split()
  for i in word:
    print(int(x)*i,end="")
  print()