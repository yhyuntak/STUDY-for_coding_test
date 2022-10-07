

"""

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

"""
import copy

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

"""
dfs를 이용해서 탐색하고 최대값을 매번 저장하는건가?
"""

# 상 우 하 좌 -> 무조건 변들이 연결되어있어야한다했음.
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,cnt):
    # 4개의 도형이 모이면 종료하기.
    if cnt == 4 :
        global max_val
        max_val = max(max_val,visited[r][c])
        return

    # 상 우 하 좌 탐색
    for i in range(4):
        # visit이 방문했는지 체크 겸 값 저장하는 것으로 사용하자 그럼 좋을듯.
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
            visited[nr][nc] = visited[r][c] + graph[nr][nc]
            dfs(nr,nc,cnt+1)
            visited[nr][nc] = 0

def other(r,c) :
    # 먼저 r,c가 ㅗ를 표현할 수 있는 칸인지 부터 확인.
    if 1<=r<N-1 and 1<=c<M-1 :
        for i in range(4):
            # 4개의 모습이 있음.
            temp_sum = graph[r][c]
            for j in range(3) :
                # 012 123 230 301
                k = (i+j)%4
                nr,nc = r+dr[k],c+dc[k]
                temp_sum += graph[nr][nc]
            global max_val
            max_val = max(max_val,temp_sum)

max_val = -10e9
visited = [[0 for _ in range(M)] for _ in range(N)]

for r_ in range(N):
    for c_ in range(M):
        now_val = graph[r_][c_]
        visited[r_][c_] = now_val
        dfs(r_,c_,1)
        visited[r_][c_] = 0
        other(r_,c_)
print(max_val)