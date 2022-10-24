# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.


R,C = map(int,input().split())
graph = []
dest = [0,0]
start = [0,0]
for r in range(R):
    temp = list(input())
    list_ = []
    for c,t in enumerate(temp) :
        list_.append(t)
        if t == 'D':
            dest = [r,c]
        elif t == 'S' :
            start = [r,c]
    graph.append(list_)

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]


import copy
from collections import deque

def pour_water(g):
    global R,C

    temp_map = copy.deepcopy(g)
    for r in range(R):
        for c in range(C):
            if temp_map[r][c] == '*' : # 물이 있는 곳이라면
                for i in range(4):
                    nwr,nwc = r+dr[i],c+dc[i]
                    if 0<=nwr<R and 0<=nwc<C and temp_map[nwr][nwc] == '.' : #경계선 안이고, 비어있는 칸이라면
                        g[nwr][nwc] = '*' # 물 채우기
    del temp_map
    return g

q = deque()
q.append(start)

stops = False
times = 0
graph[start[0]][start[1]] = 0

while q and not stops :


    # 어차피 물이 찰 곳은 이동할 수 없으니까. 물이 먼저 차버리자.
    graph = pour_water(graph)
    #
    # print(q)
    # for _ in range(R):
    #     print(graph[_])
    # print()

    # 비버 움직이기
    # 비버는 다양한 경로로 갈 수 있다.
    # 따라서 매분 모든 경로가 갈 수 있는 길을 queue에서 뽑아서 찾자
    for _ in range(len(q)):
        if stops :
           break
        now = q.popleft()
        # 4방향
        for i in range(4):
            nr, nc = now[0] + dr[i], now[1] + dc[i]
            if nr == dest[0] and nc == dest[1] : # 목적지에 도착한다면
                stops = True
                q = [True]
                break
            if (0<=nr<R and 0<=nc<C) and graph[nr][nc] == '.': # 빈칸이고 가본적없으면 간다.
                q.append([nr,nc])
                graph[nr][nc] = times+1

    times += 1
if len(q) == 0 :
    print('KAKTUS')
else :
    print(times)
