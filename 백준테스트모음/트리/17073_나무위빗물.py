import sys
read = sys.stdin.readline

N,W = map(int,read().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(1,N):
    a,b = map(int,read().split())
    graph[a].append(b)
    graph[b].append(a)

# 트리의 루트는 1번 고정
from collections import deque
q = deque()
q.append(graph[1])
visited[1] = 1

temp = 0
while q :
    connected = q.popleft()
    end_count = 0
    for now in connected :
        if visited[now] == 0 :
            q.append(graph[now])
            visited[now] = 1
        else :
            end_count += 1
    if end_count == len(connected) :
        temp +=1

print(W/temp)