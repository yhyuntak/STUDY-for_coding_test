"""

cctv는 감시할 수 있는 방향에 있는 칸 전체를 감시.

감시 못하는 부분은 사각지대이고 벽너머는 못본다.

회전은 90도로 감시 방향은 가로 또는 세로

0은 빈칸, 6은 벽, 1~5는 cctv 번호

cctv끼리는 통과가 가능하다.

cctv의 방향을 적절히 선택해서 사각지대의 최소 크기를 구하라.

"""

N,M = map(int,input().split())

graph = []
cctvs = []
blind = 0
for r in range(N):
    temp = list(map(int,input().split()))
    blind += temp.count(0)
    for c in range(M):
        if 1<=temp[c] < 6:
            cctvs.append([r,c,temp[c]])
    graph.append(temp)

# 각 cctv당 아직 방향이 없음.
# 그리고 90도로만 회전 가능함.
# 근데 이건 아마도 모든 cctv의 4방향의 경우의 수를 다 따지는 문제같음.

# 바라보는 방향 : 상 0 좌 1 하 2 우 3
direction = [0,1,2,3]

# 근데 방향들이 중복이 가능하니까, 이건 dfs로 중복조합을 찾아야함.

directions = []
from copy import deepcopy as dp

def dfs(dd):
    if len(dd) == len(cctvs):
        directions.append(dp(dd))
        return
    for i in range(4):
        dd.append(i)
        dfs(dd)
        dd.pop()

comb = []
dfs(comb)

# 이제 중복 조합을 찾았으니, cctv가 바라보는 것을 구현하기만 하면됌.
# 방향의 기준은 무조건 ->방향임.

cctv_1 = [0]
cctv_2 = [0,2]
cctv_3 = [0,3]
cctv_4 = [0,2,3]
cctv_5 = [0,1,2,3]

#  상 0 좌 1 하 2 우 3
dr = [-1,0,1,0]
dc = [0,-1,0,1]


def up_0(r,c):
    for i in range(r,-1,-1):
        if temp_visited[i][c] == 6 :
            break
        elif temp_visited[i][c] == 0 :
            temp_visited[i][c] = 9

def left_1(r,c):
    for i in range(c,-1,-1):
        if temp_visited[r][i] == 6 :
            break
        elif temp_visited[r][i] == 0 :
            temp_visited[r][i] = 9

def down_2(r,c):
    for i in range(r,N):
        if temp_visited[i][c] == 6 :
            break
        elif temp_visited[i][c] == 0 :
            temp_visited[i][c] = 9

def right_3(r,c):
    for i in range(c,M):
        if temp_visited[r][i] == 6 :
            break
        elif temp_visited[r][i] == 0 :
            temp_visited[r][i] = 9

def move(d,r,c) :
    if d == 0 :
        return up_0(r,c)
    elif d == 1 :
        return left_1(r,c)
    elif d == 2 :
        return down_2(r,c)
    elif d == 3 :
        return right_3(r,c)

min_blind = 10e9
from copy import deepcopy as dp
for temp_dir in directions :
    temp_visited = dp(graph)
    ww = 0
    for direct,cctv in zip(temp_dir,cctvs) :
        if cctv[2] == 1 :
            move(direct,cctv[0],cctv[1])

        elif cctv[2] == 2 :
            # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
            move(direct,cctv[0],cctv[1])
            move((direct+2)%4,cctv[0],cctv[1])

        elif cctv[2] == 3:
            # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
            move(direct, cctv[0], cctv[1])
            move((direct + 1) % 4, cctv[0], cctv[1])

        elif cctv[2] == 4:
            # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
            move(direct, cctv[0], cctv[1])
            move((direct + 1) % 4, cctv[0], cctv[1])
            move((direct + 2) % 4, cctv[0], cctv[1])

        elif cctv[2] == 5:
            # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
            move(direct, cctv[0], cctv[1])
            move((direct + 1) % 4, cctv[0], cctv[1])
            move((direct + 2) % 4, cctv[0], cctv[1])
            move((direct + 3) % 4, cctv[0], cctv[1])

    for _ in range(N):
        ww += temp_visited[_].count(9)
        # print(temp_visited[_])
    # print(ww)
    min_blind = min(min_blind,blind-ww)

print(min_blind)
#
# def cctv_dfs(d,r,c,cctv_num):
#
#     # # 여기엔 벽을만나거나 범위를 벗어나면의 조건문으로 종료문을.
#     # if r < 0 or N <= r or c < 0 or M <= c :
#     #     return -1
#     # else :
#     #     if graph[r][c] == 6 :
#     #         return -1
#
#     nr,nc = r+dr[d],c+dc[d]
#     if 0<= nr < N and 0<= nc < N and graph[nr][nc] != 6 :
#         temp_visited[nr][nc] = 9
#         if graph[nr][nc] != 0 :
#             temp =  cctv_dfs(d, nr, nc, cctv_num)
#             return temp #cctv_dfs(d, r + dr[d], c + dc[d], cctv_num)
#         else :
#             temp =  cctv_dfs(d, nr, nc, cctv_num)
#             return temp +1 #cctv_dfs(d, r + dr[d], c + dc[d], cctv_num)
#     else :
#         return 0
    # return val
#
# min_blind = 10e9
# visited = [[0 for _ in range(M)] for _ in range(N)]
# from copy import deepcopy as dp
# for temp_dir in directions :
#     watcher = 0
#     ww = 0
#     for direct,cctv in zip(temp_dir,cctvs) :
#         # dfs로 구현해보고싶네?
#         # cctv 번호 별 dfs문을 만들어야하네.
#         temp_visited = dp(visited)
#
#         if cctv[2] == 1 :
#
#             temp =  cctv_dfs(direct,cctv[0],cctv[1],cctv[2])
#             watcher += temp
#         elif cctv[2] == 2 :
#             # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
#             watcher += cctv_dfs(direct,cctv[0],cctv[1],cctv[2])
#             watcher += cctv_dfs((direct+2)%4,cctv[0],cctv[1],cctv[2])
#
#         elif cctv[2] == 3:
#             # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
#             watcher += cctv_dfs(direct, cctv[0], cctv[1], cctv[2])
#             watcher += cctv_dfs((direct + 1) % 4, cctv[0], cctv[1], cctv[2])
#
#         elif cctv[2] == 4:
#             # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
#             watcher += cctv_dfs(direct, cctv[0], cctv[1], cctv[2])
#             watcher += cctv_dfs((direct + 1) % 4, cctv[0], cctv[1], cctv[2])
#             watcher += cctv_dfs((direct + 2) % 4, cctv[0], cctv[1], cctv[2])
#
#         elif cctv[2] == 5:
#             # 방향만 바꿔주면서 dfs하고 와서 각각 더해주면 끝임.
#             watcher += cctv_dfs(direct, cctv[0], cctv[1], cctv[2])
#             watcher += cctv_dfs((direct + 1) % 4, cctv[0], cctv[1], cctv[2])
#             watcher += cctv_dfs((direct + 2) % 4, cctv[0], cctv[1], cctv[2])
#             watcher += cctv_dfs((direct + 3) % 4, cctv[0], cctv[1], cctv[2])
#
#         for _ in range(N):
#             ww += temp_visited[_].count(9)
#         print(temp_visited)
#         print(ww)
#     min_blind = min(min_blind,blind-ww)
#
# print(min_blind)