from collections import deque
def running(x,y,shark_size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    temp = []
    while q :
        now = q.popleft()
        now_y, now_x = now[0],now[1]
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == 0: # 아직 안가본 곳을 체크하기 위한 visited이다.
                if graph[ny][nx] <= shark_size :
                    # 작거나 같으면 일단 갈 순 있다.
                    q.append((ny,nx))
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[now_y][now_x] + 1 # 이동한 거리를 측정해주는구나 좋다
                    if 0 < graph[ny][nx] < shark_size : # 먹이이면 먹자!
                        temp.append((ny,nx,distance[ny][nx]))
    # 거리가 가장 가까운 순 -> 여러마리라면 제일 위 -> 위에도 많으면 제일 왼쪽부터
    # -를 붙인 이유는 pop을 통해서 오른쪽부터 추출해야하므로.
    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))

if __name__ == "__main__" :

    N = int(input())
    graph = []
    for _ in range(N):
        temp =list(map(int,input().split()))
        graph.append(temp)
    x,y = 0,0
    for n in range(N):
        temp = graph[n]
        check = [i for i,l in enumerate(temp) if l == 9]
        if len(check) != 0 :
            y = n
            x = check[0]
    shark_size = 2
    # 상 하 좌 우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    result = 0
    cnt = 0
    while True:
        shark = running(x, y, shark_size)
        # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
        if len(shark) == 0:
            break
        # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
        # 정렬한 결과를 반영해준다.
        ny, nx, dist = shark.pop()

        # 움직이는 칸수가 곧 시간이 된다.
        result += dist
        # 원래 있던 상어의 위치와 먹이의 위치에 0 처리를.
        graph[y][x], graph[ny][nx] = 0, 0
        # 상어 좌표를 먹은 물고기의 좌표로 옮겨준다.
        x, y = nx, ny
        # 먹이를 먹을때 마다 카운트를해서 사이즈와 먹은 양이 같아지면
        # 상어의 크기를 키우자.
        cnt += 1
        if cnt == shark_size:
            shark_size += 1
            cnt = 0
    print(result)