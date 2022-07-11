import sys
read = sys.stdin.readline
N = int(read())
graph = [ list(map(int,read().split())) for _ in range(N)]
dp_table =[[0 for _ in range(3)] for __ in range(N)] # N번째 집마다 RGB의 값들을 표현하자. 즉, NX3의 모습을

dp_table[0] = graph[0]
for i in range(1,N):
    dp_table[i][0] = min(dp_table[i-1][1], dp_table[i-1][2]) + graph[i][0]
    dp_table[i][1] = min(dp_table[i-1][0], dp_table[i-1][2]) + graph[i][1]
    dp_table[i][2] = min(dp_table[i-1][0], dp_table[i-1][1]) + graph[i][2]

print(min(dp_table[-1]))