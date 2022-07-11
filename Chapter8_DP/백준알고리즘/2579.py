import sys
read = sys.stdin.readline

N = int(read())
graph = [0] * (301)
for i in range(1, N+1):
    graph[i] = (int(read()))

dp_table = [0] * (N+1)
dp_table[1] = graph[1]

if N == 1 :
    print(dp_table[1])

elif N == 2 :
    print(max(graph[2]+graph[1], graph[2]))

elif N == 3 :
    print(max(graph[3]+graph[1], graph[3]+graph[2]))

else :

    dp_table[2] = max(graph[2]+graph[1], graph[2])
    dp_table[3] = max(graph[3]+graph[1], graph[3]+graph[2])

    for i in range(4, N+1):
        dp_table[i] = max(graph[i]+dp_table[i-2], graph[i]+graph[i-1]+dp_table[i-3])

    print(dp_table[N])
