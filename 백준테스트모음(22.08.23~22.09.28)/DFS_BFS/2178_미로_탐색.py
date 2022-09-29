# 220912

N,M = map(int,input().split())
move_graph = [[0 for m in range(M)] for _ in range(N)]
map_graph = []
for _ in range(N):
    temp = input()
    temp_list = [int(t) for t in temp]
    map_graph.append(temp_list)

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

from collections import deque
q = deque()
q.append([0,0])
move_graph[0][0] = 1

while q :
    now_r,now_c = q.popleft()
    now_move = move_graph[now_r][now_c]

    for i in range(4):
        next_r,next_c = now_r+dr[i] , now_c + dc[i]
        # 이 문제는 visited와 move_graph를 같다고 볼 수 있다.
        if 0<=next_r<N and 0<=next_c<M and map_graph[next_r][next_c] == 1 and move_graph[next_r][next_c] == 0:
            # 해당 장소는 방문이 가능하다!
            q.append([next_r,next_c])
            move_graph[next_r][next_c] = now_move + 1

print(move_graph[N-1][M-1])