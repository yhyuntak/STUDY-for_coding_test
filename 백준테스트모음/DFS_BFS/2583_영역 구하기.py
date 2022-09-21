
# 220921 못품 다시풀자.

import sys
read= sys.stdin.readline

M,N,K = map(int,input().split())

# 자신 하 우 우하
dr = [0,1,0,1]
dc = [0,0,1,1]

check_graph = [[0 for _ in range(N+1)] for _ in range(M+1)]
for _ in range(K):
    lb_c,lb_r,ru_c,ru_r = map(int,read().split())
    # 빗금 그래프에서 점을 찍어야할 곳들을 다 1로 체킹해놓자.
    for r in range(M-ru_r,M-lb_r):
        for c in range(lb_c,ru_c):
            print(r,c)
            for i in range(4):
                check_graph[r+dr[i]][c+dc[i]] = 1
    for a in range(M):
        print(check_graph[a])

    print()

# 박스가 만들어진 것을 확인하기 위한 그래프를 생성
box_graph = [[0 for _ in range(N)] for _ in range(M)]

# 4개의 꼭지점 체크하는 함수
def check_box(row,col):
    sum = 0
    for i in range(4):
        sum += check_graph[r+dr[i]][c+dc[i]]
    if sum != 4 :
        return 0
    else :
        return 1

# 4개의 꼭지점 중 하나라도 포함되어있지 않다면 영역이 살아있다는 뜻.
# 죽은 공간을 box_graph에 체크하자.
for r in range(M):
    for c in range(N):
        box_graph[r][c] = check_box(r,c)

for a in range(M):
    print(box_graph[a])

# 이제 BFS로 공간 체크만 하면 끝.

from collections import deque

# 상 우 하 좌
ddr = [-1,0,1,0]
ddc = [0,1,0,-1]

results_array = []

for r in range(M):
    for c in range(N):
        if box_graph[r][c] == 0 :
            groups = 1
            q = deque()
            q.append([r,c])
            box_graph[r][c] = 1
            while q:
                now_r,now_c = q.popleft()
                for k in range(4):
                    next_r ,next_c = now_r+ddr[k] ,now_c+ddc[k]
                    if 0<=next_r<M and 0<=next_c<N and box_graph[next_r][next_c] == 0 :
                        q.append([next_r,next_c])
                        box_graph[next_r][next_c] = 1
                        groups+=1

            results_array.append(groups)
results_array.sort()
print(len(results_array))
print(*results_array)
