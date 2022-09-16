"""
N이 주어졌을 때, 달팽이 모양으로 퍼져나가는 맵 (NxN)을 만들고

M이 주어지면 그 번호가 있는 위치의 좌표를 반환해야함.

"""

# M을 미리 받아서 해당 숫자가 만들어지면 그 좌표를 미리 저장해두자.

N = int(input())
M = int(input())

# 하 우 상 좌
dr = [1,0,-1,0]
dc = [0,1,0,-1]

graph = [[0 for _ in range(N)] for _ in range(N)]

val = N**2
r,c = 0,0
visited = [[0 for _ in range(N)] for _ in range(N)]
i=1
direction = 0

while i<= N**2 :
    # 0,0부터 시작하자.
    if val == M :
        save_loc = [r+1,c+1]
    graph[r][c] = val
    visited[r][c] = 1
    val -= 1
    i+=1
    # 다음 움직임을 위해서 r,c를 갱신해야함.
    next_r,next_c = r+dr[direction],c+dc[direction]
    if 0<=next_r<N and 0<=next_c<N and visited[next_r][next_c] == 0 : # 넘어가지 않았고, 방문한 곳이 아니라면.
        # 그대로 루프를 돌아서 다음 칸에 val을 대입하면 됨.
        r,c = next_r,next_c
        continue
    else : # 넘어가게 된다면 하->우->상->좌 방향으로 돌려가면 된다.
        direction = (direction+1) % 4
        r,c = r+dr[direction],c+dc[direction]

for n in range(N):
    print(*graph[n])
print(*save_loc)