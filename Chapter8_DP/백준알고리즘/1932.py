import sys
read = sys.stdin.readline

N = int(read())
graph = []
for _ in range(N):
    graph.append(list(map(int,read().split())))

dp_table = [[0 for _ in range(N)] for _ in range(N)]
dp_table[0] = graph[-1]
for i in range(1,N):
    for j in range(N-i):
        dp_table[i][j] = max(graph[N-1-i][j]+dp_table[i-1][j],
                             graph[N-1-i][j]+dp_table[i-1][j+1])

print(dp_table[-1][0])