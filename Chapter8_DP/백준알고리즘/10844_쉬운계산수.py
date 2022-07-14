N = int(input())

dp_table = [[0 for _ in range(10)] for _ in range(N)]
dp_table[0] = [1,1,1,1,1,1,1,1,1,1]

if N == 1 :
    print((sum(dp_table[N-1])-1)%1000000000)

else :
    for i in range(1,N):
        for j in range(10):
            if j == 0 :
                dp_table[i][j] = dp_table[i - 1][j + 1]
            elif j == 9 :
                dp_table[i][j] = dp_table[i - 1][j - 1]
            else :
                dp_table[i][j] = dp_table[i - 1][j - 1] + dp_table[i - 1][j + 1]
    print((sum(dp_table[N-1])-dp_table[N-1][0])%1000000000)
