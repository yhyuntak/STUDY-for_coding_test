import sys
read = sys.stdin.readline

N,M = map(int,read().split())
robot_y,robot_x,robot_state =  map(int,read().split())
graph = []
for i in range(N):
    graph.append(list(map(int,read().split())))

dx = [0,1,0,-1] # 북0 동1 남2 서3
dy = [-1,0,1,0] # 북0 동1 남2 서3

total = 1
graph[robot_y][robot_x] = 2
move_back = True

move_back_cnt = 0

while True :

    robot_state -= 1
    if robot_state < 0 :
        robot_state = 3

    # 왼쪽방향의 구역을 표현하기
    ny = robot_y + dy[robot_state]
    nx = robot_x + dx[robot_state]

    if graph[ny][nx] == 0 : # 청소가 안되어있다면
        graph[ny][nx] = 2 # 방문 처리
        # 로봇 위치 갱신
        robot_y = ny
        robot_x = nx
        total += 1
        move_back_cnt = 0
        continue
    else : # 벽이거나 이미 청소한 곳이라면 패스하고 회전하러가자
        move_back_cnt += 1

    # 4곳을 다 봤더니 갈 곳이 없다. 그럼 뒤로가자
    if move_back_cnt == 4 :

        ny = robot_y - dy[robot_state]
        nx = robot_x - dx[robot_state]

        if graph[ny][nx] == 2 : # 후진하기 위해 뒤를 봤더니 갈 수 있다면
            robot_y = ny
            robot_x = nx
            move_back_cnt = 0
        else : #아니라면 뒤로가자
            break

print(total)