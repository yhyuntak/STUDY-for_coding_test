"""
220912
"""
import copy

"""
각 행과 열의 끝들을 다 연결함.

비구름은 무조건 [N,0],[N,1],[N-1,0],[N-1,1] 에 사각형의 모양으로 생성됨.

8방향임 1부터 순서대로 좌 좌상 상 우상 우 우하 하 좌하

명령은 다음과 같음
1. 모든 구름이 di방향으로 si만큼 이동
2. 바구니에 물이 1씩 증가
3. 구름이 사라짐
4. 물이 증가한 칸에 물복사버그 마법을 시전, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 
바구니의 물이 증가( 각 칸마다 적용하는듯)? 단, 이동과 다르게 경계를 넘어가면 그건 거리가 1이 아님
5. 바구니에 물의 양이 2 이상인 모든 칸에 구름이 생성되고 물의 양이 2가 줄어듬. 이 때, 구름이 생기는 칸은 구름이 사라진 칸이 아님.

M번의 이동이 끝난 후, 바구니에 들어있는 물의 양의 합은??

"""

N,M = map(int,input().split())
cloud_map = []
for _ in range(N):
    cloud_map.append(list(map(int,input().split())))
# 8방향임 1부터 순서대로 좌 좌상 상 우상 우 우하 하 좌하
# index 0은 사용하지 않을것이니 99로
dr = [99,0,-1,-1,-1,0,1,1,1]
dc = [99,-1,-1,0,1,1,1,0,-1]

# 0. 먼저 구름부터 생성
now_clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

original_moved_graph = [[0 for _ in range(N)] for _ in range(N)]

# 이동 횟수 M번만큼 for문을 돌리자
for m in range(M):
    d_i , s_i = map(int,input().split())

    # 1. 구름 이동 구현
    # 2. 구름이 있는 바구니에 물이 1씩 증가는 효율성을 위해 이동과 같이 구현하자.
    moved_clouds = copy.deepcopy(now_clouds)
    moved_graph = copy.deepcopy(original_moved_graph)
    for i in range(len(moved_clouds)):
        temp_r,temp_c = moved_clouds[i]
        moved_r,moved_c = (temp_r+dr[d_i]*s_i)%N,(temp_c+dc[d_i]*s_i)%N
        moved_clouds[i] = [moved_r,moved_c]
        cloud_map[moved_r][moved_c] += 1
        moved_graph[moved_r][moved_c] = 1
    # 3. 구름이 사라짐.

    # 4. 물이 증가한 칸에 물복사버그 마법을 시전, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
    #   바구니의 물이 증가( 각 칸마다 적용하는듯)? 단, 이동과 다르게 경계를 넘어가면 그건 거리가 1이 아님
    # moved_clouds가 물이 증가한 칸을 나타내니, 그것들의 대각선 방향을 체크하면 될듯.
    # 체크하기위한 dr,dc를 또 만들어야할듯 -> 그러지말고 기존의 dr,dc의 2배수들이 대각선을 표현하니 그것을 이용
    for j in range(len(moved_clouds)):
        now_r,now_c = moved_clouds[j]
        for k in range(1,5):
            diag_r,diag_c = now_r+dr[k*2],now_c+dc[k*2]
            if 0<= diag_r < N and 0<= diag_c < N : # 단, 이동과 다르게 경계를 넘어가면 그건 거리가 1이 아님
                if cloud_map[diag_r][diag_c] > 0 : # 바구니에 물이 있으면,
                    # now 바구니에 물이 증가.
                    cloud_map[now_r][now_c] += 1

    # 5. 바구니에 물의 양이 2 이상인 모든 칸에 구름이 생성되고 물의 양이 2가 줄어듬.
    # 이 때, 구름이 생기는 칸은 구름이 사라진 칸이 아님.
    # 완전탐색을해서 구름을 지정해야할듯.
    now_clouds = []
    for rr in range(N):
        for cc in range(N):

            if moved_graph[rr][cc] == 0 and cloud_map[rr][cc] >= 2 :
                now_clouds.append([rr,cc])
                cloud_map[rr][cc] -= 2
            # if cloud_map[rr][cc] >= 2 :
            #     now_clouds.append([rr,cc])
            #     cloud_map[rr][cc] -= 2


# 출력 단
results = 0
for n in range(N):
    results += sum(cloud_map[n])
print(results)





"""
220801
"""

