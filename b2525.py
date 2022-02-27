# 입력 파트
data = input().split()
h = int(data[0])
m = int(data[1])
c = int(input())

#추가되는 시간(c) = ex)100 -> 1 40
p_h = c//60
p_m = c%60

#(p_m + m) // 60, (p_m + m) % 60
result_h = h + (p_h + ((p_m+m)//60))
result_m = (p_m + m) % 60

print(result_h % 24,result_m)