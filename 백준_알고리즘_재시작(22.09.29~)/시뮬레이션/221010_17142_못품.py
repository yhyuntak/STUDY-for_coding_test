"""

1초에 동시 복제됨. 상하좌우로. 바이러스 M개를 활성 상태로 하려함.

활성화가 비활성화로 가게되면 비활성이 활성으로 바뀜.

0은 빈칸 1은 벽 2는 바이러스

"""

import sys
read = sys.stdin.readline
N,M = map(int,read().split())
graph = []
from collections import deque
viraus = deque()
check_map = [[0 for _ in range(N)] for _ in range(N)] # 가지 못한 곳은 0으로 표기하자.
for r in range(N):
    temp = list(map(int,read().split()))
    # 바이러스들의 위치를 일단 수집
    for i,t in enumerate(temp) :
        if t == 1 : # 벽이라면
            check_map[r][i] = '-'
        elif t == 2 :
            viraus.append([r,i])
            check_map[r][i] = '*'

    graph.append(temp)

"""

바이러스가 놓여진 곳을 중복 없이 M개 뽑는 조합을 찾는다.(DFS) 

선택되면 BFS로 모든 칸에 다 바이러스를 퍼트린다. 

비활성화된 바이러스가 있는 칸은 횟수로 치지 않는 느낌.

BFS가 끝나는 시점의 시간을 세면 될듯?

"""

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

origin_visit = [[-1 for _ in range(N)] for _ in range(N)]
from copy import deepcopy as dp

def bfs(arr):
    global N
    # arr는 활성화 바이러스의 조합을 얘기한다.
    # 1초에 모든 활성화 바이러스는 자기 주변을 감염시킨다는게 포인트.
    # check맵에서  0은 갈 수 있는 곳, -는 벽, *는 비활성 바이러스다
    visit = dp(origin_visit)
    for a,b in arr : # 현재 활성화 바이러스의 위치를 0으로.
        visit[a][b] = 0
    q = deque(arr)
    # print("start : ",q)
    # for _ in range(N):
    #     print(check_map_[_])
    # print()
    max_time = 0
    while q : # 1번의 루프가 1초를 뜻한다.
        # for문을 써서 모든 q가 돌때까지
        for i in range(len(q)):
            now_r,now_c = q.popleft()
            # check_map_[now_r][now_c] = 1 # 현재 위치 방문.
            for j in range(4):
                nr,nc = now_r+dr[j],now_c+dc[j]
                if 0<= nr < N and 0<= nc < N : # 그래프 안에 있고,
                    # 다음 위치가 그냥 공간인지, 비활성화 바이러스인지에 따라 값이 바뀜.
                    # 아마 비활성화면 그냥 값만 옮겨주는 느낌으로 갈까.
                    # 그리고 다른 바이러스가 이미 갔던 길일 수도 있음. 근데 그럼 0이 아니라서 그냥 아래 조건으로 해결됌.
                    if graph[nr][nc] == 0 and visit[nr][nc] == -1 : # 공간이라면,
                        visit[nr][nc] = visit[now_r][now_c] + 1
                        q.append([nr,nc])
                        max_time = max(max_time,visit[nr][nc])

                    elif graph[nr][nc] == 2 and visit[nr][nc] == -1: # 비활성화 바이러스라면,
                        visit[nr][nc] = visit[now_r][now_c]
                        q.append([nr,nc])

    for a,b in arr : # 현재 활성화 바이러스의 위치를 갔다는 표시로.
        visit[a][b] = 9
    print("start arr : ",arr)
    for _ in range(N):
        print(visit[_])
    print()
    for ii in range(N):
        for jj in range(N):
            if visit[ii][jj] == 0 :
                return 10e9
    return max_time # 만약 다 가봤다면,

def dfs(idx,arr): # x : row , y : col, cnt : 활성화 바이러스 수
    global M,min_time
    if len(arr) == M :
        # 탐색 알고리즘.
        min_time = min(min_time,bfs(arr))
        return
    for i in range(idx,len(viraus)):
        arr.append(viraus[i])
        dfs(i+1,arr)
        arr.pop()

min_time = 10e9
run_vi = []
dfs(0,run_vi)
if min_time >= 10e9 :
    print(-1)
else :
    print(min_time)
