def han(n):
    if n < 100:
        hansu = n
    else:
        hansu = 99
        for i in range(100, n+1):
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1]-nums[2]:
                hansu += 1

    return hansu


N = int(input())
print(han(N))
