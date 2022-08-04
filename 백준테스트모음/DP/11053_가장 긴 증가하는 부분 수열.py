import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
dp_table = [1] * N
for i in range(1,N):
    for j in range(i):
        if numbers[i] > numbers[j] :
            dp_table[i] = max(dp_table[i],dp_table[j]+1)
print(max(dp_table))
