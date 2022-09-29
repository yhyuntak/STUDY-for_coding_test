"""220906"""
"""
인구이동은 하루동안 진행되고, 더이상 안될때까지 반복
1. 국경선을 공유하는 두 나라의 인구차가 L이상 ,R이하라면 국경선 오픈
2. 열려야하는 국경선을 모두 오픈하고 이동시작
3. 연결된 나라들을 연합이라함.
4. 연합을 이루는 각 칸의 인구수는 연합의 인구수/연합의 칸의수 이고, 소수점은 버리기
5. 연합 해체후 국경선 닫기
"""

N,L,R= map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
# 상 우 하 좌
dr = [0,1,0,-1]
dc = [-1,0,1,0]

# 2000일 보다 작거나 같다.
days = 1
union_change = False
change_graph = [[False for _ in range(N)] for _ in range(N)]
limit_day = 2000

while days <= limit_day :

    # 하루동안 모든 나라들을 돌면서 오픈해야되는지 말아야하는지를 파악.
    # 즉, 서로 L이상,R이하인 것들을 어떤 array에 넣어두면 좋을듯?
    # 매일매일 이뤄지는 것임.
    union_array = []

    """ 나라 돌기 """
    # 이 문제는 deque를 써야한다. 왜냐하면 하루에 모든 연합이 동시 다발적으로 인구이동이 이뤄져야 하기때문
    from collections import deque
    # 이 문제는 visited가 필수다. 왜냐하면, 방문한 나라는 다시 방문할 일이 없어야하기 때문이다.
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):

            # 임시 연합을 만들자.
            temp_union = []

            # 일단 현재의 나라가 방문했는지 안했는지부터 파악
            if visited[r][c] == 1 :
                continue

            elif visited[r][c] == 0 and change_graph[r][c] == union_change :
                # 방문하지 않았다면, deque에 넣고 방문 처리를 하자.
                q.append([r,c])
                visited[r][c] = 1
                temp_union.append([r,c])
                # 그리고 BFS를 이용해서 연합을 만들자.
                while q :
                    now_r , now_c = q.popleft()
                    # 지금 나라에서 상 우 하 좌에 있는 나라들을 보고 방문을 안한곳을 찾자.
                    for i in range(4):
                        nr = now_r+dr[i]
                        nc = now_c+dc[i]

                        if 0<= nr < N and 0<= nc < N and visited[nr][nc] == 0:
                        # L<= <=R이면 연합으로 쳐야하므로 deque에 넣자. 방문처리하는 것도 잊지 말자.
                            if L <= abs(graph[now_r][now_c]-graph[nr][nc]) <= R :
                                q.append([nr,nc])
                                visited[nr][nc] = 1
                                temp_union.append([nr,nc])
                # 이 else문이 끝난다면, 하나의 연합을 찾는 일이 끝나는 것이므로
                # 그 연합을 union_array에 저장할 생각을 하자.
            # 조건문이 끝났으니 만약 2개 이상의 국가가 묶인 임시 연합이  발생했다면, union_array에 저장하자.
            if len(temp_union)>= 2 :
                union_array.append(temp_union)
    # print(union_array)
    """연합마다 인구수 통합하기"""
    # 만약 union_array가 비어있지 않다면, 즉 연합이 존재한다면 인구 이동을 하고
    # 비어있다면, 이 while문은 종료해야한다.
    if len(union_array) != 0 :
        # 이제 연합마다 인구수 통합 대작전을 펼치자.
        for union in union_array:
            # 연합을 이루는 각 칸의 인구수는 연합의 인구수/연합의 칸의수 이고, 소수점은 버리기
            num_of_union = len(union)
            union_peoples = 0
            for ur,uc in union :
                union_peoples += graph[ur][uc]
            divide_peoples = union_peoples // num_of_union
            for ur, uc in union:
                graph[ur][uc] = divide_peoples

    else :

        break


    days +=1

print(days-1)

"""2208"""

