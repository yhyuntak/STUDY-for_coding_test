"""

격자 크기가 2^n x 2^n 이다.

A[r][c]는 (r, c)에 있는 얼음의 양이다.

단계 L을 결정. 파이어스톰은 먼저 격자를 2^L × 2^L 크기의 부분 격자로 나눈다.

그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다.

인접한 칸 중에서 얼음의 양이 3이상인 것이 없으면 얼음의 양이 1 줄어든다.

인접은 상하좌우다.

총 Q번 시전하려고 한다. 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.
1. 남아있는 얼음 A[r][c]의 합
2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.

"""
import copy

N,Q = map(int,input().split())
graph = []
len_graph = 2**N
for _ in range(len_graph):
    graph.append(list(map(int,input().split())))
from collections import deque
L_arr = deque(list(map(int,input().split())))

# 우,하,좌,상 순
dr = [0,1,0,-1]
dc = [1,0,-1,0]

while L_arr :

    L = L_arr.popleft()
    len_part = 2**L
    # L 단계는 부분 격자 2^L x 2^L 를 돌려야함 먼저.
    new_graph = [[0 for _ in range(len_graph)] for _ in range(len_graph)]

    # 일단 구간을 쪼개야하는데..
    for r in range(0,len_graph,len_part):
        for c in range(0,len_graph,len_part):
            # 한 부분 블럭의 개수는 2**L * 2**L 이다.
            for i in range(len_part):
                for j in range(len_part):
                    new_graph[r+j][c+(len_part-1)-i] = graph[r+i][c+j]

    for _ in range(len_graph):
        print(new_graph[_])
    """
        
    얼음이 있는 칸이 3개 이상 인접해 있지 않은 것은 얼음의 양이 1 줄어든다.
    인접한 칸 중 얼음이 있는 것이 1개 이하면 1 줄어든다.
    """

    # 모든 칸을 확인하면서 상하좌우를 탐색.
    melting_list = []
    for r in range(len_graph):
        for c in range(len_graph):
            ice_cnt = 0
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i]
                if 0<= nr < len_graph and 0<= nc < len_graph and new_graph[nr][nc] != 0 : # 경계선 안이면서 얼음이 있다.
                    ice_cnt += 1

            if ice_cnt <= 2 :
                melting_list.append([r,c])

    for r,c in melting_list :
        new_graph[r][c] -= 1

    graph = copy.deepcopy(new_graph)
    # bfs로 덩어리 확인.

    munch = []
    visit = [[0 for _ in range(len_graph)] for _ in range(len_graph)]
    for r in range(len_graph):
        for c in range(len_graph):
            if graph[r][c] != 0 and visit[r][c] == 0 :
                cnt = 1
                q=deque()
                q.append([r,c])
                visit[r][c] = 1
                while q :
                    rr,cc = q.popleft()
                    for i in range(4):
                        nr,nc = rr+dr[i],cc+dc[i]
                        if 0<= nr < len_graph and 0<= nc < len_graph and graph[nr][nc] != 0 and visit[nr][nc] == 0 : # 경계선 안이면서 얼음이 있다.
                            visit[nr][nc] = 1
                            cnt +=1
                            q.append([nr,nc])

                munch.append(cnt)

sums = 0
for _ in range(len_graph):
    sums+=sum(graph[_])
print(sums)
print(max(munch))