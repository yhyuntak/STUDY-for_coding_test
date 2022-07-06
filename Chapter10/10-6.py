from collections import deque

v,e = map(int,input().split())
indegree = [0 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split()) # a->b 방향의 간선의 정보를 나타냄.
    graph[a].append(b)
    indegree[b] += 1 # b로 들어오는 간선의 수 즉, indegree를 증가


def topology_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)

        # 간선 제거하는 과정
        for i in graph[now] :
            indegree[i] -= 1 # 간선을 제거했으니 indegree도 감소
            if indegree[i] == 0:
                q.append(i)
    for i in result :
        print( i,end=' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
1 2 5 3 6 4 7 
'''