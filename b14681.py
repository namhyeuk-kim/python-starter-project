#좌표가 주어지면 1~4사분면 중 어떤 사분면인지 알려주는 프로그램(x!=0, y!=0)
x = int(input())
y = int(input())

if (x > 0 and y > 0):
  print(1)

elif (x < 0 and y > 0):
  print(2)

elif (x < 0 and y < 0):
  print(3)

else:
  print(4)