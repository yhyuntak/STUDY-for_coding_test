n = int(input())

# 먼저 맵을 받자

bomb_graph = []
for _ in range(n):
    bomb_graph.append(list(input()))

move_graph = []
for _ in range(n):
    move_graph.append(list(input()))

new_map = [["." for _ in range(n)] for _ in range(n)]

# 2중 for문을 돌면서 주변을 탐색하고 지뢰의 수를 계산해서 해당 칸에 넣자.
# 단, 지뢰를 만났을 경우엔 다음 row로 넘어가기

# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

bomb_switch = False

for r in range(n):
    for c in range(n):
        ask_move = move_graph[r][c]
        if ask_move == "." :
            # 가지 않은 곳이니 넘어가자.
            continue
        else :
            # 간 곳이므로 알고리즘 실행
            # 지뢰를 밟았는지 확인만 하자
            if bomb_graph[r][c] == "*":
                bomb_switch = True

            # 주변에 8좌표를 확인해야한다.
            bomb_count = 0
            for k in range(8):
                next_r = r+dr[k]
                next_c = c+dc[k]
                if 0<= next_r < n and 0<= next_c < n :
                    if bomb_graph[next_r][next_c] == "*":
                        bomb_count+=1
        new_map[r][c] = str(bomb_count)

if bomb_switch :
    for r in range(n):
        for c in range(n):
            ask_bomb = bomb_graph[r][c]
            if ask_bomb == "*":
                new_map[r][c] = "*"
for j in range(n):
    print(''.join(new_map[j]))


"""
8
...**..*
......*.
....*...
........
........
.....*..
...**.*.
.....*..
xxxx....
....xxxx
xxxx....
....xxxx
xxxx....
....xxxx
xxxx....
....xxxx

2
*.
.*
.x
x.

2
*.
.*
..
.x
"""