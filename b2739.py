#N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
N = int(input())
for i in range(1,10):
  print("{0} * {1} = {2}".format(N,i,N*i))