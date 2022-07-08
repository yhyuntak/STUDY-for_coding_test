
from collections import deque

def DFS(graph,V,visited):
    visited[V] = True
    print(V,end = ' ')
    for i in graph[V]: # 현재 노드와 간선으로 연결된 다른 노드들을 하나씩 불러오기
        if not visited[i]: # 연결된 다른 노드가 방문되어있지 않으면(False), 방문처리하기 위해서 재귀함수 발동
            DFS(graph,i,visited)

def BFS(graph,V,visited):
    q = deque([V])
    visited[V] = True
    while q :
        now = q.popleft()
        print(now,end=' ')
        for i in graph[now] :
            # 현재 큐에서 뽑힌 now와 연결된 노드들을 하나씩 확인해서 방문 안했으면 queue에 넣기
            if not visited[i]:
                visited[i] = True
                q.append(i)


N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]

'''
여기선 그래프가 양방향임을 잊지말자!!!
'''
for i in range(1,M+1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1,N+1):
    graph[j].sort()


dfs_visited = [False]*(N+1)
bfs_visited = [False]*(N+1)
DFS(graph,V,dfs_visited)
print()
BFS(graph,V,bfs_visited)

