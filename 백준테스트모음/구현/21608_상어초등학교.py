"""
규칙
1. 비어있는 칸 중, 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를
2. 1을 만족하는게 여러개면 인접칸중 빈 칸이 가장 많은 칸으로 자리를
3. 2도 여러개면, <행 번호가 가장 작은칸>으로 그래도 여러개면 <열 번호가 가장 작은 칸>
"""

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

# 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

save_students = [[] for _ in range(N**2+1)]

# 일단 for문이 기본으로 N의 제곱번 돌아야할 것이다.
for n in range(N*N):
    like_students = list(map(int,input().split()))
    student_num = like_students.pop(0)

    save_students[student_num] = like_students

    # 구현, 시뮬레이션은 말을 그대로 따라가는게 최우선이다.
    # 1. 빈 곳 중, 좋아하는 학생이 가장 많은 칸을 찾는 알고리즘을 구현해야함.
    # 이건 일일이 탐색하는 수밖에 없다. 현재 N^2의 시간복잡도가 소요되는데,
    # 그래프를 탐색하는 2중 for문을 추가한다면 N^4이 소요된다. 그러나, 맥시멈이 20이니 최대 16만 밖에 안되므로 가능
    like_space = [[] for _ in range(5)]
    max_like_num = 0
    for r in range(N):
        for c in range(N):

            # 탐색 전, 해당 칸에 학생이 있는지 부터 확인하면 좀 더 효율적일듯.
            if graph[r][c] != 0 :
                continue

            # 상하좌우를 탐색해서 좋아하는 학생의 수를 체크하자.
            temp_like_num = 0
            temp_empty_num = 0
            for d in range(4):
                nr = r+dr[d]
                nc = c+dc[d]
                if 0<= nr < N and 0<= nc < N :
                    if graph[nr][nc] in like_students :
                        # 좋아하는 학생이 있으면  like num 증가
                        temp_like_num+=1
                    elif graph[nr][nc] == 0 :
                        # 빈칸이면 empty num 증가
                        temp_empty_num += 1
            # 좋아하는 학생을 다 체크 했으면, like_space에 추가해보자.
            like_space[temp_like_num].append([temp_empty_num,r,c])
            max_like_num = max(max_like_num,temp_like_num)
    # max_like_num으로 좋아하는 학생의 수를 체크해놓음.
    # 거기서 규칙 2,3을 한번에 만족하는 걸 찾으면 됨. 정렬을 이용해서
    # 1만을 만족하는건 like_space[max_like_num]이 한개인 경우임. 그래서 정렬을 쓰더라도 하나니까 그냥 1은 만족.
    # 2는 like_space[max_like_num]가 여러개인 경우인데, 이를 정렬하기 위해서 temp_empty_num을 첫 인덱스에 저장해둠.
    # 첫 인덱스 별로 정렬 하되 이것은 내림차순으로 동시에 행번호,열번호은 오름차순으로 정렬하자.
    sorted_like_space = sorted(like_space[max_like_num], key=lambda x: (-x[0], x[1], x[2]))
    best_space = sorted_like_space[0]
    graph[best_space[1]][best_space[2]] = student_num


results = 0
for r in range(N):
    for c in range(N):
        temp_like_num = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] in save_students[graph[r][c]]:
                    # 좋아하는 학생이 있으면  like num 증가
                    temp_like_num += 1
        if temp_like_num == 0 :
            results += 0
        else :
            results += 10**(temp_like_num-1)
print(results)
# import sys
# read = sys.stdin.readline
#
# def find_student():
#     # 무조건 1,1에서부터 시작해도 될듯.
#     visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
#     q = deque()
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if sit_maps[i][j] == 0 :
#                 start_y,start_x = i,j
#                 q.append([start_y,start_x])
#
#     best_positions = []
#     while q :
#         y,x = q.popleft()
#         visited[y][x] = 1
#         # 방문처리할때, 주변에 내가 선호하는 학생이 있는지 파악(1번)
#         love_count = 0
#         empty_count = 0
#         for j in range(4):
#             # 주변에 좋아하는 학생의 위치(ny,nx) 탐색
#             ny = y + dy[j]
#             nx = x + dx[j]
#             if ny < 1 or nx < 1 or ny >= N + 1 or nx >= N + 1:
#                 continue
#             else:
#                 if sit_maps[ny][nx] in loves:
#                     love_count += 1
#
#                 if sit_maps[ny][nx] == 0 :
#                     empty_count += 1
#
#                 # 학생이 앉아있지 않고, 방문하지 않았으면 등록
#                 if sit_maps[ny][nx] == 0 and visited[ny][nx] == 0 :
#                     q.append([ny,nx])
#                     # visited[ny][nx] = 1
#
#         best_positions.append([love_count,empty_count,y,x])
#
#     return best_positions
#
#
# N = int(read())
#
# students = {}
# for i in range(1,N*N+1):
#     students[i] = []
#
# # 몇번의 학생이 앉아있는지 확인하는 맵
# sit_maps = [[0 for _ in range(N+1)] for _ in range(N+1)]
#
# # 상 하 좌 우
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
# # 아마도 BFS로 탐색을 해야할듯.
# from collections import deque
#
# # 매 학생의 정보가 들어오면 바로바로 시작.
# students_lovers = dict()
# students_locations = dict()
# for n in range(N*N):
#     now_student,*loves = list(map(int,read().split()))
#     students_lovers[now_student] = loves
#     """
#     1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
#     2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
#     3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가
#        가장 작은 칸으로 자리를 정한다.
#     * 학생들은 상하좌우여야만 인접했다고 볼 수 있다.
#     """
#
#     # 상하좌우에 좋아하는 학생이 가장 많은 곳"들"을 찾자.
#     # 이를 위해 visited를 만들어야할듯.
#
#     best_positions = find_student()
#     best_positions.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
#     # print(now_student,best_positions)
#     *_,best_y,best_x = best_positions[0]
#
#     sit_maps[best_y][best_x] = now_student
#     # for k in range(N+1):
#     #     print(sit_maps[k])
#     # 가장 칸이 많은 곳"들"을 찾자.
#     students_locations[now_student]=[best_y,best_x]
#
# # for nn in range(N+1):
# #     print(sit_maps[nn])
# results = []
#
# for student in students_lovers.keys():
#     sy,sx = students_locations[student]
#     value_count = 0
#     for l in range(4):
#         nsy = sy+dy[l]
#         nsx = sx+dx[l]
#         if 1<= nsy < N+1 and 1<=nsx < N+1 :
#             if sit_maps[nsy][nsx] in students_lovers[student]:
#                 value_count += 1
#     if value_count == 0 :
#         results.append(0)
#     else :
#         results.append(10**(value_count-1))
#
# print(sum(results))