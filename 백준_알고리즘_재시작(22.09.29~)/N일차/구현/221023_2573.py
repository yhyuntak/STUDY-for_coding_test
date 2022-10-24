"""

빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.

단, 높이는 음수가 되지 않는다.

 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
 그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

"""


N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 문제의 핵심은 모든 빙산이 한번에 녹는다는 것
# 매 회차마다 bfs를 통해 빙산이 두덩어리 이상이 될때까지 탐색
import copy
from collections import deque

def melting():

    temp = copy.deepcopy(graph)
    for r in range(N):
        for c in range(M):
            if temp[r][c] : # 바다가 아니라면, 녹이기 시작
                cnt = 0
                for i in range(4):
                    nr,nc = r+dr[i],c+dc[i]
                    if 0<=nr<N and 0<=nc<M and temp[nr][nc] == 0 : # 경계선 안이면서 바다인 곳찾기
                        cnt += 1
                graph[r][c] = max(0,temp[r][c]-cnt) # max를 취함으로써 graph[r][c]가 음수로 내려가면 0이 되게 만들기.

    del temp

def check_dump():

    temp_visit = copy.deepcopy(visit)
    check_cnt = 0
    for r in range(1,N-1):
        for c in range(1,M-1):
            if temp_visit[r][c] == 0 : # 방문하지 않은 곳
                if graph[r][c] != 0 :  # 바다가 아니고 빙산이니까 bfs 시작
                    check_cnt += 1
                    q = deque()
                    q.append([r,c])
                    temp_visit[r][c] = check_cnt
                    while q :
                        now_r,now_c = q.popleft()
                        for i in range(4):
                            nr,nc = now_r+dr[i],now_c+dc[i]
                            if (1 <= nr < N-1 and 1 <= nc < M-1 ) and temp_visit[nr][nc] == 0 and graph[nr][nc] != 0 : # 방문하지 않았는데 빙산이면 덩어리에 속한다.
                                temp_visit[nr][nc] = check_cnt
                                q.append([nr,nc])
                # else :
                #     temp_visit[r][c] = -1 # bfs때 시간 절약을 위해 바다는 -1처리

    return check_cnt


print_bool = False
visit = [[0 for _ in range(M)] for _ in range(N)]

times = 1
while True :

    # 모든 빙산이 한번에 녹는것을 구현
    if print_bool :
        print("before")
        for _ in range(N):
            print(graph[_])
        print()
    melting()
    if print_bool :
        print("melting")
        for _ in range(N):
            print(graph[_])
        print()

    # 빙산 덩어리 체크
    check_bool = check_dump()

    if check_bool >= 2 :
        print(times)
        break
    elif check_bool == 0 : # 빙산이 다 녹음을 의미함.
        print(0)
        break
    times+=1


