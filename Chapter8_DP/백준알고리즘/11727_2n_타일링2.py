import sys
read = sys.stdin.readline
N = int(read())
dp_table = [0] * 1000
dp_table[0] = 1
dp_table[1] = 3
for i in range(2,N):
    dp_table[i] = dp_table[i-1]+dp_table[i-2]*2
print(dp_table[N-1]%10007)
