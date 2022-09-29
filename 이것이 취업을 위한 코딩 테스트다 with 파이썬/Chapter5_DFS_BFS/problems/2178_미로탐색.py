from collections import deque

N,M = map(int,input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,input()))

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0 , 0 , -1 , 1] # 상 하 좌 우
dy = [-1, 1 , 0 , 0] # 상 하 자 우

def BFS(graph,start,visited):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q :

        (x,y) = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                # 맵을 벗어나면 continue
                continue
            if graph[nx][ny] == 0 :
                # 벽에 가로막히면 continue
                continue
            if graph[nx][ny] == 1:
                # 방문했을 때 첫 방문이면
                # x,y의 방법보다 1만큼 더 간 것이기 때문에
                # 간단히 1을 더해주자.
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return graph[N-1][M-1]


print(BFS(graph,(0,0),visited))
