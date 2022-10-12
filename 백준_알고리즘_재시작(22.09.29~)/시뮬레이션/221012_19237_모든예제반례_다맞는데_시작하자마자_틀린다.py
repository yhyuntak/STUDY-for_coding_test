"""

1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

처음엔 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.

1초마다 모든 상어가 동시에 이동하고 그칸에 냄새를 뿌린다. 냄새는 상어가 k번 이동하면 사라진다.

아무 냄새 없는 칸으로 방향을. 여러개가 있으면 우선순위를 따른다.  그런 칸이 없으면 자신의 냄새가 있는 칸으로 방향을 잡는다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.
"""
import copy

N,M,K = map(int,input().split())
board = []
smell_board = [[[0,0] for _ in range(N)] for _ in range(N)] # 상어번호,냄새

for i in range(N):
    temp = list(map(int,input().split()))
    # 처음에 상어가 있는 곳엔 [상어번호,냄새 시간 K]를 저장해야한다.
    for j,t in enumerate(temp) :
        if t != 0 :
            smell_board[i][j] = [t,K]
    board.append(temp)

shark_directs = [0]
shark_directs += list(map(int,input().split()))

shark_d_board = [[] for _ in range(M+1)] # 1번부터 시작을 위해
# 위-1 아래-2 왼-3 오-4
for i in range(1,M+1):
    shark_d_board[i].append([])
    for j in range(4):
        a,b,c,d = map(int,input().split())
        shark_d_board[i].append([a,b,c,d])

# 위-1 아래-2 왼-3 오-4
dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]

time = 1

def move_shark(r,c,i,shark_n):
    board[r][c] = 0  # 상어가 있던 곳은 0으로
    next_shark_num = board[r + dr[i]][c + dc[i]]
    if next_shark_num == 0:
        board[r + dr[i]][c + dc[i]] = shark_n
        shark_directs[shark_n] = i  # 방향 업데이트
    else:
        if next_shark_num > shark_n:
            board[r + dr[i]][c + dc[i]] = shark_n
            shark_directs[next_shark_num] = 0  # 상어 죽이기
            shark_directs[shark_n] = i  # 방향 업데이트
        else:
            shark_directs[shark_n] = 0


while True : # 구현 시작

    """        
    1초마다 모든 상어가 동시에 이동하고 그칸에 냄새를 뿌린다. 냄새는 상어가 k번 이동하면 사라진다.
    """

    # 동시에 이동이므로 모든 상어가 움직이지 않은 상태의 맵에서 갈 수 있는 곳을 찾아야함.
    # 그럴려면 copy를 이용해서 현재 맵을 저장해두고 업데이트 하는 방식으로 가자.
    # temp_smells = copy.deepcopy(smell_board)
    # 모든 칸을 탐색하면서 상어가 존재할 경우, 이동을 고려하자.
    # 1번 상어부터 찾는거로 하자.
    for now_shark_num in range(1,M+1):
        temp_break = False
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0 :
                    continue
                elif board[r][c] == now_shark_num :
                    temp_break = True
                    break
            if temp_break :
                break
        now_shark_d = shark_directs[now_shark_num]
        if now_shark_d == 0 : # 이미 죽은 상어다
            continue
        now_priority = shark_d_board[now_shark_num][now_shark_d] # 현재 상어 번호의 방향의 우선순위

        # 4방향을 돌면서 갈 수 있는 "방향"들을 저장하자.
        save_ds = []
        for i in range(1,5):
            nr,nc = r+dr[i],c+dc[i]
            # 갈 수 있는 곳이란, 경계선 안의 냄새가 없는 [0,0]인 곳이다.
            if (0<=nr<N and 0<=nc<N) and smell_board[nr][nc] == [0,0] :
                save_ds.append(i)
            # 갈 수 없거나, 냄새가 있으면 continue

        # 저장된 방향이 1개면 방향을 저장하고 상어를 이동 시키자.
        if len(save_ds) == 1 :
            i = save_ds[0]
            move_shark(r,c,i,now_shark_num)
        # 여러개면 우선순위에 따라서 저장.
        elif len(save_ds) > 1 :
            for i in now_priority :
                if i in save_ds :
                    move_shark(r, c, i, now_shark_num)
                    break
        else :
            # 갈 수 있는 칸이 없으면 자신의 냄새가 있는 곳으로 방향을 잡자.
            # 이것도 가능한 칸이 여러개일 수 있다.
            # 4방향을 돌면서 냄새가 있는 "방향"들을 저장하자.
            save_ds_ = []
            for i in range(1,5):
                # 한 방향으로 최대 N번까지 갈 수 있다.
                for nn in range(1,N):
                    nr,nc = r+dr[i]*nn,c+dc[i]*nn
                    if not (0<=nr<N and 0<=nc<N) :
                        break
                    else :
                        if smell_board[nr][nc][0] == now_shark_num : # 탐색하는 칸에 냄새가 자신의 번호이면 추가
                            save_ds_.append(i)
                            # 하나라도 찾았으면 더이상 안찾아도 된다.
                            break
            # 저장된 방향이 1개면 방향을 저장하고 상어를 이동 시키자.
            if len(save_ds_) == 1:
                i = save_ds_[0]
                move_shark(r, c, i, now_shark_num)
            # 여러개면 우선순위에 따라서 저장.
            elif len(save_ds_) > 1:
                for i in now_priority:
                    if i in save_ds_:
                        move_shark(r, c, i, now_shark_num)
                        break

    # 1번만 남으면 끝내야함.
    temp = copy.deepcopy(shark_directs)
    temp[1] = 0
    if sum(temp) == 0 :
        print(time)
        break

    # 각 칸에 남은 상어로 번호와 냄새를 업데이트하면서 원래 있던 냄새는 K를 -1 해줘야한다.
    for r in range(N):
        for c in range(N):
            # 냄새가 있는 곳엔 상어가 가지 않았음.
            if smell_board[r][c] != [0,0]: # 냄새가 있는 곳 중
                if smell_board[r][c][-1] == 1 : # 이제 냄새가 지워질 건데 1인 곳은 [0,0]으로 초기화
                    smell_board[r][c] = [0,0]
                else :
                    smell_board[r][c][-1] -= 1 # 다른 곳은 그냥 1만 빼주기.

            if board[r][c] != 0 : # 상어가 있는 곳은
                # 번호 냄새로 업데이트
                smell_board[r][c] = [board[r][c],K]

    # #
    # print("shark map")
    # for _ in range(N):
    #     print(board[_])
    # print()
    # print("shark 방향 :",shark_directs)
    # print()
    # print("냄새 맵")
    # for _ in range(N):
    #     print(smell_board[_])
    # print("-------------------")

    # 여기로 넘어온다는건 다른 상어가 남은 채로 한바퀴 더돌려고하는 거임.
    if time == 1000 :
        print(-1)
        break

    time +=1
