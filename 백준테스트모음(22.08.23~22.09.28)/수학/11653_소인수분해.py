N= int(input())

nums = 2
while N != 1 :
    # 나눠진다면
    if N % nums == 0 :
        print(nums)
        N /= nums

    # 안나눠 진다면
    else :
        nums += 1

