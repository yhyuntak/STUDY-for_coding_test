"""
1번 컴퓨터가 시작
정보가 주어졌을 때, 바이러스에 걸리게되는 컴퓨터의 수는?
"""

N = int(input())
T = int(input())
computers = [[] for _ in range(N+1)] # 컴퓨터의 수

for _ in range(T):
    a,b = map(int,input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [ 0 for _ in range(N+1)]

from collections import deque

q = deque()
start = 1
q.append(start)
# 지금 선택된 노드를 방문처리하기.
visited[start] = 1
# 1을 시작으로 몇개의 방문을 했는지를 파악하기 위한 results 생성 (1은 포함하지 않는듯)
results = 0
while q :
    now = q.popleft()

    # 현재 노드와 연결된 다른 노드들을 체크하고, 방문하지 않은 것들만을 queue에 쌓기
    for next_com in computers[now] :
        if visited[next_com] == 0 :
            q.append(next_com)
            visited[next_com] = 1
            results+=1

print(results)

