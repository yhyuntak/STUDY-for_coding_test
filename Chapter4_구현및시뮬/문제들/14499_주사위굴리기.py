
import copy
from collections import deque
import sys
read = sys.stdin.readline

def dice_move(dice,d):
    if d == 1 : # 동
        temp = dice[1]
        t = temp.pop()
        temp = [dice[3]] + temp
        dice[1] = temp
        dice[3] = t
    elif d == 2 : # 서
        temp = dice[1]
        t = temp.pop(0)
        temp.append(dice[3])
        dice[1] = temp
        dice[3] = t
    elif d == 3 : # 북
        t = dice[0]
        dice[0] = dice[1][1]
        dice[1][1] = dice[2]
        dice[2] = dice[3]
        dice[3] = t
    elif d == 4 : # 남
        t = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1][1]
        dice[1][1] = dice[0]
        dice[0] = t
    return dice

N,M,y,x,K = map(int,read().split())
graph = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    temp = list(map(int,read().split()))
    graph[n] = temp

# 동 서 북 남
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

direct_list = list(map(int,read().split()))
dice = [0,[0,0,0],0,0]
results = []
for d in direct_list:
    # 주사위가 갈 곳의 위치
    ny = y + dy[d]
    nx = x + dx[d]
    if 0<=nx<M and 0<=ny<N :
        # 주사위를 굴린다
        dice = dice_move(dice,d)
        # 바닥이 0 이면
        if graph[ny][nx] == 0 :
            # 주사위의 수를 복사해서 넣자
            graph[ny][nx] = dice[3]
        # 0이 아니면
        else :
            # 바닥의 수를 주사위에 넣고 바닥을 0으로 만들자
            dice[3] = copy.deepcopy(graph[ny][nx])
            graph[ny][nx] = 0
        y = ny
        x = nx
        print(dice[1][1])
    #     results.append(dice[1][1])
    # else :
    #     print("h")
    #     results.append(-1)
    #     continue
