INF = int(1e9)

n=int(input())
m=int(input())

# 첫번째 row, column을 아예 없다고 생각하자.
graph = [[INF]*(n+1) for _ in range(n+1)]


# diagonal는 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b :
            graph[a][b]=0

#간선정보
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 2차원 배열을 전부다 훑지만(a,b) k번째 노드를 중심으로 포함해서 비교해야하기때문에 3중 반복문이 됨.
for k in range(1,n+1): # 노드를 하나씩 선택해서

    for a in range(1,n+1): #a,b 세트를 선택
        for b in range(1,n+1):
            # if a==b or a==k or k==b :
            #     continue
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])


for a in range(1,n+1):
    for b in range(1,n+1):

        if graph[a][b] == INF :
            print("INF",end=" ")

        else :
            print(graph[a][b],end=" ")
    print()