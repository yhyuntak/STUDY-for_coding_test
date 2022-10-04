# 약간  백트래킹요소가 섞여있는데.. 무조건 DFS로 가야할듯.

import sys
read = sys.stdin.readline
from copy import deepcopy as dp
sys.setrecursionlimit(10**9)

R,C = map(int,input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int,read().split())))


visited = [[-1 for _ in range(C)] for _ in range(R)]
start = [0,0]

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

route = 0



def dfs(r,c):
    # print([r,c])
    # for _ in range(R):
    #     print(visited[_])

    # 끝점에 도달했을 때, dfs 종료
    if r == R-1 and c == C-1 :
        return 1

    if visited[r][c] == -1 : # 아직 방문하지 않은 상태라면
        # 방문처리"만" 하고 알고리즘으로 들어가자.
        visited[r][c] = 0

        # 상 우 하 좌를 탐색하자
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<= nr < R and 0<= nc < C:
                # 현재 노드의 값보다 더 작은 값일 경우에만 전진한다는 조건을!
                if graph[nr][nc] < graph[r][c] :
                    # 현재 노드 값은 dfs로 다음 노드를 확인하고 더해주는 느낌.
                    # 왜냐하면 최종 노드에 달했을 때, 1을 return하면서 끝나니까
                    # 갔던 길들이 다 +1되는 방식
                    visited[r][c] += dfs(nr,nc)

    # dfs로 다음노드에 들어와 봤더니 이미 방문했던 상태라면, 해당 루트로 가는 방법의 수가 visited에 기록되어있다.
    # 그것을 return하자
    return visited[r][c]

dfs(0,0)

print(visited[0][0])
