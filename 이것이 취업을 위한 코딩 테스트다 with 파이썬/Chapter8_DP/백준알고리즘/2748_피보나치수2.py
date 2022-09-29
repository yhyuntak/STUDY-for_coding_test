N = int(input())
dp_table = [0]*(N+1)
dp_table[0] = 0
dp_table[1] = 1
for i in range(2,N+1):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]

print(dp_table[-1])