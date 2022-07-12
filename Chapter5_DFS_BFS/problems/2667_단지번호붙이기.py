from collections import deque

dx = [0,0,-1,1] # 상 하 좌 우
dy = [-1,1,0,0] # 상 하 좌 우

def BFS(graph,x,y):
    q = deque()
    q.append((y,x))
    graph[y][x] = 0
    houses = 1

    while q:
        y,x = q.popleft()

        for i in range(4):
            # 상 하 좌 우 탐색
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([ny, nx])
                houses +=1
    return houses

import sys
read = sys.stdin.readline
N = int(read())
graph = []

for i in range(N):
    # 숫자가 붙어있을땐 이렇게 해야하는 듯.
    graph.append(list(map(int,input())))


houses_list = []

for i in range(N): # y
    for j in range(N): # x
        y,x = i,j # 현재 위치
        if graph[y][x] == 1:
        # 방문하지 않은 집이고, graph를 보았을 때 집이라면 이것과 연결된 것들을 탐색해서(BFS발동) 번지수를 만들자.
            houses = BFS(graph,x,y)
            houses_list.append(houses)

houses_list.sort()
print(len(houses_list))
for m in houses_list:
    print(m)