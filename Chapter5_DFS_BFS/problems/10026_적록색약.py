import copy
import sys
read = sys.stdin.readline
from collections import deque

N = int(read())
graph = []
for _ in range(N):
    temp = list(read())
    temp.pop()
    graph.append(temp)

another_graph = copy.deepcopy(graph)

# 일반인 BFS와 색맹 BFS를 구분지어서 만드는게 편할 듯.
# 상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
#
def general_bfs(graph,y,x,state):
    # complete 처리하기.
    graph[y][x] = "C"
    q = deque()
    q.append([y,x])
    while q :
        now = q.popleft()
        # 4방향을 보자.
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            # 그래프의 범위를 넘어가지 않게 조절
            if nx<0 or ny<0 or nx >= N or ny >= N :
                continue
            if graph[ny][nx] == state :
                # 단순 방문 처리만 해주면된다.
                graph[ny][nx] = "C"
                q.append([ny,nx])

def another_bfs(graph,y,x,state):
    # complete 처리하기.
    graph[y][x] = "C"
    q = deque()
    q.append([y,x])
    while q :
        now = q.popleft()
        # 4방향을 보자.
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            # 그래프의 범위를 넘어가지 않게 조절
            if nx<0 or ny<0 or nx >= N or ny >= N :
                continue

            # R,G를 같게 보고 B를 따로 보기위한 조건문 처리
            if state == "R" or state == "G" :
                if graph[ny][nx] == "R" or graph[ny][nx] == "G":
                    # 단순 방문 처리만 해주면된다.
                    graph[ny][nx] = "C"
                    q.append([ny, nx])
            else :
                if graph[ny][nx] == state:
                    # 단순 방문 처리만 해주면된다.
                    graph[ny][nx] = "C"
                    q.append([ny, nx])
# 그래프를 순차적으로 탐방하면서 R,G,B인 경우 bfs를 들어가고,
# bfs에선 탐방한 곳을 C로 바꿔야할듯.
# cnt를 둬서 구역의 수를 카운트 할 것

cnt = 0
another_cnt = 0
for y in range(N):
    for x in range(N):
        general_state = graph[y][x]
        if general_state != "C" : # 아직 방문하지 않았을땐
            general_bfs(graph,y,x,general_state)
            cnt += 1
        another_state = another_graph[y][x]
        if another_state != "C" :
            another_bfs(another_graph,y,x,another_state)
            another_cnt += 1
print(cnt,another_cnt)
