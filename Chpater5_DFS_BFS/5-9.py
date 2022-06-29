from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue : # 큐가 비면 False를 반환하나 봄.
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # 방문한 걸 넣고
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],

]

visited = [False]*9 # 이건 노드의 개수를 표현한다고 보면 될 듯 하다.

bfs(graph,1,visited)
