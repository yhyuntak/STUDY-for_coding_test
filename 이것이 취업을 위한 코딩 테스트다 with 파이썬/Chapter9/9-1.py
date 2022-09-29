import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1): # 0을 제외하고 모든 노드를 보는건데..
        # 방문하지 않고 distance가 갱신된 것을 찾는다.
        # 여기서 방문하지 않고 라는 조건에 의해 이미 방문한 (예를 들어 시작 노드)곳은 패싱된다.
        # 그리고 그 distance 중에 가장 비용이 적은 노드 인덱스를 반환
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index= i
    return index

def dijsktra(start):

    distance[start] = 0
    visited[start] = True

    for j in graph[start] :  # start 노드와 연결된 것들을 전부 살펴봄
        distance[j[0]] = j[1] #연결된 노드에 적힌 비용들을 기록하기

    for _ in range(n-1): # start를 제외한 나머지 노드들을 방문하는 반복문

        now = get_smallest_node() #방문하지 않았고, distance 리스트에서 가장 비용이 적은 인덱스 가져오기
        visited[now] = True #방문 처리하기

        for j in graph[now] :
            cost = distance[now] + j[1] # 방문한 노드에서 하나씩 비용을 살펴보면서 비용을 더해준다.
            if cost < distance[j[0]]:
                distance[j[0]] = cost #시작 노드에서 j[0]의 노드까지 가는 비용의 최소를 갱신


dijsktra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])
