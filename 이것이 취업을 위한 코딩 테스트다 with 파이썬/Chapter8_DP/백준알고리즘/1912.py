import sys
read = sys.stdin.readline

N = int(read())
graph= list(map(int,read().split()))

dp_table = [0] * N
maximum_value = -1e9

dp_table[0] = graph[0]
maximum_value = max(dp_table[0], maximum_value)

for i in range(1,N):
    dp_table[i] = max(graph[i]+dp_table[i-1],graph[i])
    maximum_value = max(dp_table[i],maximum_value)
print(maximum_value)
