import copy
# import sys
# sys.setrecursionlimit(10**7)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 상하좌우 마다 액션을 구현해야함.

def move(board,dir):
    if dir == 0 : # 상
        for c in range(N): # 첫번째 col~마지막 col까지 훑기
            max_top = 0 # 가장 위의 인덱스를 얘기함.
            # 이제 가장 위부터 아래로 for문을 돌리기
            for r in range(1,N):
                if board[r][c] != 0 : # 보드에 값이 있으면
                    temp = board[r][c]
                    board[r][c] = 0 # 일단 현재 위치의 값을 0으로 만들기
                    if board[max_top][c] == 0 : # 만약 가장 위의 값이 0이면
                        board[max_top][c] = temp # 지금 값으로 채워주기
                    elif board[max_top][c] == temp : # 만약 같은 값이 있으면
                        board[max_top][c] = temp * 2 # 더해준다.
                        #그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 위 인덱스의 값을 1 키우자.
                        max_top += 1
                    else : # 만약 비어있지않고, 같은 값도 아니라면,
                        # 쌓음으로써 max도 1이 커져야한다.
                        max_top += 1
                        board[max_top][c] = temp # 그냥 아래에 쌓아두기.


    elif dir == 1 : # 하
        for c in range(N):  # 첫번째 col~마지막 col까지 훑기
            max_bottom = N - 1  # 가장 아래의 인덱스를 얘기함.
            # 이제 가장 아래부터 위로 for문을 돌리기
            for r in range(N-2, -1,-1):
                if board[r][c] != 0:  # 보드에 값이 있으면
                    temp = board[r][c]
                    board[r][c] = 0  # 일단 현재 위치의 값을 0으로 만들기
                    if board[max_bottom][c] == 0:  # 만약 가장 아래의 값이 0이면
                        board[max_bottom][c] = temp  # 지금 값으로 채워주기
                    elif board[max_bottom][c] == temp:  # 만약 같은 값이 있으면
                        board[max_bottom][c] = temp * 2  # 더해준다.
                        # 그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 아래 인덱스의 값을 1 줄이자.
                        max_bottom -= 1
                    else:  # 만약 비어있지않고, 같은 값도 아니라면,
                        # 쌓음으로써 max도 1이 작아져야한다.
                        max_bottom -= 1
                        board[max_bottom][c] = temp  # 그냥 위에 쌓아두기.


    elif dir == 2 : # 좌
        for r in range(N): # 첫번째 row~마지막 row까지 훑기
            max_left = 0 # 가장 왼쪽 인덱스를 얘기함.
            # 이제 가장 왼쪽의 바로 옆부터 for문을 돌리기
            for c in range(1,N):
                if board[r][c] != 0 : # 보드에 값이 있으면
                    temp = board[r][c]
                    board[r][c] = 0 # 일단 현재 위치의 값을 0으로 만들기
                    if board[r][max_left] == 0 : # 만약 가장 왼쪽 값이 0이면
                        board[r][max_left] = temp # 지금 값으로 채워주기
                    elif board[r][max_left] == temp : # 만약 같은 값이 있으면
                        board[r][max_left] = temp * 2 # 더해준다.
                        #그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 왼쪽 인덱스의 값을 1 키우자.
                        max_left += 1
                    else : # 만약 비어있지않고, 같은 값도 아니라면,
                        # 쌓음으로써 max도 1이 커져야한다.
                        max_left += 1
                        board[r][max_left] = temp # 그냥 옆에 쌓아두기.

    else : # 우
        for r in range(N): # 첫번째 row~마지막 row까지 훑기
            max_right = N-1 # 가장 오른쪽 인덱스를 얘기함.
            # 이제 가장 오른쪽의 바로 옆부터 for문을 돌리기
            for c in range(N-2,-1,-1):
                if board[r][c] != 0 : # 보드에 값이 있으면
                    temp = board[r][c]
                    board[r][c] = 0 # 일단 현재 위치의 값을 0으로 만들기
                    if board[r][max_right] == 0 : # 만약 가장 오른쪽 값이 0이면
                        board[r][max_right] = temp # 지금 값으로 채워주기
                    elif board[r][max_right] == temp : # 만약 같은 값이 있으면
                        board[r][max_right] = temp * 2 # 더해준다.
                        #그런데 한번의 이동에서 더해진 값이 존재하면 더이상 또 더해지면 안되므로, 가장 오른쪽 인덱스의 값을 1 줄이자.
                        max_right -= 1
                    else : # 만약 비어있지않고, 같은 값도 아니라면,
                        # 쌓음으로써 max도 1이 줄어야한다.
                        max_right -= 1
                        board[r][max_right] = temp # 그냥 옆에 쌓아두기.



    return board


# 일단 DFS를 해야할 것 같음.
def dfs(board,cnt):

    # 5번을 돌리면 cnt가 5가 되어 들어올 것임.
    # 그럼 끝내면서 최대 값을 찾아야할거 같음
    if cnt == 5 :
        global max_val
        for r in range(N):
            for c in range(N):
                max_val = max(max_val,board[r][c])
        return

    for direction in range(4):
        # 상 : 0 하 : 1 좌 : 2 우 : 3 로 구현해볼까
        temp_board = move(copy.deepcopy(board),direction)
        dfs(temp_board,cnt+1)


max_val = 0
dfs(graph,0)

print(max_val)