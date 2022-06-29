
def BFS(x,y):

    graph[x][y]



n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):

    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

            else : # 벽일 경우 무시
                continue
    return graph[n-1][m-1]

print(BFS(0,0))