# import math
# import sys
# read =sys.stdin.readline
# from fractions import Fraction
# from collections import deque
#
# def solution(N,L,R,graph):
#
#     # 상 하 좌 우
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#
#     # 아 이문제 하루에 다 이동하고 다음날에 다 이동하고 이런느낌이네;
#     # 매일 매일 모든 연합을 미리 지정해야함!
#     # 그니까 BFS로 매일 연합이 되는 것들을 찾고 저장한다.
#     # 근데 저장된 연합이 없다면 그대로 알고리즘 종료. 이런느낌으로 가야할듯.
#
#     union_exist = True
#
#     # 인구이동의 날짜를 세는 count변수 생성
#     days = 0
#
#     while union_exist :
#
#         union_space = []
#         visited = [[0 for _ in range(N)] for _ in range(N)]
#
#         # 일단 2중 for문으로 모든 곳을 돌아봐야함.
#         for r in range(N):
#             for c in range(N):
#
#                 # 여기서 중요한건, 이미 연합이 되어서 visited 처리가 된 곳은 다시 둘러볼 필요가 없다는 것.
#
#                 if visited[r][c] == 1 :
#                     continue
#
#                 # 현재 위치가 탐색되지 않았다면 이곳을 시작으로 BFS를 진행해서 연합을 찾아보자.
#
#                 q = deque()
#                 q.append([r,c])
#
#                 # 현재 위치에서의 연합을 저장할 곳을 임시로 생성
#                 temp_neighbor = [[r,c]]
#
#                 while q :
#                     # 현재 위치 뽑기
#                     now_r,now_c = q.popleft()
#                     # 방문 처리
#                     visited[now_r][now_c] = 1
#
#                     # 현재 위치를 기점으로 상하좌우를 탐색하자
#                     for i in range(4):
#                         search_r = now_r + dy[i]
#                         search_c = now_c + dx[i]
#
#                         # 확인할 곳이 일단 정상적인 범위인지 체크하고, 방문한 곳이 아닌지도 함께 체크
#                         if (0<= search_r < N and 0<= search_c < N) and visited[search_r][search_c] == 0:
#                             # 국경선이 열린게 하나라도 있어야지 인구이동을 할 수 있다.
#                             # now와 search의 차이를 확인하자.
#
#                             # L R 범위에 들어간다면
#                             if L<= abs(graph[search_r][search_c] - graph[now_r][now_c])<=R :
#
#                                 # 현재 위치의 연합국가로 설정
#                                 temp_neighbor.append([search_r,search_c])
#                                 # 설정함과 동시에 다시 해당 국가의 주변에 가능한 곳이 있는지 파악하기 위해
#                                 # queue에 넣고, 다시 방문하지 않기 위해 visited 처리.
#                                 q.append([search_r,search_c])
#                                 visited[search_r][search_c] = 1
#
#                 if len(temp_neighbor) > 1 :
#                     union_space.append(temp_neighbor)
#
#         # 이제 연합들의 묶음이 완성되었으니, 각 연합들 마다 인구 이동을 진행하자.
#         # 저장된 연합이 없으면 종료
#         if len(union_space) == 0:
#             union_exist = False
#         # 연합이 있으면 인구이동을 진행하자.
#         else :
#             #먼저 days를 올리자.
#             days +=1
#             # 연합을 뽑아서 인구이동 하자.
#             for union in union_space :
#
#                 # 인구를 모두 더하기
#                 people = 0
#                 for union_r,union_c in union :
#                     people += graph[union_r][union_c]
#
#                 # 인구의 총 합에 근접국의 수를 나누자.
#                 people = math.floor(Fraction(people,len(union)))
#                 # 분배하자.
#                 for union_r,union_c in union :
#                     graph[union_r][union_c] = people
#
#     return days
#
#
# N,L,R = map(int,read().split())
# graph = []
#
# for n in range(N):
#     graph.append(list(map(int,read().split())))
#
# print(solution(N,L,R,graph))
