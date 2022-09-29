


#220914

import sys
read = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    temp = read()
    temp = temp[:-1]
    temp_array = [ int(t) for t in temp]
    graph.append(temp_array)

# BFS로 탐색하면서 집 번호를 매길 변수가 있어야함
house_number = 1
# 각 house의 수를 저장할 array를 만들자.
house_array = []

# 이제 BFS를 하면서 집 찾기.

# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

from collections import deque
visited = [[0 for _ in range(N)] for _ in range(N)]

# 이 문제는 그래프를 전부 돌아야함 무조건
for r in range(N):
    for c in range(N):
        # BFS가 발동하는 조건은 해당 위치의 번호가 1일때임.
        now_house = graph[r][c]
        # 이때 단지 수도 세자
        if now_house == 1 :
            q = deque()
            q.append([r,c])
            graph[r][c] = 0
            counts = 1
            while q:
                now_r, now_c = q.popleft()
                for i in range(4):
                    next_r, next_c = now_r + dr[i], now_c + dc[i]
                    if 0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] == 1 :
                        # 큐에 넣고  단지 수 카운트
                        q.append([next_r,next_c])
                        # 그리고 해당 집번호를 삭제하자.
                        graph[next_r][next_c] = 0
                        counts += 1

            house_array.append(counts)

        # 그렇지 않다면 continue 하자

len_house = len(house_array)
house_array.sort()
print(len_house)
for j in range(len_house):
    print(house_array[j])