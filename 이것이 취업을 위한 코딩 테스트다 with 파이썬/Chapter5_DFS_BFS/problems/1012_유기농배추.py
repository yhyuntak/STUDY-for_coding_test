from collections import deque
import sys
read = sys.stdin.readline

dx = [0,0,-1,1] # 상 하 좌 우
dy = [-1,1,0,0] # 상 하 좌 우

def BFS(graph, x, y,M,N,cnt):
    # 처음 시작한 graph는 방문했으므로 0으로 만들어서 다신 못들어오게 막자.
    graph[y][x] = 0
    # queue를 생성하고 현재 위치를 queue에 넣자.
    q = deque()
    q.append([y,x])

    # while문을 통해 시작한 node의 주변 중 graph가 1인 것을 전부 탐색하자.
    while q :
        # now[0] = y, now[1] = x
        now = q.popleft()

        # 상 하 좌 우를 탐색하자.
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            # 그래프를 벗어나는 경우는 continue를 넣자
            if nx < 0 or ny < 0 or nx >= M or ny >= N :
                continue
            # 그래프를 벗어나지 않았고 graph가 1인 부분은 같은 지역으로 묶을 수 있다.
            if graph[ny][nx] == 1:
                # queue에 (ny,nx) 를 추가하고 cnt를 올리자. 그리고 다시 방문하지 않게 graph를 0으로 만들자
                q.append((ny,nx))

                graph[ny][nx] = 0
    cnt += 1
    return cnt

T = int(input())
cnt_array = []

for i in range(T):

    # graph 생성

    M,N,K = map(int,read().split())

    # 가로 M개 세로 N개
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(K):
        X,Y = map(int,read().split())
        graph[Y][X] = 1

    cnt = 0

    for x in range(M):
        for y in range(N):
            # 하나씩 탐방하면서 graph가 1이면 BFS를 시작하자
            if graph[y][x] == 1 :
                cnt = BFS(graph,x,y,M,N,cnt)

    cnt_array.append(cnt)

for z in range(len(cnt_array)):
    print(cnt_array[z])