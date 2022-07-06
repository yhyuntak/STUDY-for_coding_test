n,m =  map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((1,b))
    graph[b].append((1,a))


start = 1

end,mid = map(int,input().split())

'''
이 문제는 A->K + K->X를 각각 구해서 합해주면 답일듯
'''

import heapq

def road_to_map(start,distance):

    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :

        dist , now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for cost, connected_node in graph[now] :

            if cost + dist < distance[connected_node] :
                distance[connected_node] = cost + dist
                heapq.heappush(q,(cost+dist,connected_node))

    return distance


INF = 1e9
A_to_K_distance = [INF]*(n+1)
K_to_X_distance = [INF]*(n+1)

A_to_K_road = road_to_map(start,A_to_K_distance)
Num_A_to_K = A_to_K_road[mid]

K_to_X_road = road_to_map(mid,K_to_X_distance)
Num_K_to_X = K_to_X_road[end]

if Num_A_to_K+Num_K_to_X >= INF :
    print(-1)
else :
    print(Num_A_to_K+Num_K_to_X)

# print(A_to_K_road)
# print(Num_A_to_K)
# print(K_to_X_road)
# print(Num_K_to_X)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''