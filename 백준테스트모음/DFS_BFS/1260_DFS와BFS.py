#220906
import sys
read = sys.stdin.readline
from collections import deque

def DFS(start, visited, results):
    # 현재 방문한 점을 출력하는 것이 문제의 목표이다.
    results.append(start)
    # start와 연결된 노드들 중 방문하지 않은 노드가 있다면 방문하자
    for node in graph[start]:
        if visited[node] == 0:
            visited[node] = 1
            DFS(node, visited, results)

def BFS(start, visited, results):
    # 시작 노드를 queue에 넣고 시작.
    q = deque([start])
    visited[start] = 1

    # start노드를 먼저 방문했으니 results에 저장
    results.append(start)

    # 루프를 돌면서 q를 하나씩 꺼내서 너비탐색시작
    while q:
        now_node = q.popleft()
        # 현재 노드와 연결된 다른 노드들을 for문으로 보면서 방문하지 않은 노드들만 추가.
        for next_node in graph[now_node]:
            if visited[next_node] == 0:
                q.append(next_node)
                # 방문처리하는 것도 잊지 말자.
                visited[next_node] = 1
                # 그리고 방문했으니 results에 저장
                results.append(next_node)
def print_array(array):
    for a in array:
        print(a, end=' ')

N,M,V = map(int,read().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,read().split())
    graph[a].append(b)
    graph[b].append(a)

for g in range(1,N+1):
    graph[g].sort()

visited_dfs = [0 for _ in range(N+1)]
# 1번 노드를 방문처리 해놓고 시작하자.
visited_dfs[V] = 1
results_dfs = []

DFS(V,visited_dfs,results_dfs)
print_array(results_dfs)

print()

visited_bfs = [0 for _ in range(N+1)]
results_bfs = []

BFS(V,visited_bfs,results_bfs)
print_array(results_bfs)