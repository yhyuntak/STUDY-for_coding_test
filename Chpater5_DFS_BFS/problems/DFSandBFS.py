
from collections import deque

def dfs(graph, v, visited):
    # 현재 vertex를 방문 처리함.
    visited[v] = True
    print(v,end=' ')

    # 이제 탐색 시작
    for i in graph[v] :

        # 만약 방문하지 않은게 참(not)이라면
        if not visited[i] :

            # 그곳을 방문 처리하자.
            dfs(graph,i,visited)


def bfs(graph,start,visited):

    # 현재 위치를 queue에 쌓기
    queue = deque()
    queue.append(start)

    # 방문했다고 기록하기
    visited[start] = True

    # queue 가 더이상 쌓이지 않을때까지 반복
    while queue :
        # queue에서 하나 뽑아.
        v= queue.popleft()
        print(v,end=' ')

        # 주변을 하나씩 탐색하기 시작
        for i in graph[v]:
            # 탐색하려는 곳이 방문하지 않은게 참이면,
            if not visited[i]:
                # 여기는 이제 탐색하러 도착했음. 이제 이녀석의 주변을 방문하기 위해서 queue에 쌓자
                queue.append(i)
                # 도착했으니 True로 .
                visited[i]=True


n,m,v = map(int,input().split())
node_list = [[] for _ in range(n+1)]


for i in range(m):
    # 연결관계 만들어주기
    now_inputs = list(map(int,input().split()))
    node_list[now_inputs[0]].append(now_inputs[1])
    node_list[now_inputs[1]].append(now_inputs[0])

for i in range(n+1):
    node_list[i].sort()

dfs_visited = [False for _ in range(n+1)]
bfs_visited = [False for _ in range(n+1)]
dfs_visited[0] = True

dfs_results = []
bfs_results = []

dfs(node_list,v,dfs_visited)
print()
bfs(node_list,v,bfs_visited)