#
# """
# 기본 정보 설정
# """
#
# # NxN칸, M번 이동
# N,M = map(int,input().split())
# water_graph = []
# for _ in range(N):
#     water_graph.append(list(map(int,input().split())))
# move_info = []
# for m in range(M):
#     move_info.append(list(map(int,input().split())))
#
# # 좌 좌상 상 우상 우 우하 하 좌하
# # 1번부터 표현하자.
# dc = [0,-1,-1,0,1,1,1,0,-1]
# dr = [0,0,-1,-1,-1,0,1,1,1]
#
# """
# M번만큼 이동하는 for문 생성
# """
#
# """
# 1. 구름이 d방향으로 s만큼 이동
# 2. 구름 4칸은 비가내려서 바구니에 저장된 물의 양이 1 증가한다.
# 3. 구름은 사라진다
# 4. 2에서 물이 증가한 칸들에서 물복사버그 마법을 사용해서 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
# 해당 칸의 물이 증가한다.아, 이동은 1<->N이 됨을 명심하고, 이 물버그는 1<->N이 되지 않는다.
# 5. 바구니에 저장된 물의양이 2이상인 모든 칸에 구름 생성되고 물의 양이 2줄어듬.
# 이때 구름이 생기는 곳은 3에서 구름이 사라진 칸이 아니어야한다.
# """
#
# # 위 말그대로 따라하자.
# # 일단 구름 visted와 list를 초기화하자.
# cloud_visited = [[0 for _ in range(N)] for _ in range(N)]
# cloud_list = [[N-1,0],[N-1,1],[N-1-1,0],[N-1-1,1]]
#
# for m,[direction,distance] in enumerate(move_info):
#
#     # 구름이 움직이는걸 구현하자. cloud_list를 가지고와서 for문 돌면서 진행할수밖에!
#     # 이동된 구름으로 인해 물이 증가한 곳에서 물복사버그를 해야하므로, moving cloud의 정보를 저장하는 list도 만들어야한다.
#     moving_cloud_list = []
#     for cloud_r,cloud_c in cloud_list :
#         # 움직인 구름의 위치를 표현해보자.
#         # %를 잘 활요해야겠다 진짜
#         moving_cloud_r = (cloud_r + dr[direction]*distance) %N
#         moving_cloud_c = (cloud_c + dc[direction]*distance) %N
#         # 그럼 이제 구름의 이동이 끝났다.
#         # 그럼 비가 내려서 물의 양이 1 증가되도록 하자.
#         water_graph[moving_cloud_r][moving_cloud_c] += 1
#
#         # 움직인 구름의 정보 즉, 물이 추가된 위치의 정보를 가져가자.
#         moving_cloud_list.append([moving_cloud_r,moving_cloud_c])
#         # 구름은 사라지지만 이 움직인 위치는 다시 구름이 생성되면 안되니 visited에 추가
#         cloud_visited[moving_cloud_r][moving_cloud_c] += 1
#
#
#     # 좋아 이렇게되면 이제 구름생성 -> 비내리기 -> 물증가 까지 완료했다.
#     # 이제 마지막으로 물 복사버그만 완성하면 된다.
#     # 내용은 다음과 같다.
#     """
#     4. 2에서 물이 증가한 칸들에서 물복사버그 마법을 사용해서 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
#        해당 칸의 물이 증가한다.아, 이동은 1<->N이 됨을 명심하고, 이 물버그는 1<->N이 되지 않는다.
#     """
#     # 비가 내려서 물이 증가한 칸들! 즉, moving_cloud_r/c를 아직 사용해야한다.
#     # 각각을 또 확인해주면서.. 근데 이걸 또 for문을 돌면 너무 비효율적인것 같으니, 위에 이미 사용하고있는 것에 첨가하자. -> 아니야 이거 따로해야되는거야
#     # 왜냐하면 구름이 물주면서 물의 양의 정보가 바뀔 수 있기 때문에!!
#
#     # 움직인 구름들의 위치를 for문으로 가져오자.
#     for water_r,water_c in moving_cloud_list:
#
#         # 비가내린 곳의 대각선 방향들의 dc,dr의 idx는 2,4,6,8이다
#         # 먼저 복사될 물의 양을 저장하자.
#         amount_water = 0
#         # temp_copy_list = []
#         # moving_cloud_r/c에서 대각선 방향들을 체크하자.
#         for dd in range(2,9,2):
#             diagonal_r = water_r + dr[dd]
#             diagonal_c = water_c + dc[dd]
#             #여기서 이 대각선 요소들은 0<= 위치 < N을 만족해야만 된다.
#             if 0<=diagonal_r<N and 0<=diagonal_c<N :
#                 # 해당 위치들에 나중에 물을 추가를 할꺼니까 리스트를 저장해둔다. -> 문제를 잘못 봄
#                 # temp_copy_list.append([diagonal_r,diagonal_c])
#                 # 대각선 요소가 합당할 때, 그 위치에 있는 바구니속 물의 양이 1이상이면 amount_water를 카운트한다.
#                 if water_graph[diagonal_r][diagonal_c] >= 1:
#                     amount_water+=1
#         # 이제 물 복사 버그를 하기 위해 물의 양도 측정되었고, 복사할 위치들도 저장됬으니 -> 취소,
#         # 복사를 시작하자.
#         # 주변에 그럴만한게 없었다면 amount_water가 0이므로 걱정하지말자.
#         # for copy_r,copy_c in temp_copy_list:
#         water_graph[water_r][water_c] += amount_water
#
#     # 이제 마지막으로 구름을 만들자
#     """
#     5. 바구니에 저장된 물의양이 2이상인 모든 칸에 구름 생성되고 물의 양이 2줄어듬.
#     """
#     # 물의 양이 2 이상인 모든 칸에 구름을 생성한다. 이때 물의 양을 2 줄이고, 이전에 구름이 생성됬던 곳은 배제한다.
#     # 임시로 새로 만들어질 구름 리스트를 저장하는 리스트를 생성
#     temp_cloud_list = []
#     # 여기는 water map을 확인할 수 밖에 없다.
#     for r in range(N):
#         for c in range(N):
#             now_water = water_graph[r][c]
#             # 물의 양이 2이상인지 확인하고, cloud_list에 없으면 여기는 구름이 생성될 곳이라고 판단하자.
#             if now_water >= 2 and cloud_visited[r][c] == 0:
#                 # 확인 됬으면, 물의 양을 줄이자.
#                 water_graph[r][c] -= 2
#                 # 임시 구름 리스트에도 추가하자.
#                 temp_cloud_list.append([r,c])
#             elif cloud_visited[r][c] == 1:
#                 # 아래에서 이걸 아예 처음으로 초기화하지말고,
#                 # 이 조건문을 사용해서 1인걸 0으로 만들자.
#                 # 왜냐하면 r,c가 한번 훑고 지나가면 다시 훑을일이 없기 때문이다.
#                 cloud_visited[r][c] = 0
#     # 구름 리스트를 업데이트하자
#     cloud_list = temp_cloud_list
#
# # 다 더하면 끝
# results = 0
# for n in range(N):
#     results += sum(water_graph[n])
#
# print(results)