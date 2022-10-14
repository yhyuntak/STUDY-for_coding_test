"""

1)  모든 온풍기에서 바람이 한 번 나옴
2) 온도 조절
3) 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4) 초콜릿 하나 먹음
5) 조사하는 모든 칸의 온도가 K이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고 아니면 1부터 다시 시작

온풍기의 방향은  그 방향은 오른쪽, 왼쪽, 위, 아래 중 하나.

어떤 칸에 같은 온풍기에서 나온 바람이 여러 번 도착한다고 해도 온도는 여러번 상승하지 않는다.

온풍기가 2대 이상 있을 수도 있다. 이 경우 각각의 온풍기에 의해서 상승한 온도를 모두 합한 값이 해당 칸의 상승한 온도이다.

구사과가 먹은 초콜릿의 개수를 출력한다.

"""



# 일단 온풍기부터 하고 2번을 살펴보자.
R,C,K = map(int,input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
robots = []

# 1-우 0 , 2-좌 1, 3-위 2, 4-하3
dr = [0,0,-1,1]
dc = [1,-1,0,0]
research_list = []
for r in range(R):
    """
    0: 빈 칸 -1 
    1: 방향이 오른쪽인 온풍기가 있음 0
    2: 방향이 왼쪽인 온풍기가 있음 1
    3: 방향이 위인 온풍기가 있음 2
    4: 방향이 아래인 온풍기가 있음 3
    5: 온도를 조사해야 하는 칸 4
    """
    temp = list(map(int,input().split()))
    for c,t in enumerate(temp):
        t -= 1
        if 0<= t < 4 :
            robots.append([r,c,t])
        elif t == 4 :
            research_list.append([r,c])

    # board.append(temp)

num_wall = int(input())
walls = [[[-1,-1] for _ in range(C)] for _ in range(R)]
for _ in range(num_wall):
    r,c,t = list(map(int,input().split()))
    if t == 0 :
        walls[r-1][c-1][0] = 0
    elif t == 1 :
        walls[r-1][c-1][1] = 1

from collections import deque

def wind(arr,robot,wall):
    # 먼저 로봇을 선택하자
    for robo in robot :
        robo_r,robo_c,robo_d = robo

        if robo_d == 0 : # 우
            region = deque()
            region.append([robo_r,robo_c+1])
            arr[robo_r][robo_c+1] += 5
            temper = 4
            wind_visit = [[0 for _ in range(C)] for _ in range(R)]
            # robo_c+1 ~ C-1 까지 바람이 퍼짐
            # 근데 현재 위치에서 다음 위치에 값을 넣을 것이니까  C-1로 써야함.
            for cc in range(robo_c+1,C-1):
                if temper <= 0 : # 온도가 0 이하가 되면 더이상 할필요가 없다.
                    break
                # region에 들어있는 칸만큼 영역을 체크하자.
                len_region = len(region)
                for reg in range(len_region):
                    now_r,now_c = region.popleft()

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr1,nc1 = now_r-1,now_c+1

                    # [r-1,c+1] , [r,c+1],  [r+1,c+1]에 바람을 -1로 줄 수 있다.
                    # 먼저 [r-1,c+1]에 줄 수 있는지 봐보자. -> r-1,c 와 r,c 사이에 벽, r-1,c / r-1,c+1 사이의 벽이 없어야한다.
                    if 0<=nr1<R and 0<=nc1<C :
                        if walls[now_r][now_c][0] != 0 and walls[now_r-1][now_c][1] != 1 and wind_visit[now_r-1][now_c+1] == 0 : # 벽이 없고 아직 방문 안했으면
                            arr[now_r-1][now_c+1] += temper
                            wind_visit[now_r - 1][now_c + 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r-1,now_c+1])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr2,nc2 = now_r,now_c+1
                    if 0<=nr2<R and 0<=nc2<C :
                        # [r,c+1]에 줄 수 있는지 보자.
                        if walls[now_r][now_c][1] != 1 and wind_visit[now_r][now_c+1] == 0 :
                            arr[now_r][now_c+1] += temper
                            wind_visit[now_r][now_c + 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r,now_c+1])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr3,nc3 = now_r+1,now_c+1
                    if 0<=nr3<R and 0<=nc3<C :
                        # [r+1,c+1]에 줄 수 있는지 봐보자. -> r+1,c,0 과 r+1,c,1 이
                        if walls[now_r+1][now_c][0] != 0 and walls[now_r+1][now_c][1] != 1 and wind_visit[now_r+1][now_c+1] == 0 : # 벽이 없고 아직 방문 안했으면
                            arr[now_r+1][now_c+1] += temper
                            wind_visit[now_r + 1][now_c + 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r+1,now_c+1])
                temper -= 1

        elif robo_d == 1 : # 좌
            region = deque()
            if not (0<=robo_r<R and 0<= robo_c -1 < C) :
                continue
            region.append([robo_r,robo_c-1])
            arr[robo_r][robo_c-1] += 5
            temper = 4
            wind_visit = [[0 for _ in range(C)] for _ in range(R)]
            # robo_c-1 ~ 1 까지 바람이 퍼짐
            for cc in range(robo_c-1,0,-1):
                if temper <= 0 : # 온도가 0 이하가 되면 더이상 할필요가 없다.
                    break
                # region에 들어있는 칸만큼 영역을 체크하자.
                len_region = len(region)
                for reg in range(len_region):
                    now_r,now_c = region.popleft()

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr1,nc1 = now_r-1,now_c-1
                    # [r-1,c-1] , [r,c-1],  [r+1,c-1]에 바람을 -1로 줄 수 있다.
                    # 먼저 [r-1,c-1]에 줄 수 있는지 봐보자. -> r-1,c 와 r,c 사이에 벽, r-1,c / r-1,c+1 사이의 벽이 없어야한다.
                    if 0<=nr1<R and 0<=nc1<C :
                        if walls[now_r][now_c][0] !=0 and walls[now_r-1][now_c-1][1] !=1 and wind_visit[now_r-1][now_c-1] == 0 : # 벽이 없고 아직 방문 안했으면
                            arr[now_r-1][now_c-1] += temper
                            wind_visit[now_r - 1][now_c - 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r-1,now_c-1])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr2,nc2 = now_r,now_c-1
                    if 0<=nr2<R and 0<=nc2<C :
                        # [r,c+1]에 줄 수 있는지 보자.
                        if walls[now_r][now_c-1][1] !=1 and wind_visit[now_r][now_c-1] == 0 :
                            arr[now_r][now_c-1] += temper
                            wind_visit[now_r][now_c - 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r,now_c-1])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr3,nc3 = now_r+1,now_c-1
                    if 0<=nr3<R and 0<=nc3<C :
                        # [r+1,c+1]에 줄 수 있는지 봐보자. -> r+1,c,0 과 r+1,c,1 이
                        if walls[now_r+1][now_c][0] !=0 and walls[now_r+1][now_c-1][1] !=1 and wind_visit[now_r+1][now_c-1] == 0 : # 벽이 없고 아직 방문 안했으면
                            arr[now_r+1][now_c-1] += temper
                            wind_visit[now_r + 1][now_c - 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r+1,now_c-1])

                temper -= 1

        elif robo_d == 2 : # 상
            region = deque()
            if not (0<=robo_r-1<R and 0<= robo_c < C) :
                continue
            region.append([robo_r-1,robo_c])
            arr[robo_r-1][robo_c] += 5
            temper = 4
            wind_visit = [[0 for _ in range(C)] for _ in range(R)]
            # robo_r-1 ~ 0 까지 바람이 퍼짐
            # 근데 현재 위치에서 다음 위치에 값을 넣을 것이니까  C-1로 써야함.
            for rr in range(robo_r-1,0,-1):
                if temper <= 0 : # 온도가 0 이하가 되면 더이상 할필요가 없다.
                    break
                # region에 들어있는 칸만큼 영역을 체크하자.
                len_region = len(region)
                for reg in range(len_region):
                    now_r,now_c = region.popleft()

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr1,nc1 = now_r-1,now_c-1
                    if 0<=nr1<R and 0<=nc1<C :
                        if walls[now_r][now_c-1][0] != 0 and walls[now_r][now_c-1][1] != 1 and wind_visit[now_r-1][now_c-1] == 0 : # 벽이 없고 아직 방문 안했으면
                            arr[now_r-1][now_c-1] += temper
                            wind_visit[now_r - 1][now_c - 1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([now_r-1,now_c-1])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr2,nc2 = now_r-1,now_c
                    if 0<=nr2<R and 0<=nc2<C :
                        if walls[now_r][now_c][0] != 0 and wind_visit[nr2][nc2] == 0 :
                            arr[nr2][nc2] += temper
                            wind_visit[nr2][nc2] = 1
                            # 줬으면 region에 추가하기.
                            region.append([nr2,nc2])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr3,nc3 = now_r-1,now_c+1
                    if 0<=nr3<R and 0<=nc3<C :
                        if walls[now_r][now_c][1] != 1 and walls[now_r][now_c+1][0] != 0 and wind_visit[nr3][nc3] == 0 : # 벽이 없고 아직 방문 안했으면
                            arr[nr3][nc3] += temper
                            wind_visit[nr3][nc3] = 1
                            # 줬으면 region에 추가하기.
                            region.append([nr3,nc3])
                temper -= 1
        elif robo_d == 3:  # 상
            region = deque()
            if not (0 <= robo_r + 1 < R and 0 <= robo_c < C):
                continue
            region.append([robo_r + 1, robo_c])
            arr[robo_r + 1][robo_c] += 5
            temper = 4
            wind_visit = [[0 for _ in range(C)] for _ in range(R)]
            # robo_r-1 ~ 0 까지 바람이 퍼짐
            # 근데 현재 위치에서 다음 위치에 값을 넣을 것이니까  C-1로 써야함.
            for rr in range(robo_r+1,R-1):
                if temper <= 0:  # 온도가 0 이하가 되면 더이상 할필요가 없다.
                    break
                # region에 들어있는 칸만큼 영역을 체크하자.
                len_region = len(region)
                for reg in range(len_region):
                    now_r, now_c = region.popleft()

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr1, nc1 = now_r + 1, now_c - 1
                    if 0 <= nr1 < R and 0 <= nc1 < C:
                        if walls[now_r+1][now_c - 1][0] !=  0 and walls[now_r][now_c - 1][1] !=  1 and \
                                wind_visit[nr1][nc1] == 0:  # 벽이 없고 아직 방문 안했으면
                            arr[nr1][nc1] += temper
                            wind_visit[nr1][nc1] = 1
                            # 줬으면 region에 추가하기.
                            region.append([nr1, nc1])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr2, nc2 = now_r + 1, now_c
                    if 0 <= nr2 < R and 0 <= nc2 < C:
                        if walls[now_r+1][now_c][0] != 0 and wind_visit[nr2][nc2] == 0:
                            arr[nr2][nc2] += temper
                            wind_visit[nr2][nc2] = 1
                            # 줬으면 region에 추가하기.
                            region.append([nr2, nc2])

                    # 만들어질 곳이 경계를 넘어가는지 확인하자.
                    nr3, nc3 = now_r + 1, now_c + 1
                    if 0 <= nr3 < R and 0 <= nc3 < C:
                        if walls[now_r][now_c][1] != 1 and walls[now_r+1][now_c + 1][0] !=  0 and wind_visit[nr3][
                            nc3] == 0:  # 벽이 없고 아직 방문 안했으면
                            arr[nr3][nc3] += temper
                            wind_visit[nr3][nc3] = 1
                            # 줬으면 region에 추가하기.
                            region.append([nr3, nc3])
                temper -= 1

    return arr


def calc_val(arr,save_arr, r_, c_, nr_, nc_,val_) :

    if save_arr[r_][c_] > save_arr[nr_][nc_]:
        arr[r_][c_] -= val_
        arr[nr_][nc_] += val_
        if arr[r_][c_] < 0:
            arr[r_][c_] = 0
        if arr[nr_][nc_] < 0:
            arr[nr_][nc_] = 0

    elif save_arr[r_][c_] < save_arr[nr_][nc_] :
        arr[r_][c_] += val_
        arr[nr_][nc_] -= val_
        if arr[r_][c_] < 0:
            arr[r_][c_] = 0
        if arr[nr_][nc_] < 0:
            arr[nr_][nc_] = 0

    return arr

import copy
choco = 1
print_bool = False
while choco < 101 :

    # 1) 온풍기 작전
    # 먼저 온풍기가 바라보는 방향으로 한칸 간 곳이 시작이다.
    # 항상 5가 시작이다.
    # 더해주는 개념으로 가야한다.
    # 방향에 따라 row와 col로 퍼지는 방향이 다르다.
    board = wind(board,robots,walls)


    if print_bool :
        for _ in range(R):
            print(walls[_])
        print()
        for _ in range(R):
            print(board[_])
        print("-"*10)


    save_board = copy.deepcopy(board)
    visit_ = [[0 for _ in range(C)] for _ in range(R)]
    # save로 확인해서 board를 조작하자.
    for r in range(R):
        for c in range(C):
            # 상하좌우 2칸씩 모두 체크해야함;;
            visit_[r][c] = 1
            for i in [0,3]:
                nr,nc = r+dr[i],c+dc[i]
                if 0<=nr<R and 0<=nc<C :
                    # int(현재칸-다음칸)/4) 로 작은 칸엔 + 큰 칸은 - 해주면 된다.
                    val = abs(save_board[r][c]-save_board[nr][nc])//4
                    # 이때, 방향에 따라서 벽이 .. 존재할 수 있다..
                    if i == 0 : #우
                        # 현재칸의 세로
                        if walls[r][c][1] != 1 :
                            board = calc_val(board,save_board,r,c,nr,nc,val)
                    elif i == 1 : # 좌
                        # 다음 칸의 세로
                        if walls[nr][nc][1] != 1 :
                            board = calc_val(board,save_board,r,c,nr,nc,val)

                    elif i == 2 : # 상
                        # 현재 칸의 가로
                        if walls[r][c][0] != 0 :
                            board = calc_val(board,save_board,r,c,nr,nc,val)

                    elif i== 3 : # 하
                        # 다음 칸의 가로
                        if walls[nr][nc][0] != 0 :
                            board = calc_val(board,save_board,r,c,nr,nc,val)

    if print_bool :
        for _ in range(R):
            print(board[_])
        print("-"*10)

    for r in range(R):
        if r == 0 or r == R-1:
            for c in range(C):
                if board[r][c] == 0 :
                    continue
                else :
                    board[r][c] -= 1
        else :
            for c in [0,C-1]:
                if board[r][c] == 0 :
                    continue
                else :
                    board[r][c] -= 1

    if print_bool :
        for _ in range(R):
            print(board[_])
        print("-"*10)


    temper_ok = 0
    val_ok = 0
    # for r in range(R):
    #     for c in range(C):
    for r,c in research_list :
        val_ok += 1
        if board[r][c] >= K :
            temper_ok += 1
    if temper_ok == val_ok :
        break

    choco += 1
# 5) 조사하는 모든 칸의 온도가 K이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고 아니면 1부터 다시 시작

print(choco)