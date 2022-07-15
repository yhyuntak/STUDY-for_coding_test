N = int(input())
dp_table = [[0,0] for _ in range(90)]
dp_table[0] = [1,1]

for i in range(1,N):
    dp_table[i][0] = sum(dp_table[i-1])
    dp_table[i][1] = dp_table[i-1][0]

print(dp_table[N-1][1])

