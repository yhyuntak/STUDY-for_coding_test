"""
root 노드에서 가중치가 가장 큰 그니까 가장 멀리있는 노드를 탐색하고
그 노드를 기준으로 또 가장 먼 노드를 다시 탐색하면 된다.

DFS로 풀자.
"""
import copy
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N=int(input())

# 노드 i와 j가 연결되어있음을 알리기 위한 정보를 저장할 때, 가중치도 같이 저장하자.
trees = [[] for _ in range(10001)] # 1번 부터 10000까지의 트리
for _ in range(N-1):
    a,b,w = map(int,read().split())
    # 무방향성 트리임
    trees[a].append([b,w])
    trees[b].append([a,w])

root_node = 1
start_info = [0,0] # 시작 노드의 번호와 거리를 저장하는 것
final_info = [0,0] # 끝 노드의 번호와 거리를 저장하는 것

def start_dfs(node,dist,visited):
    # 일단 말단 노드에 도착했을 때가 그 루트의 최대 거리임을 기억하자.
    # 그럼 말단 노드에 도착했을 때 길이를 비교해서 업데이트하는 로직이 필요함.
    # visited를 만들어야겠네 이건
    for connected,weight in trees[node]:
        if visited[connected] == 0 : # 방문하지 않았다면
            visited[connected] = 1
            start_dfs(connected,dist+weight,visited)

    # 만약 visited로 다 걸러서 for문이 끝나게 되면, 그 루트의 최대 길이 dist를 비교하자.
    if start_info[1] < dist :
        start_info[0] = node
        start_info[1] = dist


def final_dfs(node,dist,visited):
    # 일단 말단 노드에 도착했을 때가 그 루트의 최대 거리임을 기억하자.
    # 그럼 말단 노드에 도착했을 때 길이를 비교해서 업데이트하는 로직이 필요함.
    # visited를 만들어야겠네 이건
    for connected,weight in trees[node]:
        if visited[connected] == 0 : # 방문하지 않았다면
            visited[connected] = 1
            final_dfs(connected,dist+weight,visited)
    # 만약 visited로 다 걸러서 for문이 끝나게 되면, 그 루트의 최대 길이 dist를 비교하자.
    if final_info[1] < dist :
        final_info[0] = node
        final_info[1] = dist

visited = [0 for _ in range(10001)]
# 시작 노드 찾기.
start_visited = copy.deepcopy(visited)
start_visited[root_node] = 1
start_dfs(root_node,0,start_visited)

# 끝 노드 찾기
final_visited = copy.deepcopy(visited)
start_node=start_info[0]
final_visited[start_node] = 1
final_dfs(start_node,0,final_visited)
print(final_info[1])

"""
4
1 2 2
1 3 1
2 4 4
2 5 5
"""