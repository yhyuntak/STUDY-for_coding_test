#220907
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(read())
trees = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,read().split())
    trees[a].append(b)
    trees[b].append(a)

visited_and_parents = [0 for _ in range(N+1)]
start = 1

def DFS(start):
    for i in trees[start]:
        if visited_and_parents[i] == 0 :
            # 아직 부모가 정해지지 않은 노드이므로,
            visited_and_parents[i] = start
            DFS(i)
DFS(start)
for j in range(2,N+1):
    print(visited_and_parents[j])


#220905
# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# N = int(read())
# tree = [[] for _ in range(N+1)]
# visited = [0 for _ in range(N+1)]
#
# for _ in range(N-1):
#     a,b = map(int,read().split())
#     tree[a].append(b)
#     tree[b].append(a)
#
# def DFS(start):
#     for node in tree[start]:
#         if visited[node] == 0 :
#             # 방문하지 않았던 노드라면, 부모를 기록해야하므로 부모 번호를 visited의 index에 기록하자.
#             # 후에 출력할 것.
#             visited[node] = start
#             DFS(node)
#
# DFS(1)
# for j in range(2,N+1):
#     print(visited[j])
#
#




#
# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# N = int(read())
# tree = [[] for _ in range(N+1)]
# parents = [0 for _ in range(N+1)]
#
# for _ in range(N-1):
#     a,b = map(int,read().split())
#     tree[a].append(b)
#     tree[b].append(a)
#
# def DFS_BFS(start,tree,parents):
#     # start 노드에 연결된 vertex들을 확인하자.
#     for i in tree[start]:
#         if parents[i] == 0 : # visited의 역할도 겸해준다.
#             parents[i] = start
#             DFS_BFS(i,tree,parents)
#
# DFS_BFS(1,tree,parents)
#
# for j in range(2,N+1):
#     print(parents[j])