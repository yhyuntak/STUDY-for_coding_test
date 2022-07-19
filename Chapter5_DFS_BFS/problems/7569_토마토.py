import sys
read =sys.stdin.readline
from collections import deque

M,N,H = map(int,read().split())

graph = [[[] for _ in range(N)] for _ in range(H)] # 제일 바깥부터 순서대로 H,N,N이다

# 모든 칸에서 토마토가 존재하는지 확인하고 우선적으로 QUEUE에 넣어야한다.
q = deque()
for h in range(H):
    for n in range(N):
        graph[h][n] = list(map(int,read().split()))
        tomato_temp = [i for i,tomato in enumerate(graph[h][n]) if tomato == 1]
        if len(tomato_temp) >= 1 : # 토마토가 있다면 queue에 정보를 넣자
            for t in tomato_temp :
                q.append([h,n,t])

# 움직임 설정
# 상 하 좌 우 위 아래
dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dh = [0,0,0,0,1,-1]

days = 0
while q :
    # 하루에 영향을 끼칠 수 있는 토마토는 전부 영향을 끼쳐야하므로
    # for문을 넣어서 전부 사용되게끔 유도
    for i in range(len(q)):
        now_tomato = q.popleft()
        # 6가지 행동을 파악
        for j in range(6):
            nh = now_tomato[0] + dh[j]
            ny = now_tomato[1] + dy[j]
            nx = now_tomato[2] + dx[j]
            # 상자의 정상 범주 안에 있어야하는 조건 하에 진행
            if 0<=nx<M and 0<=ny<N and 0<=nh<H :
                # 주변의 토마토가 있다면(0) 그것을 익었다고 처리하고(1)
                # queue에 넣자
                if graph[nh][ny][nx] == 0 :
                    graph[nh][ny][nx] = 1
                    q.append([nh,ny,nx])

    days += 1

zero_count = 0
for h in range(H):
    for n in range(N):
        zero_count += graph[h][n].count(0)
if zero_count == 0 :
    print(days-1)
else :
    print(-1)
