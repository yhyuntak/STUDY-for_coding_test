import copy
from collections import deque

N ,M = map(int,input().split())
friends = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)


# BFS로 한명씩 탐색하면서 베이컨의 수를 기록하자.
save_results = [0] # 0번째 인덱스를 버리기위해 0으로 초기화

origin_visited = [0 for _ in range(N+1)]

for person in range(1,N+1):
    # i번째 사람이 i를 제외한 나머지 사람들과 만나는 횟수를 저장해야함.
    temp_bacon = []
    for another in range(1,N+1):
        if another == person :
            continue
        # BFS 실행
        temp_visited = copy.deepcopy(origin_visited)
        q = deque()
        q.append([person,0])
        temp_visited[person] = 1

        while q:
            now_person,count = q.popleft()
            if now_person == another :
                temp_bacon.append(count)
                break
            for n in friends[now_person] :
                if temp_visited[n] == 0 :
                    temp_visited[n] = 1
                    q.append([n,count+1])
    save_results.append(sum(temp_bacon))

print(save_results.index(min(save_results[1:])))
