n,m,c = map(int,input().split())

INF = 1e9
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    X,Y,Z = map(int,input().split())
    graph[X].append((Z,Y))


import heapq

def road(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue

        for cost,connected_node in graph[now] :
            if cost + dist < distance[connected_node] :
                distance[connected_node] = cost + dist
                heapq.heappush(q,(cost+dist,connected_node))
road(c)

count = 0
max_distance = 0

for d in distance :
    if d != INF and d != 0:
        count += 1
        max_distance = max(max_distance,d)

print(count,max_distance)

'''
3 2 1
1 2 4
1 3 2
'''