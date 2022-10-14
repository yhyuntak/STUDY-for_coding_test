"""

가장 처음에 주사위의 이동 방향은 동쪽이다.

주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다
주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.

주사위 아랫면 정수 A, 주사위 칸의 정수 B
A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
A = B인 경우 이동 방향에 변화는 없다.

(x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다.  -> bfs
이동할 수 있는 칸이란, 이웃한 곳들에서 정수 B가 있는 곳을 얘기한다.
점수는 B*C가 된다.

총 점수의 합은?

"""

R,C,K = map(int,input().split())
board = []
for _ in range(R):
    board.append(list(map(int,input().split())))

from collections import deque
dice = deque([deque([0,2,0]),deque([4,1,3]),deque([0,5,0]),deque([0,6,0])])
dice_d = 1

# 주사위의 항상 아랫면은 [1,1]이다.
# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def move_dice(dice_,d):
    # 상 우 하 좌 : 0,1,2,3
    if d == 2 : # 상 (0)
        temp = dice_[3][1]
        for i in range(3,0,-1):
            dice_[i][1] = dice_[i-1][1]
        dice_[0][1] = temp
    elif d== 0 : # 하 : 제일 아래(2)

        temp = dice_[0][1]
        for i in range(3):
            dice_[i][1] = dice_[i+1][1]
        dice_[3][1] = temp

    elif d == 3 : #  좌 : 왼쪽 면이 아래로.
        row = dice_[1]
        temp = row.popleft()
        row.append(dice_[3][1])
        dice_[3][1] = temp

    elif d == 1 : # 우 : 오른쪽 면이 아래로.
        row = dice_[1]
        temp = row.pop()
        row.appendleft(dice_[3][1])
        dice_[3][1] = temp

    return dice_

dice_r,dice_c = 0,0
results = 0
for k in range(1,K+1):
    # K번 구른다.

    # 주사위 위치 가보기.
    nr,nc = dice_r+dr[dice_d],dice_c+dc[dice_d]
    if not ( 0<= nr < R and 0<=nc < C): # 그래프를 벗어나면,
        # 이동 방향을 반대로 한다.
        dice_d = (dice_d+2)%4
    # 주사위 갈 곳 최종 갱신
    dice_r,dice_c = dice_r+dr[dice_d],dice_c+dc[dice_d]
    dice = move_dice(dice,dice_d) # 주사위도 굴리자.
    #
    # for _ in range(4):
    #     print(dice[_])
    # print()

    # 주사위의 아랫면 dice[3][1]과 주사위가 있는 칸 board[dice_r][dice_c]를 비교하자.
    A = dice[3][1]
    B = board[dice_r][dice_c]
    if A > B : # 시계 방향으로 90도 -> +1
        dice_d = (dice_d+1)%4
    elif A < B : # 반시계 -> -1
        dice_d = (dice_d-1)%4
    else : # 이동 방향에 변화가 없다.
        pass

    # 이제 BFS를 해서 board[dice_r][dice_c]에 있는 값과 같은 값을 갖는 칸의 수 C를 세자.

    q = deque()
    q.append([dice_r,dice_c])
    visit = [[0 for _ in range(C)] for _ in range(R)]
    visit[dice_r][dice_c] = 1
    C_cnt = 1
    while q :
        now_r,now_c = q.popleft()
        for i in range(4):
            nr,nc = now_r+dr[i],now_c+dc[i]
            if (0<=nr<R and 0<=nc<C) and visit[nr][nc] == 0 : # 경계선 안, 방문하지 않음.
                if board[nr][nc] == B :
                    C_cnt += 1
                    visit[nr][nc] = 1
                    q.append([nr,nc])

    results += B*C_cnt
print(results)
