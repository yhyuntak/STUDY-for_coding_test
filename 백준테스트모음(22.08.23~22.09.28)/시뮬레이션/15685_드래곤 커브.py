"""
드래곤 커브는 시작점 시작방향 세대로 구성

음 일단 아래방향이 +y 오른쪽방향이 +x 이다.

N 세대 커브는 N-1세대의 끝점을 기준으로 시계방향으로 90도 회전 시키는 느낌

문제는 사각형의 4개의 점이 모두 드래곤 커브의 일부인 사각형들의 개수를 구하는 것.
"""

def make_curve(x,y,d,g) :
    # 이거 패턴을 보니까 기존에 있던 방향들에 1씩 더해서 역으로 읽는 느낌인데?
    # 방향들을 저장할 필요가 있을 듯?
    directions = [d]
    # 초기 시작 위치에 +1 하기
    map_graph[y][x] += 1

    # 0세대로 인해 끝 값 초기화 하기
    end_y, end_x = y + dy[d], x + dx[d]
    map_graph[end_y][end_x] += 1
    # print(end_y,end_x)
    # 이제 1세대 이상은 for문으로 처리하기.
    for generation in range(1, g + 1):
        # directions을 거꾸로 읽으면서 +1 을 해서 end_y,end_x 를 갱신하기
        temp_directions = []
        for idx in range(len(directions)):
            temp_idx = -1 - idx
            temp_d = directions[temp_idx]
            temp_d = (temp_d + 1) % 4
            end_y, end_x = end_y + dy[temp_d], end_x + dx[temp_d]
            map_graph[end_y][end_x] += 1
            # print(directions)
            # print(temp_idx,directions[temp_idx],end_y,end_x)
            temp_directions.append(temp_d)
        directions += temp_directions

def check_ract(i, j):
    origin = map_graph[i][j]
    right = map_graph[i][j + 1]
    down = map_graph[i + 1][j]
    diag = map_graph[i + 1][j + 1]

    if origin >= 1 and right >= 1 and down >= 1 and diag >= 1:
        return 1
    else:
        return 0

N = int(input())

map_graph = [[0 for _ in range(101)] for _ in range(101)]
info_array = []

# 우 상 좌 하
dy = [0,-1,0,1]
dx = [1,0,-1,0]

# 음.. 이 문제를 해결하려면 g를 for문의 느낌으로 사용하는 어떤 function을 제작해야할 듯
for _ in range(N):
    x,y,d,g = map(int,input().split())
    make_curve(x,y,d,g)

# 100x100을 돌면서 사각형을 확인하는 것을 만들어야할듯
nums = 0
for i in range(100):
    for j in range(100):
        nums += check_ract(i,j)

print(nums)