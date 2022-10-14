

from collections import deque

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
M_list = deque()
for _ in range(M):
    M_list.append(list(map(int,input().split())))

"""

상어는 그래프 중심에있고
번호가 연속되면 연속하는 구슬이라고 한다.

1) 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다. 
파괴되면 빈칸이 된다. 벽은 파괴되지 않는다. 벽 너머는 파괴가 가능하다. 

2) 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다. (그니까 자신 다음의 칸에서 땡겨오는 느낌)
 더이상 구슬이 이동하지 않을때까지 반복. 

3) 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생한다.

4) 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동한다

5) 3)-4)는 더 이상 폭발하는 구슬이 없을때까지 반복된다

6) , 구슬이 변화하는 단계가 된다. 연속하는 구슬은 하나의 그룹이라고 한다 (1개도 연속이라고 친다)
A,B로 변하는데, A는 그룹의 구슬의 개수, B는 그룹을 이루는 구술의 번호로. 바꿔주는데, A,B가 무조건 임.
만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다. -> 이게 무슨말인질 모르겠네?? 칸의 번호보다 구슬의 수가 더 크면 사라진다는 건가?  
"""

# 1 2 3 4 -> 상 하 좌 우 0 1 2 3으로 바꾸기.
dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]

temp = [2,4,1,3]
turn_list = []
for n in range(int((N-1)//2)):
    for i in range(4):
        for j in range((n+1)*2):
            if j == 0 and i == 0 : # 제일 첫번째는 무조건3임.
                turn_list.append(3)
            else :
                turn_list.append(temp[i])

def move_board(shark_r_,shark_c_,board_):

    for turn in range(N**2-1):
        shark_r_ = shark_r_ + dr[turn_list[turn]]
        shark_c_ = shark_c_ + dc[turn_list[turn]]
        if board_[shark_r_][shark_c_] != 0 : # 빈칸이 아니면 넘기자.
            continue
        else :
            # 빈칸이면, 다음칸부터 빈칸이 아닌 것을 찾자.
            nr_,nc_ = shark_r_ ,shark_c_ # 현재 위치를 일단 킵해놓자.
            for turn_2 in range(turn+1,N**2-1):
                nr_,nc_ = nr_+dr[turn_list[turn_2]],nc_+dc[turn_list[turn_2]]
                if board_[nr_][nc_] == 0 : # 빈칸이면 넘기자.
                    continue
                else : # 빈칸이 아닌 곳을 만나면 땡겨오자.
                    board_[shark_r_][shark_c_] = board_[nr_][nc_]
                    board_[nr_][nc_] = 0 # 땡겨온 곳을 0으로 만들자.
                    break # 그리고 종료시키고 다음 칸으로 넘어가자.

    return board_

one = 0
two = 0
three = 0

print_true = False
while M_list :

    if print_true :

        print("step : 0")
        for _ in range(N):
            print(board[_])
        print("-"*10)

    shark_r, shark_c = N // 2, N // 2
    """
    1) 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다. 
      파괴되면 빈칸이 된다. 벽은 파괴되지 않는다. 벽 너머는 파괴가 가능하다. 
    """
    d_i,s_i = M_list.popleft()
    for i in range(1,s_i+1):
        board[shark_r+dr[d_i]*i][shark_c+dc[d_i]*i] = 0

    """
    0은 빈칸이다.
    """

    if print_true:

        print("step : 1 - 블리자드~")
        for _ in range(N):
            print(board[_])
        print("-" * 10)

    """
    2) 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다. (그니까 자신 다음의 칸에서 땡겨오는 느낌)
      더이상 구슬이 이동하지 않을때까지 반복. -> 모든 칸을 다 확인해야함.
    """


    """
    3) 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생한다. -> 2,3,4를 한번에 묶어야 할지도 모른다.
    """
    while True:

        board = move_board(shark_r, shark_c, board)

        if print_true:

            print("step : 2 - 끌어오기~")
            for _ in range(N):
                print(board[_])
            print("-" * 10)


        nr,nc = shark_r,shark_c
        turn = 0
        group_list = []

        while turn < N**2-1 :

            # 현재 칸을 설정.
            nr += dr[turn_list[turn]]
            nc += dc[turn_list[turn]]
            crit = board[nr][nc]
            if crit == 0 : # 다 돌지 않더라도 빈칸을 만나면 종료시키자.
                break
            temp_group = [[nr,nc]]
            nnr , nnc = nr, nc
            # 빈칸이 아니라면, 현재칸 이후로 하나씩 살펴보기.
            for turn2 in range(turn+1,N**2-1):

                nnr += dr[turn_list[turn2]]
                nnc += dc[turn_list[turn2]]

                next_val = board[nnr][nnc]
                if next_val == 0 :
                    #다음칸이 빈칸이면 더 할 필요가 없다.
                    turn += 1 # 근데 crit_val 이 0이 되는 걸 찾아야하니까 turn을 1 증가.
                    if len(temp_group)>=4 :
                        group_list.append(temp_group)
                    break
                # print([nr,nc],crit,[nnr,nnc],next_val)
                if crit == next_val : # 값이 같으면 그룹에 넣어놓기.
                    temp_group.append([nnr,nnc])
                else : # 값이 다르면 초기화 하면서 점프 값 늘리기.

                    if len(temp_group)>=4 :
                        group_list.append(temp_group)
                    for i in range(turn+1,turn2):
                        nr += dr[turn_list[i]]
                        nc += dc[turn_list[i]]
                    turn = turn2
                    break
        if len(group_list) == 0 : # 근데 찾아진 그룹이 없으면 종료.
            break

        for group in group_list: # 점수 매기기.
            for r, c in group:
                if board[r][c] == 1 :
                    one += 1
                elif board[r][c] == 2 :
                    two += 1
                elif board[r][c] == 3 :
                    three += 1
                board[r][c] = 0

        if print_true:
            print("step : 3 - 폭발!")
            for _ in range(N):
                print(board[_])
            print("-" * 10)


    if print_true:
        print("step : 2,3의 결과")
        for _ in range(N):
            print(board[_])
        print("-" * 10)


    """
    5) , 구슬이 변화하는 단계가 된다. 연속하는 구슬은 하나의 그룹이라고 한다 (1개도 연속이라고 친다)
    A,B로 변하는데, A는 그룹의 구슬의 개수, B는 그룹을 이루는 구술의 번호로. 바꿔주는데, A,B가 무조건 임.
    만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다. -> 이게 무슨말인질 모르겠네?? 칸의 번호보다 구슬의 수가 더 크면 사라진다는 건가?
    """

    nr, nc = shark_r, shark_c
    turn = 0
    group_list = []

    while turn < N ** 2 - 1:

        # 현재 칸을 설정.
        nr += dr[turn_list[turn]]
        nc += dc[turn_list[turn]]
        crit = board[nr][nc]
        if crit == 0:  # 다 돌지 않더라도 빈칸을 만나면 종료시키자.
            break
        temp_group = [[nr, nc]]
        nnr, nnc = nr, nc
        # 빈칸이 아니라면, 현재칸 이후로 하나씩 살펴보기.
        for turn2 in range(turn + 1, N ** 2 - 1):

            nnr += dr[turn_list[turn2]]
            nnc += dc[turn_list[turn2]]

            next_val = board[nnr][nnc]
            if next_val == 0:
                # 다음칸이 빈칸이면 더 할 필요가 없다.
                turn += 1  # 근데 crit_val 이 0이 되는 걸 찾아야하니까 turn을 1 증가.
                if len(temp_group) >= 1:
                    group_list.append(temp_group)
                break
            # print([nr,nc],crit,[nnr,nnc],next_val)
            if crit == next_val:  # 값이 같으면 그룹에 넣어놓기.
                temp_group.append([nnr, nnc])
            else:  # 값이 다르면 초기화 하면서 점프 값 늘리기.
                if len(temp_group) >= 1:
                    group_list.append(temp_group)
                for i in range(turn + 1, turn2):
                    nr += dr[turn_list[i]]
                    nc += dc[turn_list[i]]
                turn = turn2
                break

    # 이제 2칸씩 뛰면서 그룹을 채워나가면 된다.
    group_list = deque(group_list)
    nr, nc = shark_r, shark_c
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(0,int(N**2)-1,2):
        if len(group_list) == 0 :
            break
        now_group = group_list.popleft()
        val = board[now_group[0][0]][now_group[0][1]]
        nr += dr[turn_list[i]]
        nc += dc[turn_list[i]]
        new_board[nr][nc] = len(now_group)
        nr += dr[turn_list[i+1]]
        nc += dc[turn_list[i+1]]
        new_board[nr][nc] = val

    board = new_board

    if print_true:

        print("step : 5")
        for _ in range(N):
            print(board[_])
        print("-" * 10)
print(one+2*two+3*three)