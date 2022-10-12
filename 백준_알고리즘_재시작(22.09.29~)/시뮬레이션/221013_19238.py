"""

손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.
오늘 M명의 승객을 태우는 것이 목표

각 칸은 비어 있거나 벽이 놓

 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다

 특 정 위치로 이동할 때 항상 최단경로로만 이동
 M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다.

 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다.

  현재 위치에서 최단거리가 가장 짧은 승객을 고른다

  그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. (정렬)

  택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다.

  한 승객을 목적지로 성공적으로 이동시키면, 그" 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다." 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. -> 계속 연료 체크해야.?
   "승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다."

   모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.
"""

from collections import deque

N,M,fuel = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
taxi = list(map(int,input().split()))
taxi[0],taxi[1] = taxi[0]-1,taxi[1]-1
people = deque()
for _ in range(M):
    a,b,c,d = list(map(int,input().split()))
    people.append([a-1,b-1,c-1,d-1])

origin_visit = [[0 for _ in range(N)] for _ in range(N)]

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

from copy import  deepcopy
# 모든 손님을 이동시키자. 다 하면 종료하기 위해
while people :
    select_person = []
    # 먼저 택시와 승객의 거리를 측정.
    # BFS를 이용해서 현재 위치에서 모든 위치까지의 거리를 표현하면 좋을 듯.
    temp_visit = deepcopy(origin_visit)
    q = deque()
    q.append(taxi)
    while q :
        r,c = q.popleft()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if (0<=nr<N and 0<=nc<N) and board[nr][nc] == 0 and temp_visit[nr][nc] == 0 : # 경계선 안이고, 빈칸이고, 방문하지 않았으면
                if taxi[0] == nr and taxi[1] == nc :
                    continue
                temp_visit[nr][nc] = temp_visit[r][c] + 1
                q.append([nr,nc])
    # 그리고 나서 사람을 세서 가장 가까운 사람들을 찾자.
    min_val = 10e9
    min_people = []
    for person in people :
        if min_val > temp_visit[person[0]][person[1]] :
            min_val = temp_visit[person[0]][person[1]]
            min_people = []
        if temp_visit[person[0]][person[1]] == min_val :
            min_people.append(person)

    # 그런데 가까운 사람이 여러명일 수 있으니, 1) 행이 가장 작은, 2) 열이 가장 작은 으로 정렬
    min_people.sort(key=lambda x :(x[0],x[1]))
    select_person = min_people[0]

    """
    근데 현재 택시로부터 갈 수 없는 곳이 나타날 수 있다. 예를 들어 벽에 막혀 있다던지! 
    그러면 그 손님은 무슨짓을 해도 데려갈 수 없으니 그냥 끝내야한다. 
    """

    if min_val == 0 :
        if taxi[0]==select_person[0] and taxi[1] == select_person[1] :
            pass
        else :
            break

    # 선택한 사람을 제거해야함.
    temp_p = deque()
    while people :
        now_p = people.pop()
        if now_p == select_person :
            while temp_p :
                people.append(temp_p.pop())
            break
        else :
            temp_p.append(now_p)
    # 사람 목록에서 선택된 사람을 제거했다.

    # 이제 택시가 사람을 태웠다. 즉, 택시가 사람의 위치로 가야함.
    # 이제부터 연료가 사용됨. min_val 만큼.. 이제 조건을 파악하면서 가야됌.

    # print([select_person[0]+1,select_person[1]+1,select_person[2]+1,select_person[3]+1],min_val,taxi[0],taxi[1],fuel)

    taxi = [select_person[0],select_person[1]]
    fuel -= min_val
    if fuel <= 0 : # 사람한테 갔는데 0 이하가 되면 더이상 운행 불가임.
        break
    # 도착지의 정보는 우리가 알고 있음. 그러니까 bfs를 써야함. 왜냐하면 벽이 있을 수 있기 때문이다.
    # bfs를 일찍 종료하기 위해서, 해당 위치를 만나게 되면 종료하는 조건을 사용하자.
    temp_visit2 = deepcopy(origin_visit)
    q = deque()
    q.append(taxi)
    dont_stop = True
    while q and dont_stop:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < N and 0 <= nc < N) and board[nr][nc] == 0 and temp_visit2[nr][
                nc] == 0:  # 경계선 안이고, 빈칸이고, 방문하지 않았으면
                if taxi[0] == nr and taxi[1] == nc :
                    continue
                temp_visit2[nr][nc] = temp_visit2[r][c] + 1
                q.append([nr, nc])
                if nr == select_person[2] and nc == select_person[3] :
                    dont_stop = False
                    break

    taxi = [select_person[2],select_person[3]] # 택시가 도착했다.
    will_use_fuel = temp_visit2[taxi[0]][taxi[1]]

    # print([select_person[0]+1,select_person[1]+1,select_person[2]+1,select_person[3]+1],will_use_fuel,taxi[0],taxi[1],fuel)
    #
    # print("------")
    """
    근데 현재 택시로부터 갈 수 없는 곳이 나타날 수 있다. 예를 들어 벽에 막혀 있다던지! 
    그러면 그 손님은 무슨짓을 해도 도착지 까지 데려갈 수 없으니 그냥 끝내야한다. 
    """
    if will_use_fuel == 0 :
        break

    # 여기서 짚고가야할 것! 목적지에 도착 했을 때 연료가 0이 되도 종료되는게 아님!
    if fuel - will_use_fuel < 0 : # 출발지에서의 연료에 도착지까지의 연료를 뺐을 때, 음수가 나오면 갈 수 없는 곳이다.
        # 따라서 종료
        break
    else : # 0 이상일 땐 사용한 연료(will_use_fuel)의 2배를 충전시킨다.
        fuel -= will_use_fuel
        fuel += will_use_fuel*2

    # 선택했던 손님을 지우자.
    select_person = []
    # for _ in range(N):
    #     print(temp_visit2[_])
    # print(will_use_fuel,people,select_person)
    # print("----")

if len(people) == 0 and len(select_person) == 0 :
    print(fuel)
else :
    print(-1)