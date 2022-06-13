N,K = map(int,input().split())


count_1 = 0
count_2 = 0
while True:

    if N == 1 :
        break
    print(N,count_1, count_2)

    if N % K == 0 :
        count_2 += 1
        N /= K

    else :
        mul = N % K
        count_1 += mul
        N -= mul

print(count_1+count_2)