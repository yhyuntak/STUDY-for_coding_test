"""

블록은 타일 하나 또는 두 개가 가로 또는 세로로 붙어있는 형태

블록을 놓을 위치를 빨간색 보드에서 선택하면, 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동한다. 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동한다

초록색 보드의 4번 행은 모든 칸이 타일로 가득 차있다. 이렇게 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다.

사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다.

파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며, 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동한다.

렇게 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다.

<블럭 사라짐>
초록색 보드의 0, 1번 행과 파란색 보드의 0, 1번 열은 그림에는 연한색으로 표현되어 있는 특별한 칸이다.
. 초록색 보드의 0, 1번 행에 블록이 있으면, 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고, 초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동하고,
 파란색 보드의 0, 1번 열에 블록이 있으면, 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고, 파란색 보드의 모든 블록이 사라진 열의 수만큼 이동하게 된다.

행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다. 이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리해야 한다.
"""

N = int(input())
from collections import deque

blocks = deque()
for _ in range(N):
    t, r, c, = map(int, input().split())
    blocks.append([t, r, c])

green = deque([deque([0, 0, 0, 0]) for _ in range(6)])
blue = deque([deque([0, 0, 0, 0, 0, 0]) for _ in range(4)])

# 블럭이 다 놓을떄까지.
point = 0
while blocks:
    # print("block start!!")
    t, r, c = blocks.popleft()
    """
    t = 1: 크기가 1×1인 블록을 (r, c)에 놓은 경우
    t = 2: 크기가 1×2인 블록을 (r, c), (r, c+1)에 놓은 경우
    t = 3: 크기가 2×1인 블록을 (r, c), (r+1, c)에 놓은 경우
    """

    # 먼저 쌓는것부터 구현. 중요한 것은 안에 공간은 뚫려있는데 그 위에가 막혀서 못들어갈 수 있다.
    # 그러니까 아래에서부터 확인하는게 아니라 위에서부터 확인하며 내려가야한다.

    if t == 1:
        # 1x1 블록을 놓는 것이니
        # 한 col,row만 보면된다.

        # 먼저 초록.
        # 초록은 빨강의 어떤 row에 놓든 상관 없이 열 c의 row만 훑으면 된다.
        temp_g = []
        for g_i in range(6):
            if green[g_i][c] == 0:
                temp_g = [g_i, c]
            else:  # 벽을 만나게 되면 # 그 곳부턴 탐색할 필요가 없다.
                break
        green[temp_g[0]][temp_g[1]] = 1

        # 다음 파랑.
        # 파랑은 빨강의 어떤 col이든 상관 없이 행 r에만 집중하면 된다.
        temp_b = []
        for b_j in range(6):
            if blue[r][b_j] == 0:
                temp_b = [r, b_j]
            else:
                break
        blue[temp_b[0]][temp_b[1]] = 1

    elif t == 2:
        # 1x2 블록을 놓는 것이니
        # 빨강의 (r,c),(r,c+1)를.
        temp_g = []
        for g_r in range(6):
            if green[g_r][c] == 0 and green[g_r][c + 1] == 0:  # 두 칸 다 0일 때 가능
                temp_g = [[g_r, c], [g_r, c + 1]]
            else:
                break
        green[temp_g[0][0]][temp_g[0][1]] = 1
        green[temp_g[1][0]][temp_g[1][1]] = 1

        # 블루는 세워진 형태로 들어온다.
        temp_b = []
        for b_c in range(5):  # +1을 할꺼니까 6까지 볼 필욘 없다.

            if blue[r][b_c] == 0 and blue[r][b_c + 1] == 0:  # 두 칸 다 0일 때 가능

                temp_b = [[r, b_c], [r, b_c + 1]]
            else:
                break
        blue[temp_b[0][0]][temp_b[0][1]] = 1
        blue[temp_b[1][0]][temp_b[1][1]] = 1

    elif t == 3:
        # 2x1 블록을 놓는 것이니
        # 빨강의 (r,c),(r+1,c)를.
        temp_g = []
        for g_r in range(5):  # 초록은 세워져서 들어온다. +1을 할꺼니까 6까지 볼 필요 없다.
            if green[g_r][c] == 0 and green[g_r + 1][c] == 0:  # 두 칸 다 0일 때 가능
                temp_g = [[g_r, c], [g_r + 1, c]]
            else:
                break
        green[temp_g[0][0]][temp_g[0][1]] = 1
        green[temp_g[1][0]][temp_g[1][1]] = 1

        # 블루는 누워진 형태로 들어온다.
        temp_b = []
        for b_c in range(6):
            if blue[r][b_c] == 0 and blue[r + 1][b_c] == 0:  # 두 칸 다 0일 때 가능
                temp_b = [[r, b_c], [r + 1, b_c]]
            else:
                break
        blue[temp_b[0][0]][temp_b[0][1]] = 1
        blue[temp_b[1][0]][temp_b[1][1]] = 1

    # 움직임 구현은 끝났다.

    # print("stacked green")
    # for _ in range(6):
    #     print(green[_])
    # print()
    # print("stacked blue")
    # for _ in range(4):
    #     print(blue[_])
    # print("----------------")

    # 무조건 행 열 꽉차면 삭제를 먼저.
    """        
    초록색 보드의 4번 행은 모든 칸이 타일로 가득 차있다. 이렇게 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다.    
    사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다.
    파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며, 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동한다.

    한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다.
    """

    # 아래에서 부터 꽉찬 행,열을 찾아서 삭제해주면 좋을듯.
    # deque로 하면 너무 편할 듯.
    # 먼저 초록.
    g_r = 5
    while g_r >= 0:
        # 아래부터 해서 꽉찬 것을 찾자.
        now_green = green[g_r]
        if sum(now_green) == 4:  # 꽉찼으면
            # 삭제해주는 알고리즘
            temp_g = deque()
            for r_g_r in range(5, g_r - 1, -1):
                if r_g_r == g_r:
                    green.pop()
                    break
                else:
                    temp_g.appendleft(green.pop())
            while temp_g:
                green.append(temp_g.popleft())
            green.appendleft([0, 0, 0, 0])
            # 꽉찬게 있으면 인덱스는 그대로.
            # 단, point는 +1
            point += 1

        else:  # 꽉찬게 없으면 인덱스 업데이트
            g_r -= 1

    # 다음 파랑.
    b_c = 5
    while b_c >= 0:
        # 오른쪽부터 꽉찬 것을 찾자.
        now_blue = [blue[i][b_c] for i in range(4)]
        if sum(now_blue) == 4:  # 꽉찼으면
            # 삭제해주는 알고리즘
            for r_b_r in range(4):
                temp_b = deque()
                row = blue[r_b_r]
                for j in range(5, b_c - 1, -1):
                    if j == b_c:
                        row.pop()
                        break
                    else:
                        temp_b.appendleft(row.pop())
                while temp_b:
                    row.append(temp_b.popleft())
                row.appendleft(0)

                blue[r_b_r] = row
            point += 1


        else:
            b_c -= 1
    #
    # print("pop green")
    # for _ in range(6):
    #     print(green[_])
    # print()
    # print("pop blue")
    # for _ in range(4):
    #     print(blue[_])
    # print("----------------")

    # 이제는 특별 구역에 들어가면 삭제되는 로직 구현.

    # 먼저 초록
    # 0,1에 블록이 있는 행의 수만큼 아래에서 제거.
    remove_cnt_g = 0
    for i_ in range(2):
        if sum(green[i_]) > 0:
            remove_cnt_g += 1
    if remove_cnt_g > 0:
        # 제거 로직 실행
        g_r = 5
        while g_r >= 6 - remove_cnt_g:
            # 삭제해주는 알고리즘
            green.pop()
            green.appendleft([0, 0, 0, 0])
            g_r -= 1

    # 다음 파랑
    # 0,1에 블록이 있는 열의 수만큼 아래에서 제거.
    remove_cnt_b = 0
    for j_ in range(2):
        now_blue = [blue[i][j_] for i in range(4)]
        if sum(now_blue) > 0:
            remove_cnt_b += 1
    if remove_cnt_b > 0:
        # 제거 로직 실행
        b_c = 5
        while b_c >= 6 - remove_cnt_b:
            # 삭제해주는 알고리즘
            for r_ in range(4):
                blue[r_].pop()
                blue[r_].appendleft(0)
            b_c -= 1
    #
    #
    # print("remove green")
    # for _ in range(6):
    #     print(green[_])
    # print()
    # print("remove blue")
    # for _ in range(4):
    #     print(blue[_])
    # print("----------------")

block_sum = 0
for g in green:
    block_sum += sum(g)
for b in blue:
    block_sum += sum(b)

print(point)
print(block_sum)