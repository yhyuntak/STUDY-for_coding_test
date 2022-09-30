N = int(input())
start,end = map(int,input().split())
m = int(input())

array = [[] for _ in range(N+1)] # 사람은 N명이고 1번부터라서 N+1

for _ in range(m):
    parent,child = map(int,input().split())
    # 부모와 자식간의 방향성을 설정하지 말아야한다. 어디서 출발할지 모르니.
    array[parent].append(child)
    array[child].append(parent)

# 방문한 사람을 표현
visited = [0 for _ in range(N+1)]

# BFS로 start로 시작해서 end까지 가는 것을 생각.

from collections import deque
q = deque()
q.append([start])
visited[start] = 1

cnt_dict = {}
cnt_dict[start] = 0

while q :
    now_parent = q.popleft()
    now_parent = now_parent[0]

    for next_parent in array[now_parent] :
        if visited[next_parent] == 0 : # 아직 방문하지 않았으면
            cnt_dict[next_parent] = cnt_dict[now_parent]+1
            visited[next_parent] = 1
            q.append([next_parent])
    # print(q,cnt_dict)

try :
    if cnt_dict[end] == 0 :
        print(-1)
    else :
        print(cnt_dict[end])
except KeyError :
    print(-1)