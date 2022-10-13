import copy

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))


times = 1
max_val = -1
def dfs(b,t):
    if t == 6 :
        global  max_val
        for r in range(N):
            for c in range(N):
                max_val = max(b[r][c],max_val)
        return

    # 상 하 좌 우 0 1 2 3 로 움직임.
    for d in range(4):
        temp_board = copy.deepcopy(b)
        # 이동을 표현하자.
        if d == 0 : # 위로 기울이기.

            # 모든 column 확인
            for c in range(N):
                # 제일 위(r=1) 에 있는거부터 확인.
                # 확인해야할 위치 저장
                check_r = 0
                for r in range(1,N):
                    # 현재 칸이 빈칸이면 continue
                    if temp_board[r][c] == 0 :
                        continue
                    # 확인하는 칸이 빈칸이면 채우기.
                    if temp_board[check_r][c] == 0 :
                        temp_board[check_r][c] += temp_board[r][c]
                        temp_board[r][c] = 0
                        # 이건 check_r이 증가할 필요가 없다.
                    elif temp_board[check_r][c] == temp_board[r][c] : # 같은 수라면 더해주기.
                        temp_board[check_r][c] *= 2
                        temp_board[r][c] = 0
                        check_r += 1 # 한번 합쳐진건 다시 합쳐질 수 없으니 +1
                    else : # 0이 아니고 같은수가 아니라면, 아래에 쌓아야한다.
                        check_r += 1
                        temp_board[check_r][c] = temp_board[r][c]
                        if check_r != r :
                            temp_board[r][c] = 0
        elif d == 1:  # 아래로 기울이기.

            # 모든 column 확인
            for c in range(N):
                # 확인해야할 위치 저장
                check_r = N - 1
                # 제일 아래의 -1(r=N-2) 에 있는거부터 확인.
                for r in range(N-2,-1,-1):
                    # 현재 칸이 빈칸이면 continue
                    if temp_board[r][c] == 0:
                        continue
                        # 확인하는 칸이 빈칸이면 채우기.
                    if temp_board[check_r][c] == 0:
                        temp_board[check_r][c] += temp_board[r][c]
                        temp_board[r][c] = 0
                        # 이건 check_r이 증가할 필요가 없다.
                    elif temp_board[check_r][c] == temp_board[r][c]:  # 같은 수라면 더해주기.
                        temp_board[check_r][c] *= 2
                        temp_board[r][c] = 0
                        check_r -= 1  # 한번 합쳐진건 다시 합쳐질 수 없으니 +1
                    else:  # 0이 아니고 같은수가 아니라면, 아래에 쌓아야한다.
                        check_r -= 1
                        temp_board[check_r][c] = temp_board[r][c]
                        if check_r != r :
                            temp_board[r][c] = 0
        elif d == 2:  # 왼쪽으로 기울이기.

            # 모든 row 확인
            for r in range(N):
                # 확인해야할 위치 저장
                check_c = 0
                # 제일 왼쪽의 -1(c=1) 에 있는거부터 확인.
                for c in range(1,N):
                    # 현재 칸이 빈칸이면 continue
                    if temp_board[r][c] == 0:
                        continue
                        # 확인하는 칸이 빈칸이면 채우기.
                    if temp_board[r][check_c] == 0:
                        temp_board[r][check_c] += temp_board[r][c]
                        temp_board[r][c] = 0
                        # 이건 check_c이 증가할 필요가 없다.
                    elif temp_board[r][check_c] == temp_board[r][c]:  # 같은 수라면 더해주기.
                        temp_board[r][check_c] *= 2
                        temp_board[r][c] = 0
                        check_c += 1  # 한번 합쳐진건 다시 합쳐질 수 없으니 +1
                    else:  # 0이 아니고 같은수가 아니라면, 아래에 쌓아야한다.
                        check_c += 1
                        temp_board[r][check_c] = temp_board[r][c]
                        if check_c != c :
                            temp_board[r][c] = 0
        elif d == 3:  # 오른쪽으로 기울이기.

            # 모든 row 확인
            for r in range(N):
                # 확인해야할 위치 저장
                check_c = N - 1
                # 제일 오른쪽의 -1(c=N-2) 에 있는거부터 확인.
                for c in range(N-2,-1,-1):
                    # 현재 칸이 빈칸이면 continue
                    if temp_board[r][c] == 0:
                        continue
                        # 확인하는 칸이 빈칸이면 채우기.
                    if temp_board[r][check_c] == 0:
                        temp_board[r][check_c] += temp_board[r][c]
                        temp_board[r][c] = 0
                        # 이건 check_c이 증가할 필요가 없다.
                    elif temp_board[r][check_c] == temp_board[r][c]:  # 같은 수라면 더해주기.
                        temp_board[r][check_c] *= 2
                        temp_board[r][c] = 0
                        check_c -= 1  # 한번 합쳐진건 다시 합쳐질 수 없으니 +1
                    else:  # 0이 아니고 같은수가 아니라면, 아래에 쌓아야한다.
                        check_c -= 1
                        temp_board[r][check_c] = temp_board[r][c]
                        if check_c != c :
                            temp_board[r][c] = 0

        # print("{}번째의 {}방향으로 기울이기".format(t,d))
        # for _ in range(N):
        #     print(temp_board[_])
        dfs(temp_board,t+1)


dfs(board,times)

print(max_val)




