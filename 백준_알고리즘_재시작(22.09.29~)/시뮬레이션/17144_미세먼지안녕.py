"""
공기청정기는 항상 1번 열에 설치되어있고, 크기를 2행을 차지한다. (초기값) -1 -1로 주어진다.

시뮬레이션
1. 미세먼지가 있는 모든칸에서 "동시에" 확산
- 인접한 4방향으로 확산
- 인접한 방향에 칸이 없거나 공기청정기가 있으면 확산은 일어나지 않는다.
- 확산 양은 칸의 양/5이고 소수점을 "버린다".
- 남은 미세먼지 양은 확산된 만큼 빼준다. A - (A/5)*(확산된 칸 수)

2. 다음으로 공기청정기 작동
- 바람이 나오는데, 위쪽 바람은 반시계방향으로 순환, 아래쪽은 시계로 순환
- 바람이 불면 미세먼지가 방향대로 한칸씩 움직인다.
- 미세먼지가 공청으로 들어가면 사라진다.

T 초가 지난 후, 방에 남은 미세먼지의 총양을 계산
"""
import copy
import math
import sys
read = sys.stdin.readline

R,C,T = map(int,read().split())
graph = []
for _ in range(R):
    graph.append(list(map(int,read().split())))
# 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 공기청정기의 위치 알기
air_fresh = []
for r in range(R):
    if graph[r][0] == -1 :
        air_fresh.append([r,0])

# 알고리즘 시작
from collections import deque
# T초 동안 일어나는 일이므로 FOR문 사용

for t in range(T):
    """
    1. 미세먼지가 있는 모든칸에서 "동시에" 확산
    - 인접한 4방향으로 확산
    - 인접한 방향에 칸이 없거나 공기청정기가 있으면 확산은 일어나지 않는다.
    - 확산 양은 칸의 양/5이고 소수점을 "버린다".
    - 남은 미세먼지 양은 확산된 만큼 빼준다. A - (A/5)*(확산된 칸 수)
    """
    # 모든 칸에서 동시에 확산이니까 일단, queue를 만들어서 미세먼지가 있는 칸들을 넣자.
    q = deque()
    for r in range(R):
        for c in range(C):
            # 미세먼지가 있으면 저장하자.
            if graph[r][c] >= 1 :
                q.append([r,c])

    # 이제 인접한 네 방향으로 확산하는 알고리즘을 짜자
    # 이건 음 한번 확산만 할거니까 나중에 q를 append 안해도된다.


    # 이때, 네방향을 찾을 때 한번에 확산임을 잊지말자.
    # 그래서 map을 하나더 만들어야한다. 왜냐하면 기존의 정보를 저장해놔야 동시에 확산가능하기 때문이다.
    # 이 temp는 수정되지 않는 맵이다.
    temp_graph = copy.deepcopy(graph)

    # while q :
    for qq in q:
        now_dust_r,now_dust_c = qq#q.popleft()
        # 네 방향 확인하면서 확산될 곳들을 저장도 해야한다. 이 while문 끝에 확산도 해야함.
        temp_dust_list = []
        for i in range(4):
            near_dust_r = now_dust_r + dr[i]
            near_dust_c = now_dust_c + dc[i]
            # 네 방향이 잘못된 곳이 아님과 동시에 공기청정기가 있으면 안된다.
            if 0<=near_dust_r<R and 0<=near_dust_c<C and graph[near_dust_r][near_dust_c] != -1 :
                temp_dust_list.append([near_dust_r,near_dust_c])
        # 확산될 곳을 다 찾았으면 개수를 세자
        near_num = len(temp_dust_list)
        # 장소가 1개 이상이면 확산하고 미세먼지를 감소시키자.
        # 근데 굳이 if문 안쓰고 for문 써도 되긴함. 없으면 없는대로 안돌아가거든.

        for n_r,n_c in temp_dust_list:
            # 여기는 인접칸들에 미세먼지를 뿌려주는 곳
            graph[n_r][n_c] += math.floor(temp_graph[now_dust_r][now_dust_c]/5)
        # 이제 확산됬으니 미세먼지를 빼주자.
        # 이거도 near_num이 0이면 그냥 안더해주게 됨.
        graph[now_dust_r][now_dust_c] -= math.floor(temp_graph[now_dust_r][now_dust_c]/5) * near_num

    """
    이제 확산이 끝났으니 공기청정기가 돌아갈 시간이다.
    2. 다음으로 공기청정기 작동
    - 바람이 나오는데, 위쪽 바람은 반시계방향으로 순환, 아래쪽은 시계로 순환
    - 바람이 불면 미세먼지가 방향대로 한칸씩 움직인다.
    - 미세먼지가 공청으로 들어가면 사라진다.
    """

    # 먼저 위쪽 바람을 구현해볼까.
    # 공기청정기의 위쪽의 행좌표는 다음과 같다.
    upper_air_r = air_fresh[0][0]
    # 먼저 위에 영향을 끼칠 공간을 저장하자
    temp_map = copy.deepcopy(graph)
    # 4개의 for문으로 옮겨주자.

    # 윗 행부터
    for upper_c in range(C-1): # c-1의 이유는 제일 오른 쪽 값은 그 오른쪽 값이 없기 때문
        graph[0][upper_c] = temp_map[0][upper_c+1]
    # 제일 왼쪽 열
    for left_r in range(1,upper_air_r): #1부터 하는 이유는 제일 첫번째 값(0,0)은 이미 위 for문에서 고쳐짐.
        graph[left_r][0] = temp_map[left_r-1][0]
    # 제일 아래 행
    for down_c in range(2,C): # 1부터 하는 이유는 공청의 위치와 공청 옆은 깨끗하기에, c인 이유는 제일 끝 열까지 와야해서.
        graph[upper_air_r][down_c] = temp_map[upper_air_r][down_c-1]
    # 제일 우측 열
    for right_r in range(upper_air_r):
        graph[right_r][-1] = temp_map[right_r+1][-1]
    graph[upper_air_r][1] = 0

    # 공기청정기의 아래쪽의 행좌표는 다음과 같다.
    down_air_r = air_fresh[1][0]
    # 4개의 for문으로 옮겨주자.
    # 제일 위 행
    for upper_dc in range(2,C):
        graph[down_air_r][upper_dc] = temp_map[down_air_r][upper_dc-1]
    # 제일 우측 열
    for right_dr in range(down_air_r+1,R):
        graph[right_dr][C-1] = temp_map[right_dr-1][C-1]
    # 제일 아래 행
    for down_dc in range(C - 1):
        graph[R-1][down_dc] = temp_map[R-1][down_dc + 1]
    # 제일 왼쪽 행
    for left_dr in range(down_air_r+1,R-1):
        graph[left_dr][0] = temp_map[left_dr+1][0]
    graph[down_air_r][1] = 0

# 결과 출력

results = 0
for vv in range(R):
    results += sum(graph[vv])
print(results+2)