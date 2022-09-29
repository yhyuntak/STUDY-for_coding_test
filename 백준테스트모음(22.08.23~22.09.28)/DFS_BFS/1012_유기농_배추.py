
# 220916

"""

각 테스트 케이스마다 상우하좌로 연결되어 있지 않은 그룹들의 개수를 찾으면 됨.

"""

from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

for t in range(T):
    M,N,K = map(int,input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        c,r = map(int,input().split())
        graph[r][c] = 1

    # 이 문제는 2중 루프를 이용해서 모든 그래프를 훑어봐야한다. 메모리 절약을 위해서 이미 탐색된 곳은 2로 처리하자.

    groups = 0

    for r in range(N):
        for c in range(M):
            # 만약 현재 위치에 배추가 있으면 BFS 작동
            if graph[r][c] == 1 :
                groups += 1
                q = deque()
                q.append([r,c])
                graph[r][c] = 2
                while q :
                    now_r,now_c = q.popleft()
                    for i in range (4):
                        next_r,next_c = now_r+dr[i],now_c+dc[i]
                        if 0<= next_r < N and 0<= next_c < M and graph[next_r][next_c] == 1:
                            graph[next_r][next_c] = 2
                            q.append([next_r,next_c])
            else :
                # 없어도 방문햇다는 표시하기.
                graph[r][c] = 2

    print(groups)


