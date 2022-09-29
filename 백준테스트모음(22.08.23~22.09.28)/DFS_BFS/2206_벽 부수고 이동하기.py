
# 220927

import sys
read = sys.stdin.readline

N,M = map(int,read().split())

graph = []
for _ in range(N):
    temp = read().split()
    temp = temp[0]
    temp_array = [int(t) for t in temp]
    graph.append(temp_array)

visited = [[[0 * 2 for _ in range(2)] for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1


# 1을 만나면 벽을 뚫었다는 state를 1로
# 0을 만나면 벽을 안뚫었다는 state를 0으로

# 이 문제는 현재 위치를 1로 설정하고 거리를 진행할수록 +1을 해가는 식인데.. 이미 1이 사용되었으니 -1씩 감소하는 거로 해보자.

from collections import deque



# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]


# state는 각자의 q가 객체라고 생각하고 각각이 계속해서 그 정보를 유지하며 가져가야함.

def bfs():
    q = deque()
    q.append([0, 0, 0])  # 제일 마지막은 벽을 뚫었는가 안뚫었는가에 대한 state

    while q :
        now_r,now_c,wall = q.popleft()
        if now_r == N-1 and now_c == M-1 :
            return visited[N-1][M-1][wall]
        for i in range(4):
            next_r,next_c = now_r+dr[i],now_c+dc[i]
            if 0<= next_r < N and 0<= next_c < M : # 일단 맵 안에 들어오는지부터 체크
                # 여기서 다음 칸이 벽이냐 아니냐를 체크해야함.
                if graph[next_r][next_c] == 0 and visited[next_r][next_c][wall] == 0: # 만약 그냥 땅이고 아직 방문하지 않았다면 방문한다.
                    visited[next_r][next_c][wall] = visited[now_r][now_c][wall]+1 # 한칸 이동했다는 표시 설정.
                    q.append([next_r,next_c,wall]) # 단, 벽을 뚫었는지의 여부는 이전 상태의 state를 그대로 사용.

                elif graph[next_r][next_c] == 1 : # 벽이라면 state를 확인하자.
                    if wall == 0 : # 아직 벽을 안뚫어봤다면 뚫자.
                        visited[next_r][next_c][1] =  visited[now_r][now_c][wall]+1
                        q.append([next_r,next_c,1])
                    elif wall == 1 : # 벽을 뚫어본 상태라면 더이상 갈 수 없으니 q에 넣지 않음으로써 객체 소멸.
                        continue
    return -1

print(bfs())

"""
2 6
010001
000110
"""