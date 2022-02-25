#오름정렬

#1.버블 정렬
n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()
for i in range(len(nums)):
    print(nums[i])

#2. 삽입 정렬
n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))
    
for i in range(1,len(nums)):
    while (i>0) & (nums[i] < nums[i-1]):
        nums[i],nums[i-1] = nums[i-1],nums[i]
        
        i -= 1
for x in nums:
    print(x)