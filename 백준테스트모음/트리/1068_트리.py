# 220916

N = int(input())

# -1이 나오면 루트고, 각각 자신의 부모를 표현함.
array = list(map(int,input().split()))
trees = [[] for _ in range(N)]
root_node = 0
for idx,a in enumerate(array):
    if a == -1 :
        root_node = idx
    else :
        trees[idx].append(a)
        trees[a].append(idx)

remove_node = int(input())
visited = [0 for _ in range(N)]

def DFS(start,remove,count):
    children = trees[start]
    # 말단 노드의 경우, 자식이 없고 부모는 이미 방문한 상태임.
    # 그러니까 카운트만 세서 위로 올려버려야함.
    if len(children) == 1 and visited[start] == 1 :
        return count + 1
    for child in children :
        if child != remove :
            if visited[child] == 0:
                visited[child] = 1
                count = DFS(child,remove,count)
        else :
            # 만약 자기 자식이 remove되버렸으면 자기 자신이 leaf가 되므로 카운트하나하기.
            # 이때, 자기가 root면 안되고, 자식들이 remove를 빼고 부모도 빼고 없으면 자기가 리프가 됨.
            global root_node
            if root_node != start and len(children)-2 == 0:
                count+=1
    return count

count = 0
visited[root_node] = 1
if root_node == remove_node :
    print(0)
else :
    count = DFS(root_node,remove_node,count)
    print(count)



"""
        9
      1   2

"""






# 220801
# def dfs(trees, remove_list, m):
#     # 자식이 없다면 함수를 종료하고 해당 노드의 정보를 추가해서 윗단으로 보내기
#     if len(trees[m]) == 0:
#         return remove_list + [m]
#
#     # left,right 자식 노드가 있는지 모르니 for문으로 대체하자.
#     for child in trees[m]:
#         # 자식이 있으니 여기까지 왔고,
#         # 그럼 그 자식의 dfs로 들어가야함.
#         remove_list = dfs(trees, remove_list, child)
#
#     return remove_list
#
#
# def solution():
#     import sys
#     read = sys.stdin.readline
#
#     N = int(read())
#     input_list = list(map(int, read().split()))
#     M = int(read())
#
#     # tree의 dictionary 초기화
#     trees = dict()
#     for i in range(N):
#         trees[i] = []
#         # key의 value들은 key를 부모로 갖는 자식노드들을 뜻한다.
#
#     for child, parent in enumerate(input_list):
#
#         # 동시에 트리에 값을 넣자.
#         parent = input_list[child]
#         if parent == -1:
#             continue
#         # 지워질 값은 애초에 넣지 말아볼까
#         elif child == M :
#             continue
#         else:
#             trees[parent].append(child)
#
#     # 엥 dict으로 처리하니까 그냥 자식 없는 노드를 세는 방법이 DFS로 탐색하지 않아도 되네?
#
#     # 일단 노드 제거 부분을 구현하자
#     # 트리에서 해당 노드(M)으로 child를 뽑아
#     # 이 부분을 DFS로 구현해야겠다.
#     # DFS로 탐색하다가 자식이 없으면 제거 리스트에 해당 요소를 추가하는 느낌으로?
#
#     remove_list = []
#     remove_list = dfs(trees, remove_list, M)
#     # 이제 remove_list를 통해 tree dict에서 node제거
#     for remove_node in remove_list:
#         trees.pop(remove_node)
#
#     # 이제 empty 요소를 측정하자.
#     leaf_node_count = list(trees.values()).count([])
#
#     return leaf_node_count
#
#
# print(solution())
#
