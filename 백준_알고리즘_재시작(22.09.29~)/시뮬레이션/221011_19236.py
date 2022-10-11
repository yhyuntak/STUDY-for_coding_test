"""

방향은 8개. 각각 번호를 갖는 물고기들이 있다.

1. 0,0에 있는 물고기를 먹고 진입. 방향은  먹은 물고기의 방향과 같다.

2. 바로 물고기가 이동한다.

번호가 작은 물고기부터 "순서대로" 이동. 한칸을 방향대로 이동할 수 있고, 이동 가능한 칸은 빈칸 혹은 다른 물고기가 있는 칸이다.
상어가 있거나 경계를 넘어가면 안된다.
만약 이동 불가능하면 이동할 수 있는 칸을 바라볼 떄까지 45도씩 반시계로 회전. 이동할 수 있는 곳을 찾자 마자 이동하는 듯.
다른 물고기가 있는 곳으로 가면 서로의 위치를 바꾼다.

3. 상어 이동
방향으로 여러 칸을 이동가능. 물고기가 있는 곳으로 가면 먹고 방향을 가짐. 지나가는 칸의 물고기는 안먹음.
물고기가 없으면 이동 불가능.
상어가 이동할 수 있는 공간이 아무리 찾아도 없으면 집으로 간다. (끝)인듯? 다시 진입도 치는건가..?

"""
import copy

fishes_map = [[] for _ in range(4)]
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(4):
        a,b = temp[j*2],temp[j*2+1]
        fishes_map[i].append([a,b-1,'f'])

# 상 좌상 좌 좌하 하 우하 우 우상
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]

def dfs(sr,sc,score,graph):

    global max_val
    score += graph[sr][sc][0] # 물고기 먹기
    graph[sr][sc][0] = 0
    max_val = max(max_val,score)

    # 물고기 이동
    for num in range(1,17):
        fr,fc = -1,-1
        find_ = False
        for i in range(4):
            for j in range(4):
                print(i,j)
                if graph[i][j][0] == num:
                    fr,fc = i,j
                    find_ = True
                    break
            if find_ :
                break
        if fr == -1 and fc == -1 : # 빈칸이라면
            continue

        fish_d = graph[fr][fc][1]

        for i in range(8): # 이렇게 묶어서 표현 가능한 이유가 i=0부터 시작하기 때문에.
            nd = (i+fish_d)%8
            nr,nc = fr+dr[nd],fc+dc[nd]
            # 만약 경계선을 넘어가거나 상어를 만나면 돌아가게끔.
            if not (0<=nr<4 and 0<=nc<4) or (nr == sr and nc == sc) : # 상어의 위치를 입력으로 넣네..
                continue
            # 여기까지오면 이젠 문제없는 것이므로
            # 먼저 무조건 방향 업데이트
            graph[fr][fc][1] = nd
            graph[fr][fc],graph[nr][nc] = graph[nr][nc],graph[fr][fc]
            break
    # 상어가 밥먹음
    sd = graph[sr][sc][1]
    for i in range(1,5):
        nr,nc = sr+dr[sd]*i,sc+dc[sd]*i
        if (0<=nr<4 and 0<=nc<4) and graph[nr][nc][0] > 0 : # 빈칸은 번호를 0으로 만들것이므로.
            # 물고기가 경계선 안에있으면을 뜻함
            # 물고기 먹는건 dfs 첫번째에 구현함.
            dfs(nr,nc,score,copy.deepcopy(graph))

max_val = -10e9
dfs(0,0,0,fishes_map)
print(max_val)