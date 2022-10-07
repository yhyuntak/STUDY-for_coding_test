import sys
read = sys.stdin.readline

V = int(read())

trees = [[] for _ in range(V+1)]

for _ in range(V):
    node,*info = list(map(int,read().split()))
    for i in range((len(info)-1)//2) :
        a,weight = info[i*2:(i+1)*2]
        trees[node].append([a,weight])

# 각 노드에는 연결된 노드 번호와 weight가 설정되어있다.

# 이제 지름을 구해보자. 근데 이게 아무 정점이나 잡아도 되나?

start_info = [0,0]
final_info = [0,0]

def start_dfs(node,visit,dist):

    for next_node,weight in trees[node] :
        if visit[next_node] == 0 :
            visit[next_node] = 1
            start_dfs(next_node,visit,dist+weight)

    # 더이상 방문할 곳이 없다면 그곳은 리프노드이다.
    # 따라서 최대 거리인지 확인하자.
    if start_info[1] < dist :
        start_info[1] = dist
        start_info[0] = node

start = 1
start_visited = [0 for _ in range(V+1)]
start_visited[start] = 1
start_dfs(start,start_visited,0)


def final_dfs(node,visit,dist):

    for next_node,weight in trees[node] :
        if visit[next_node] == 0 :
            visit[next_node] = 1
            final_dfs(next_node,visit,dist+weight)

    # 더이상 방문할 곳이 없다면 그곳은 리프노드이다.
    # 따라서 최대 거리인지 확인하자.
    if final_info[1] < dist :
        final_info[1] = dist
        final_info[0] = node
    # print(node,dist,final_info)

final_start = start_info[0]
final_start_visited = [0 for _ in range(V+1)]
final_start_visited[final_start] = 1
final_dfs(final_start,final_start_visited,0)

print(final_info[1])