a,b = map(int,input().split())
a_list = list(str(a))
b_list = list(str(b))
a_list.reverse()
b_list.reverse()

a_list = list(map(int,a_list))
b_list = list(map(int,b_list))
A = a_list[0]*100 + a_list[1]*10 + a_list[2]*1
B = b_list[0]*100 + b_list[1]*10 + b_list[2]*1
if A > B:
    print(A)
else:
    print(B)