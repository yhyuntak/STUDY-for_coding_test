import sys
read =sys.stdin.readline

N = int(read())
graph = []

max_height = 0
for _ in range(N):
    temp = list(map(int,read().split()))
    graph.append(temp)
    max_height = max(max_height,max(temp))

dx = [0 ,0,-1,1]
dy = [-1,1,0,0]

from collections import deque

result_height = 0
for h in range(0,max_height):
    visited = [[-1] * N for _ in range(N)]

    q = deque()
    cnt = 0
    for y in range(N):
        for x in range(N):
            # 현재 위치가 침수됬는지 혹은 방문했었는지 확인
            if graph[y][x] <= h or visited[y][x] != -1 :
                continue
            else :
                q.append([y, x])
                visited[y][x] = 1
                # 아니라면 bfs 실행
                while q :
                    now = q.popleft()
                    for j in range(4):
                        ny = now[0] + dy[j]
                        nx = now[1] + dx[j]
                        # 정상 범주에 있고, 방문하지 않았어야함. 그리고 기둥이 침수되지 않아야함.
                        if 0<=ny<N and 0 <= nx < N and visited[ny][nx] == -1 and graph[ny][nx] > h :
                            visited[ny][nx] = cnt
                            q.append([ny,nx])

                cnt+=1
    result_height = max(result_height,cnt)
print(result_height)
