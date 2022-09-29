from collections import deque
import sys

def BFS(graph,V,visited):

    visited[V] = True
    q = deque([V])
    # q.append(V)

    while q :
        now = q.popleft()
        for k in graph[now]:
            if not visited[k] :
                visited[k] = True
                q.append(k)

read = sys.stdin.readline
N,M = map(int,read().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,read().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
cnt = 0
for j in range(1,N+1):
    if not visited[j] :
        BFS(graph,j,visited)
        cnt += 1
    else : continue
print(cnt)