# 다 벽이다
# 뱀은 처음에 0,0에 위치하고, 길이는 1이다.
# 오른쪽으로 향한다 처음엔
import copy

N = int(input())
K = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
for k in range(K): # 사과의 위치
    temp =list(map(int,input().split()))
    # 행,렬 로 주어짐
    graph[temp[0]-1][temp[1]-1] = 1
L = int(input())

direction_list = dict()
for l in range(L):
    temp =list(input().split())
    # 행,렬 로 주어짐
    direction_list[int(temp[0])]= temp[1]

# 우 하 좌 상 -> 0 1 2 3
dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque

x,y= 0,0
graph[y][x] = -1

snake_body = deque([[y,x]])
snake_direction = 0

def turn(snake_direction,direction):
    if direction == "L":
        snake_direction -= 1
    else:
        snake_direction += 1
    return snake_direction % 4

time_constant = 0
while True :

    time_constant += 1
    # 시뮬레이션
    # 1. 무조건 방향으로 머리가 한칸 움직인다.

    y += dy[snake_direction]
    x += dx[snake_direction]

    # 4. 벽에 닿거나 자기몸에 닿으면 끝
    if y < 0 or x < 0 or y >= N or x >= N or graph[y][x] == -1:
        # 게임의 총 시간은?
        print(time_constant)
        break
    else :
        # 3. 사과가 없으면 길이는 늘어나지 않으니 꼬리가 한칸 땡겨져야한다.
        if graph[y][x] != 1:
            # 헤드만 추가하고 꼬리 자르기
            temp_y,temp_x = snake_body.popleft()
            graph[temp_y][temp_x] = 0

        graph[y][x] = -1
        snake_body.append([y,x])

        # x초가 끝난 후 방향 돌리기
        if time_constant in direction_list.keys():
            snake_direction = turn(snake_direction,direction_list[time_constant])


