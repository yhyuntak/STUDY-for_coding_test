n,m = map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(n):
    graph[_] = list(map(int,input()))

dx = [-1,1,0,0] #상 하 좌 우
dy = [0,0,-1,1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    if graph[x][y] == 0:
        # 안채워져있으면 (방문하지 않았으면) 어차피 이곳은 아이스크림이 무조건 될 수 밖에 없다.
        # 그러니까 이 위치에서 주변을 전부다 채우기 위해서 재귀함수를 사용한다.
        graph[x][y] = 1 # 채우고 (방문 처리하고)

        # 상 하 좌 우 를 모두 재귀 함수를 통해 호출한다.
        # 그래서 주변의 모든 0을 1로 바꿔주는거지.
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            dfs(nx,ny)
        # dfs(x-1,y) # 상
        # dfs(x,y-1) # 좌
        # dfs(x+1,y) # 하
        # dfs(x,y+1) # 우

        # 재귀함수가 전부 완료가 되버리면 이 지점의 근처의 모든 0은 없어졌다!
        # 라고 표현하며 True를 반환해 아이스크림 개수를 1 추가하자.

        return True
    return False

# 모든 위치에 대해서 살펴보는구나..
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True :
            result += 1

print(result)