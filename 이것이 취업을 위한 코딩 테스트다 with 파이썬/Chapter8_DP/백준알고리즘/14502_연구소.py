import copy
from collections import deque

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

dx = [0 ,0, -1, 1] # 상 하 좌 우
dy = [-1 ,1 ,0, 0] # 상 하 좌 우

maximum = 0


def bfs():
    # 모든 바이러스를 detect하고 queue에 넣자
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for y in range(N):
        for x in range(M):
            if tmp_graph[y][x] == 2:
                q.append([y, x])

    while q:
        now = q.popleft()
        for j in range(4):
            ny = now[0] + dy[j]
            nx = now[1] + dx[j]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if tmp_graph[ny][nx] == 0:  # 아직 방문하지 않았다면
                q.append([ny, nx])
                tmp_graph[ny][nx] = 2

    global maximum


    cnt = 0
    for v in range(N):
        cnt += tmp_graph[v].count(0)
    maximum = max(maximum,cnt)

# 벽부터 만들어보자
def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for a in range(N):
        for b in range(M):
            if graph[a][b] == 0:
                graph[a][b] = 1
                make_wall(cnt + 1)
                graph[a][b] = 0

make_wall(0)
print(maximum)