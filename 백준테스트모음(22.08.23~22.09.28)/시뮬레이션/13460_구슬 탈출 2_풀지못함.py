"""
ROW : N , COLUMN : M
보드에는 구멍이 하나 있음 : O
게임 목표는 빨간 구슬을 구멍을 통해 빼는 것 이때 파란건 들어가면 안됌

이리저리 굴려서 하는데, 상하좌우로 기울이기 가능

모든 공은 동시에 움직이는 듯. 빨간거만 단독으로 들어가야 성공임.
구슬들은 동시에 같은 칸에 있을 수 없음.

기울이는 동작을 그만하는것은 구슬이 더이상 움직이지 않을때까지.

보드,구슬이 주어지면 최소 몇번만에 빨간걸 구멍으로 뺄 수 있는가?
10번을 초과하면 -1을 출력할 것

"""
import sys
read = sys.stdin.readline
N,M = map(int,read().split())


# 이 문제의 핵심은 모든 공이 한번에 움직이는 것을 잊지 않는 것.
# 그렇다는건 공의 위치를 항상 파악하고 BFS를 돌려야한다는 것
# 그래프를 생성할 때 공의 위치를 파악해두자.

graph = [[0 for _ in range(M)] for _ in range(N)]
ball_loc = []
for r in range(N):
    temp = read()
    temp = temp[:-1]
    for c,t in enumerate(temp) :
        # 공의 위치들 먼저 저장
        if t == 'B' :
            ball_loc.append([r,c,'B'])
        elif t == 'R' :
            ball_loc.append([r,c,'R'])

        # 벽,현재 공이 있는 곳을 장애물로 처리하기
        if t == 'B' or t == 'R' or t == "#" :
            graph[r][c] = 1
        # 출구는 -1로 표현할까?
        elif t == 'O' :
            graph[r][c] = -1

# 이제 그래프랑 볼의 위치 파악은 끝남.

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# DFS로 풀어보자

start = [[ball_loc]+[0]]

def DFS(balls_count):

    # 상 우 하 좌를 실행하자.
    for i in range(4):
        if i == 0 : # 상일 때
            # 더 위에있는 것 먼저 (내림차순으로 정렬할 것.)
            now_ball_loc.sort(key=lambda x : x[0])

        elif i == 1 : # 우일 때
            # 더 오른쪽에 있는 것 먼저 (오름차순)
            now_ball_loc.sort(key=lambda x:-x[1])

        elif i == 2 : # 하일 때
            # 더 아래에 있는 것 먼저 (오름차순)
            now_ball_loc.sort(key=lambda x : -x[0])

        elif i == 3:  # 좌일 때
            # 더 왼쪽에 있는 것 먼저 (내림차순)
            now_ball_loc.sort(key=lambda x: x[1])

#
# # BFS를 이용해서 도착할때마다의 모든 경우의 수의 걸리는 횟수를 기록하자.
#
# from collections import deque
# q = deque([[ball_loc]+[0]])
#
# while q :

#
# while q :
#     now_balls = q.popleft()
#
#     for i in range(4):
#         # 상0 우1 하2 좌3 에 따라서 ball_loc을 재정렬하고 움직임을 추가해보자.
#         if i == 0 : # 상일 때
#             # 더 위에있는 것 먼저 (내림차순으로 정렬할 것.)
#             now_ball_loc.sort(key=lambda x : x[0])
#             # 순서대로 움직여보자.
#             for ball_r,ball_c,ball in now_ball_loc :
#                 while True: # 갈 수 있을 때까지를 의미
#                     # 일단 공이 있던 위치를 0으로 초기화
#                     graph[ball_r][ball_c] = 0
#                     # 그리고 갈 수 있으면 가고 없으면 말자.
#                     temp_ball_r,temp_ball_c = ball_r+dr[i],ball_c+dc[i]
#                     if  graph[temp_ball_r][temp_ball_c] == 0 : # 갈 수 있으면
#                         # 갔다고 처리
#                         graph[temp_ball_r][temp_ball_c] = 1
#                         ball_r,ball_c = temp_ball_r,temp_ball_c
#                     else : # 갈 수 없으면
#                         break
#
#         elif i == 1 : # 우일 때
#             # 더 오른쪽에 있는 것 먼저 (오름차순)
#             now_ball_loc.sort(key=lambda x:-x[1])
#
#         elif i == 2 : # 하일 때
#             # 더 아래에 있는 것 먼저 (오름차순)
#             now_ball_loc.sort(key=lambda x : -x[0])
#
#         elif i == 3:  # 좌일 때
#             # 더 왼쪽에 있는 것 먼저 (내림차순)
#             now_ball_loc.sort(key=lambda x: x[1])
#
#
#     # 빨간 공이 O에 도착하면 QUEUE에 넣지 말자.
#






