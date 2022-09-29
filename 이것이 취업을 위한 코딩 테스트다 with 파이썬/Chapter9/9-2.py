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
        if distance[now] < dist: #지금 본 노드가 이미 탐색되었고, 이미 탐색된 비용이 지금 힙큐에서 뽑은 비용보다 작으면 업데이트를 할 필요가 없으니 패스
            # 4 3 -->    3 < 4  -> true 실행안됨 ->
            continue

        for connected_node,connected_cost in graph[now]: # 지금 보고있는 노드와 연결된 노드들(now 인덱스에 있는 튜플들)을 탐색
            cost = dist + connected_cost # 현재 노드까지의 거리와 다음 노드 간의 거리를 더해서 비용 계산
            if cost < distance[connected_node]: # 현재 저장된 다음 노드까지의 거리와 계산된 비용을 비교해서
                # 계산된 비용이 더 적으면 저장된 거리를 갱신
                distance[connected_node] = cost
                # 그리고 그 노드를 탐색만하고 아직 방문하지 않았으니, 힙큐에 넣기
                heapq.heappush(q,(cost,connected_node))
        print("q:",q)
        print("distance:",distance)

dijikstra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''