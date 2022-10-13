"""

초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다.
일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현


블록 그룹은 연결된 블록의 집합
그룹에 일반 블록은 적어도 한개 이상. 일반 블록의 색은 같아야함. 검은색은 포함되면 안되고 무지개는 상관 없다.
그룹당 총 블록의 수는 3이상.

임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. -> 한 면이 인접해야한다는 의미.

블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다. -> 정렬

 블록 그룹이 존재하는 동안 계속해서 반복

1) 크기가 가장 큰 블록 그룹을 찾는다.
그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.

2) 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.

3) 격자에 중력이 작용한다. 검은색을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다.

4) 격자가 90도 반시계 방향으로 회전한다.

5_ 다시 중력 작용 -> 함수로만들ㅇ자.
"""

from collections import deque

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

import copy
def gravity(arr):
    # temp_arr = copy.deepcopy(arr)
    # 모든 열을 돌면서 각각의 row를 확인하자.
    for c in range(N):
        # 제일 아래에서 부터 확인하자. 근데 제일 아래칸의 바로 윗칸 부터! (N-2)
        for r in range(N-2,-1,-1):
            # 현재 칸이 무지개,일반이여야만 움직일 수 있다.
            if arr[r][c] <= -1 : # 빈칸이거나, 검은색이면 continue
                continue

            # 어디에 장애물이 있을지 모르니까 또 루프를 돌면서 장애물의 위치를 파악하자.
            for pointing in range(r+1,N): # 지금 위치에서 제일 마지막까지 탐색할것.
                if arr[pointing][c] != -2 : # 빈칸이 아니라면, 블록이 있다는 것이므로 더이상 갈 수 없다.
                    pointing -= 1
                    break
            # 놓을 수 있는 위치가 pointing으로 결정됬다.
            # 블럭을 해당 위치에 놓자.
            arr[pointing][c] = arr[r][c]
            # 그리고 블럭이 있던 곳은 빈칸으로 초기화
            if pointing != r :
                arr[r][c] = -2

    return arr

Results = 0
while True :
    # 일단 블록의 그룹들을 찾아야한다.
    # 블록 그룹의 기준은 "일반블록" 이면서 행의 번호가 가장 작고 열의 번호가 가장 작은 것. 즉, 이중 루프를 돌면서 선택되는 것이 기준이다.

    groups_info = []
    block_groups = []
    group_idx = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            now_block = board[r][c]
            # 지금의 블럭이 일반블럭이여야만 그룹을 찾는 BFS를 쓸 수 있다.
            if now_block > 0 and visited[r][c] == 0 : # 일반 블럭의 조건이고, 중복 방문을 빼야한다.

                # 이제 이 블럭을 기준으로 그룹을 생성하자.
                crit_val = now_block
                q = deque()
                q.append([r,c])
                visited[r][c] = crit_val
                total_cnt = 1 # 기준 블럭 선택의 수 포함시킴.
                rainbow_cnt = 0
                block_group = [[r,c]]
                rainbow_list = []
                while q :
                    now_r,now_c = q.popleft()
                    for i in range(4):
                        nr,nc = now_r+dr[i],now_c+dc[i]
                        if (0<=nr<N and 0<=nc<N) and visited[nr][nc] == 0 : # 일단 경계선 안이고 방문하지 않았어야한다.
                            # 검은색은 continue, 무지개는 다 ok , 일반 블럭은 crit_val과 같은 것만.
                            now_val = board[nr][nc]
                            if now_val == 0 : # 무지개
                                visited[nr][nc] = 1
                                total_cnt+=1
                                rainbow_cnt += 1
                                q.append([nr,nc])
                                block_group.append([nr,nc])
                                rainbow_list.append([nr,nc])
                            elif now_val == crit_val : # 일반
                                visited[nr][nc] = crit_val
                                total_cnt+=1
                                q.append([nr,nc])
                                block_group.append([nr,nc])
                            else : # 검은색 혹은 값이 다른 일반블럭 또는 빈칸(-2)
                                # 방문 했다는 처리는 하자.
                                continue

                #  그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
                if total_cnt >= 2 :
                    block_groups.append(block_group)
                    groups_info.append([group_idx,total_cnt,rainbow_cnt,r,c]) # [총개수,무지개수,기준블럭행,기준블럭열]
                    group_idx += 1

                for rr,rc in rainbow_list :
                    visited[rr][rc] = 0
    if len(groups_info) == 0 :
        break

    groups_info.sort(key=lambda x : (-x[1],-x[2],-x[3],-x[4]))
    biggest_group = block_groups[groups_info[0][0]]
    """        
    2) 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
    """
    B = 0
    for r,c in biggest_group :
        board[r][c] = -2 # 0은 무지개니까.. 빈칸은 -2로 하자
        B+=1
    Results += B**2
    """
        
    3) 격자에 중력이 작용한다. 검은색을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다.
    
    """
    board = gravity(board)


    """
    
    4) 격자가 90도 반시계 방향으로 회전한다.
    """

    temp_board = copy.deepcopy(board)
    for r in range(N):
        for c in range(N):
            temp_board[(N-1)-c][r] = board[r][c]


    """
    5_ 다시 중력 작용 -> 함수로만들ㅇ자.    
    
    """

    board = gravity(temp_board)


print(Results)