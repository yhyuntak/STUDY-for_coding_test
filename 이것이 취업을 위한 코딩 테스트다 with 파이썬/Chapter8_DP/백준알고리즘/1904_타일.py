import sys
read = sys.stdin.readline
N = int(input())

if N == 1 :
    print(1%15746)
elif N == 2 :
    print(2%15746)
else :
    dp_table = [0]*(N+1)
    dp_table[1] = 1
    dp_table[2] = 2
    for i in range(3,N+1):
        dp_table[i] = (dp_table[i-1]+dp_table[i-2])%15746
    print(dp_table[N])
