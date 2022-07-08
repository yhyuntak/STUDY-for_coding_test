from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    #컴퓨터는 서로 연결되어있으므로.
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited = [False for _ in range(N+1)]

def BFS(graph,V,visited):
    q = deque()
    q.append(V)
    while q :
        now = q.popleft()
        visited[now] = True
        for i in graph[now] :
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return visited


updated_visited = BFS(graph,1,visited)
print(sum(updated_visited)-1) # 1은 빼야한다.