N,M = map(int,input().split())
s_row,s_col,direction = map(int,input().split())
state = [s_row,s_col]
# my_go = [[0]*M for _ in range(N)]
my_map = []
for _ in range(N):
    row_dont_go = list(map(int,input().split()))
    my_map.append(row_dont_go)

my_map[state[0]][state[1]] = 1

dx = [0,1,0,-1] # 북 동 남 서
dy = [-1,0,1,0] # 북 동 남 서

count = 1
finish_ = 0
while True :
    direction -= 1 # 북:0 동:1 남:2 서:3
    if direction < 0 :
        direction = 3
    # 1,2단계 수행
    if my_map[state[0]+dy[direction]][state[1]+dx[direction]] == 0 :
        # 가고
        state[0] += dy[direction]
        state[1] += dx[direction]
        my_map[state[0]][state[1]] = 1
        count += 1
        finish_ = 0
    else:
        # 가지 않는다.
        finish_ += 1

    # 네방향 모두 갈 수 없을 때
    if finish_ == 4 :
        if my_map[state[0]-dy[direction]][state[1]-dx[direction]] == 0 :
            state[0] -= dy[direction]
            state[1] -= dx[direction]
        else :
            break
        finish_ = 0

print(count)

