import sys
read = sys.stdin.readline
from collections import deque

def bfs(graph,y,x,summation):

    q = deque()
    graph[y][x] = 0 # 방문처리
    q.append([y,x])

    while q : # 큐가 빌 때까지
        now = q.popleft()
        for n in range(8):
            ny = now[0] + dy[n]
            nx = now[1] + dx[n]

            if nx <0 or ny <0 or nx >= W or ny >= H :
                continue

            if graph[ny][nx] == 1 : # 땅이라면 밟자.
                graph[ny][nx] = 0
                q.append([ny,nx])

        # while 한번이 한 뭉탱이가 끝나는 것
    summation += 1

    return summation



# 상 하 좌 우 좌상 좌하 우상 우하
dx = [0,0,-1,1,-1,-1,1,1]
dy = [-1,1,0,0,-1,1,-1,1]

summation_array = []
while True :

    summation = 0
    W,H = map(int,read().split())
    if W == 0 and H == 0 :
        break
    else :
        graph = []
        for h in range(H):
            graph.append(list(map(int,read().split())))
        for y in range(H):
            for x in range(W):
                if graph[y][x] == 1 : # 땅이라면 bfs 실행
                    summation = bfs(graph,y,x,summation)
                    # for mm in range(H):
                    #     print(graph[mm])
                    # print()
    summation_array.append(summation)

for kk in summation_array:
    print(kk)