# import copy
# # import sys
# # sys.setrecursionlimit(10**7)
#
# N = int(input())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int,input().split())))
#
# # 상하좌우 마다 액션을 구현해야함.
#
# def move(board,dir):
#     if dir == 0 : # 상
#         for c in range(N): # 첫번째 col~마지막 col까지 훑기
#             max_top = 0 # 가장 위의 인덱스를 얘기함.
#             # 이제 가장 위부터 아래로 for문을 돌리기
#             for r in range(1,N):
#                 if board[r][c] != 0 : # 보드에 값이 있으면
#                     temp = board[r][c]
#                     board[r][c] = 0 # 일단 현재 위치의 값을 0으로 만들기
#                     if board[max_top][c] == 0 : # 만약 가장 위의 값이 0이면
#                         board[max_top][c] = temp # 지금 값으로 채워주기
#                     elif board[max_top][c] == temp : # 만약 같은 값이 있으면
#                         board[max_top][c] = temp * 2 # 더해준다.
#                         #그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 위 인덱스의 값을 1 키우자.
#                         max_top += 1
#                     else : # 만약 비어있지않고, 같은 값도 아니라면,
#                         # 쌓음으로써 max도 1이 커져야한다.
#                         max_top += 1
#                         board[max_top][c] = temp # 그냥 아래에 쌓아두기.
#
#
#     elif dir == 1 : # 하
#         for c in range(N):  # 첫번째 col~마지막 col까지 훑기
#             max_bottom = N - 1  # 가장 아래의 인덱스를 얘기함.
#             # 이제 가장 아래부터 위로 for문을 돌리기
#             for r in range(N-2, -1,-1):
#                 if board[r][c] != 0:  # 보드에 값이 있으면
#                     temp = board[r][c]
#                     board[r][c] = 0  # 일단 현재 위치의 값을 0으로 만들기
#                     if board[max_bottom][c] == 0:  # 만약 가장 아래의 값이 0이면
#                         board[max_bottom][c] = temp  # 지금 값으로 채워주기
#                     elif board[max_bottom][c] == temp:  # 만약 같은 값이 있으면
#                         board[max_bottom][c] = temp * 2  # 더해준다.
#                         # 그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 아래 인덱스의 값을 1 줄이자.
#                         max_bottom -= 1
#                     else:  # 만약 비어있지않고, 같은 값도 아니라면,
#                         # 쌓음으로써 max도 1이 작아져야한다.
#                         max_bottom -= 1
#                         board[max_bottom][c] = temp  # 그냥 위에 쌓아두기.
#
#
#     elif dir == 2 : # 좌
#         for r in range(N): # 첫번째 row~마지막 row까지 훑기
#             max_left = 0 # 가장 왼쪽 인덱스를 얘기함.
#             # 이제 가장 왼쪽의 바로 옆부터 for문을 돌리기
#             for c in range(1,N):
#                 if board[r][c] != 0 : # 보드에 값이 있으면
#                     temp = board[r][c]
#                     board[r][c] = 0 # 일단 현재 위치의 값을 0으로 만들기
#                     if board[r][max_left] == 0 : # 만약 가장 왼쪽 값이 0이면
#                         board[r][max_left] = temp # 지금 값으로 채워주기
#                     elif board[r][max_left] == temp : # 만약 같은 값이 있으면
#                         board[r][max_left] = temp * 2 # 더해준다.
#                         #그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 왼쪽 인덱스의 값을 1 키우자.
#                         max_left += 1
#                     else : # 만약 비어있지않고, 같은 값도 아니라면,
#                         # 쌓음으로써 max도 1이 커져야한다.
#                         max_left += 1
#                         board[r][max_left] = temp # 그냥 옆에 쌓아두기.
#
#     else : # 우
#         for r in range(N): # 첫번째 row~마지막 row까지 훑기
#             max_right = N-1 # 가장 오른쪽 인덱스를 얘기함.
#             # 이제 가장 오른쪽의 바로 옆부터 for문을 돌리기
#             for c in range(N-2,-1,-1):
#                 if board[r][c] != 0 : # 보드에 값이 있으면
#                     temp = board[r][c]
#                     board[r][c] = 0 # 일단 현재 위치의 값을 0으로 만들기
#                     if board[r][max_right] == 0 : # 만약 가장 오른쪽 값이 0이면
#                         board[r][max_right] = temp # 지금 값으로 채워주기
#                     elif board[r][max_right] == temp : # 만약 같은 값이 있으면
#                         board[r][max_right] = temp * 2 # 더해준다.
#                         #그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 오른쪽 인덱스의 값을 1 줄이자.
#                         max_right -= 1
#                     else : # 만약 비어있지않고, 같은 값도 아니라면,
#                         # 쌓음으로써 max도 1이 줄어야한다.
#                         max_right -= 1
#                         board[r][max_right] = temp # 그냥 옆에 쌓아두기.
#
#
#
#     return board
#
#
# # 일단 DFS를 해야할 것 같음.
# def dfs(board,cnt):
#
#     # 5번을 돌리면 cnt가 5가 되어 들어올 것임.
#     # 그럼 끝내면서 최대 값을 찾아야할거 같음
#     if cnt == 5 :
#         global max_val
#         for r in range(N):
#             for c in range(N):
#                 max_val = max(max_val,board[r][c])
#         return
#
#     for direction in range(4):
#         # 상 : 0 하 : 1 좌 : 2 우 : 3 로 구현해볼까
#         temp_board = move(copy.deepcopy(board),direction)
#         dfs(temp_board,cnt+1)
#
#
# max_val = 0
# dfs(graph,0)
#
# print(max_val)