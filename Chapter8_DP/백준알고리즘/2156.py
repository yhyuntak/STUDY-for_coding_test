import sys
read = sys.stdin.readline

N = int(input())

graph = [0]
for i in range(1,N+1):
    graph.append(int(input()))

dp_table = [0]*(N+1)

if N == 1 :
    print(graph[1])
elif N == 2:
    print(graph[1]+graph[2])
elif N == 3 :
    print(max(graph[1],graph[2])+graph[3])

else :
    maximum_val = 0
    dp_table[1] = graph[1]
    dp_table[2] = graph[1]+graph[2]

    for j in range(3,N+1):
        # print(j,dp_table[j-2],graph[j-1]+dp_table[j-3])
        dp_table[j] = max(dp_table[j-2],graph[j-1]+dp_table[j-3])+graph[j]
        print(j,dp_table[j-1],dp_table[j])
        dp_table[j] = max(dp_table[j],dp_table[j-1])

    print((dp_table))

