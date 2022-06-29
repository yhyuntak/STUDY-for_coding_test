def dfs(graph,v,visitied):
    visited[v] = True
    print(v,end=' ') # 현재 내 노드를 얘기함
    for i in graph[v]: # 현재 내 노드에서 갈 수 있는 선택지를 얘기함.

        if not visitied[i]:
            # 선택지 각각의 방문 여부를 확인하고 방문 안했을 경우(visitied[i] = False)
            # 그 곳에 가서 다시 dfs를 실행해 탐색하러 간다.
            # dfs 자체를 재귀함수로써 사용해 갈 수 있는 가장 깊게까지 간 후,
            # 못가는 곳이 생기면 그 때의 재귀함수를 종료하고 그 때의 노드에서
            # 갈 수 있는 곳을 체크하는 방식으로..
            dfs(graph,i,visitied)

# 이게 아마도 adjacency list 같고, 숫자를 가장 낮은 것부터 노드의 이웃들을 표시하는 것이 일반적이다.
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],

]

visited = [False]*9

dfs(graph,1,visited)
