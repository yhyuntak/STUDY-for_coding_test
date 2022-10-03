N = int(input())

d = [0 for i in range(1001)]

if N == 1 :
    print(1)
elif N == 2 :
    print(2)
else :
    d[1] =1
    d[2] =2
    for j in range(3,N+1):
        d[j] = d[j-1]+d[j-2]
    print(d[N]%10007)
