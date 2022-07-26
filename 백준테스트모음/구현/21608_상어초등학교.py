import sys
read = sys.stdin.readline

def find_student():
    # 무조건 1,1에서부터 시작해도 될듯.
    visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
    q = deque()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if sit_maps[i][j] == 0 :
                start_y,start_x = i,j
                q.append([start_y,start_x])

    best_positions = []
    while q :
        y,x = q.popleft()
        visited[y][x] = 1
        # 방문처리할때, 주변에 내가 선호하는 학생이 있는지 파악(1번)
        love_count = 0
        empty_count = 0
        for j in range(4):
            # 주변에 좋아하는 학생의 위치(ny,nx) 탐색
            ny = y + dy[j]
            nx = x + dx[j]
            if ny < 1 or nx < 1 or ny >= N + 1 or nx >= N + 1:
                continue
            else:
                if sit_maps[ny][nx] in loves:
                    love_count += 1

                if sit_maps[ny][nx] == 0 :
                    empty_count += 1

                # 학생이 앉아있지 않고, 방문하지 않았으면 등록
                if sit_maps[ny][nx] == 0 and visited[ny][nx] == 0 :
                    q.append([ny,nx])
                    # visited[ny][nx] = 1

        best_positions.append([love_count,empty_count,y,x])

    return best_positions


N = int(read())

students = {}
for i in range(1,N*N+1):
    students[i] = []

# 몇번의 학생이 앉아있는지 확인하는 맵
sit_maps = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 아마도 BFS로 탐색을 해야할듯.
from collections import deque

# 매 학생의 정보가 들어오면 바로바로 시작.
students_lovers = dict()
students_locations = dict()
for n in range(N*N):
    now_student,*loves = list(map(int,read().split()))
    students_lovers[now_student] = loves
    """
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 
       가장 작은 칸으로 자리를 정한다.
    * 학생들은 상하좌우여야만 인접했다고 볼 수 있다.
    """

    # 상하좌우에 좋아하는 학생이 가장 많은 곳"들"을 찾자.
    # 이를 위해 visited를 만들어야할듯.

    best_positions = find_student()
    best_positions.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    # print(now_student,best_positions)
    *_,best_y,best_x = best_positions[0]

    sit_maps[best_y][best_x] = now_student
    # for k in range(N+1):
    #     print(sit_maps[k])
    # 가장 칸이 많은 곳"들"을 찾자.
    students_locations[now_student]=[best_y,best_x]

# for nn in range(N+1):
#     print(sit_maps[nn])
results = []

for student in students_lovers.keys():
    sy,sx = students_locations[student]
    value_count = 0
    for l in range(4):
        nsy = sy+dy[l]
        nsx = sx+dx[l]
        if 1<= nsy < N+1 and 1<=nsx < N+1 :
            if sit_maps[nsy][nsx] in students_lovers[student]:
                value_count += 1
    if value_count == 0 :
        results.append(0)
    else :
        results.append(10**(value_count-1))

print(sum(results))