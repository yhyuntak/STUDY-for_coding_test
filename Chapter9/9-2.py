import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijikstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: #현재노드가 사용됬으면 패스?
            continue
        for i in graph[now]: # now와 연결된 노드들(now 인덱스에 있는 튜플들)을 탐색
            cost = dist + i[1] # 현재 노드까지의 거리와 다음 노드 간의 거리를 더해서 비용 계산
            if cost < distance[i[0]]: # 현재 저장된 다음 노드까지의 거리와 계산된 비용을 비교해서
                # 계산된 비용이 더 적으면 저장된 거리를 갱신
                distance[i[0]] = cost
                # 그리고 그 노드를 탐색만하고 아직 방문하지 않았으니, 힙큐에 넣기
                heapq.heappush(q,(cost,i[0]))

dijikstra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])

