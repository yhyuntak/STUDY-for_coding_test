from collections import deque
import sys
read = sys.stdin.readline

M,N = map(int,read().split())
graph = []
for _ in range(N):
    array = list(map(int,read().split()))
    graph.append(array)

dx = [0 , 0 , -1 , 1] # 상 하 좌 우
dy = [-1, 1, 0, 0] # 상 하 좌 우


# 한번 싹 훑으면서 토마토가 익은 것을 다 찾아서 queue에 넣자.
q = deque()
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1 :
            q.append([y,x])

# 함수 쓰지 말고 그냥 전개하자 어차피 반복문일뿐.
days = 0
while q:
    days += 1
    # print("days : {}".format(days))

    for qq in range(len(q)):
        now = q.popleft()
        for j in range(4):
            ny = now[0] + dy[j]
            nx = now[1] + dx[j]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if graph[ny][nx] == 0:  # 주변에 토마토가 안있었으면
                # 토마토를 익게하고 queue에 넣자
                graph[ny][nx] = 1
                # visited[ny][nx] = 1
                q.append([ny, nx])
    #
    # print(q)
    # for f in range(N):
    #     print(graph[f])
    # print()

check_zero = False
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            check_zero = True
if check_zero :
    print(-1)
else :
    print(days-1)
