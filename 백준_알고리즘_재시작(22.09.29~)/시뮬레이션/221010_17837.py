"""

하나의 말 위에 다른 말을 올릴 수 있다

체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.

턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다.

말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다.

턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.

체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때, 게임이 종료되는 턴의 번호를 구해보자.

"""

N,K = map(int,input().split())
board = []
for _ in range(N) :
    board.append(list(map(int,input().split())))

from collections import deque
horses_map = [[deque() for _ in range(N)] for _ in range(N)]
horses = [[] for _ in range(K+1)]
# horses = {}
for k in range(1,K+1):
    r,c,d = map(int,input().split())
    # horses[(r,c)] = [[k,d]]
    horses_map[r-1][c-1].append([k,d])
    horses[k] = [r-1,c-1]
# 우 좌 상 하
dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

game = 1
end_val = True
# 맵 색깔 0 : 흰색 1 : 빨간색 2 : 파란색
while game <= 1000 and end_val : #for game in range(1,5):#1002) :
    # 이 루프를 다 돌고 끝나면 게임이 끝나지 않는 것임.

    # print("{}th start".format(game))
    # for _ in range(N):
    #     print(horses_map[_])
    # print()

    # 이제 말이 움직이는 것을 구현하자.
    # 말은 1번부터 K번까지 순서대로 하나씩 움직인다.
    for now_num in range(1,K+1):
        # n번말의 위치를 불러오자.
        horse_r,horses_c = horses[now_num]
        # 해당 위치에 쌓여있는 말의 정보를 모두 가져오자.
        stack_horse = horses_map[horse_r][horses_c]
        """
        쌓인 것을 정의하자.
        왼쪽에 있을수록 위에 쌓인것이고, 오른쪽이 아래에 깔린 것이다.
        """
        # for문을 통해서 현재 움직일 말의 번호가 나타날때까지 popleft()를 해서 현재 말의 위에 쌓인 것들도 다 뽑아서 움직일 준비.
        temp_stacks = []
        for i in range(len(stack_horse)):
            temp_stacks.append(stack_horse.popleft())
            if temp_stacks[i][0] == now_num : # 지금 선택된 말이 현재 찾는 말이면 스탑
                break
        # 같이 움직일 말들의 번호와 방향의 정보를 얻었다.
        # 이제 움직인다.

        # 먼저 방향으로 말을 움직이자.
        # temp_stacks의 마지막 list는 현재의 말의 정보다.
        next_h_r , next_h_c = horse_r + dr[temp_stacks[-1][1]],horses_c+dc[temp_stacks[-1][1]]

        # print("before : ",temp_stacks,next_h_r,next_h_c)

        # 파랑과 그래프를 벗어날 경우 방향을 바꿔서 다음 칸을 봐야하므로 먼저 이 조건으로 방향을 바꿀지부터 결정해야하네.
        if next_h_r < 0 or next_h_r >= N or next_h_c < 0 or next_h_c >= N or board[next_h_r][
            next_h_c] == 2:  # 그래프를 벗어나거나, 파랑일 경우
            # 방향을 뒤집자.

            direct = temp_stacks[-1][1]
            # print("before d:", temp_stacks[-1][1])
            if direct == 1 :
                direct = 2
            elif direct == 2 :
                direct = 1
            elif direct == 3 :
                direct = 4
            elif direct == 4 :
                direct = 3
            temp_stacks[-1][1] = direct
            # print("after d:",temp_stacks[-1][1])

        # 만약 위 조건문에 안걸렸으면, 그냥 평소처럼 한칸 전진하면 됌.
        next_h_r , next_h_c = horse_r + dr[temp_stacks[-1][1]],horses_c+dc[temp_stacks[-1][1]]
        # print("after : ",temp_stacks,next_h_r,next_h_c)


        # 먼저 하얀색을 구현하자.
        if 0<=next_h_r < N and 0 <= next_h_c < N :
            # 그래프 내에 있으면 하양,빨강,파랑을 고려하자.
            if board[next_h_r][next_h_c] == 0 : # 하양이라면
                # 원래 있던 체스 말 위에 그대로 쌓자 (appendleft)
                for stack in temp_stacks :
                    change_num = stack[0]
                    horses[change_num] = [next_h_r,next_h_c]
                horses_map[next_h_r][next_h_c] = deque(temp_stacks+list(horses_map[next_h_r][next_h_c]))
            elif board[next_h_r][next_h_c] == 1 : # 빨강이라면
                # 이동하면서 순서를 반대로 뒤집어서 위에 쌓자 (appendleft)
                for stack in temp_stacks :
                    change_num = stack[0]
                    horses[change_num] =  [next_h_r,next_h_c]
                horses_map[next_h_r][next_h_c] = deque(list(reversed(temp_stacks))+list(horses_map[next_h_r][next_h_c]))
            elif board[next_h_r][next_h_c] == 2 : # 파랑이면
                # 현재 위치에 그대로 저장.
                horses_map[horse_r][horses_c] = deque(temp_stacks+list(horses_map[horse_r][horses_c]))

        elif next_h_r < 0 or next_h_r >= N or next_h_c < 0 or next_h_c >= N : # 그래프를 또 벗어날 경우
                # 현재 위치에 그대로 저장.
                horses_map[horse_r][horses_c] = deque(temp_stacks+list(horses_map[horse_r][horses_c]))
                continue
        if len(horses_map[next_h_r][next_h_c]) >= 4 :
            end_val = False
        #
        # for _ in range(N):
        #     print(horses_map[_])
        # print("-"*20)
    game += 1
if game <= 1000 : print(game-1)
else : print(-1)