
save_cases = {}
count = 0
while True :

    temp_list = list(input().split())

    if str(-1) in temp_list:
        break
    elif len(temp_list) == 0 :
        count+=1
    else :
        temp_list = list(map(int,temp_list))
        if save_cases.get(count) is None :
            save_cases[count] = temp_list
        else :
            save_cases[count] += temp_list

from collections import deque

def check_tree(now_list):

    now_queue = deque(now_list)
    now_graph = {}
    overlap_graph = {}
    overlap_graph2 = {}

    for pop_q in range(len(now_list)):
        start = now_queue.popleft()
        end = now_queue.popleft()

        if start == 0 or end == 0 :
            break

        if now_graph.get(start) is None :
            now_graph[start] = [end]
        else :
            now_graph[start] += [end]

        if overlap_graph.get(start) is None:
            overlap_graph[start] = 0
            overlap_graph2[start] = 0
        if overlap_graph.get(end) is None:
            overlap_graph[end] = 0
            overlap_graph2[end] = 0

    # overlap_graph는 0이 하나고 나머지는 다 1이어야한다.
    # 우선 루트를 찾아야하니까 bfs로 돌면서 방문하지 않는 곳이 있는지 확인하자.
    q = deque()
    if len(now_graph.keys()) == 0 :
        return 1
    temp_list = list(now_graph.keys())
    for t in temp_list:
        q.append(now_graph[t])
    while q :
        now = q.popleft()
        for n in now :
            overlap_graph[n] += 1
    if list(overlap_graph.values()).count(0) != 1 :
        return -1
    else :
        temp_ = list(overlap_graph.keys())
        root_idx = list(overlap_graph.values()).index(0)
        root_node = temp_[root_idx]

        # root를 찾았으면 이 root를 기점으로 bfs를 다시 전개해서 count를 하자.

        last_q = deque()
        last_q.append(now_graph[root_node])
        while last_q :
            now_q = last_q.popleft()
            for nq in now_q :
                overlap_graph2[nq] += 1
                if now_graph.get(nq) is None :
                    last_q.append([])
                else :
                    last_q.append(now_graph[nq])

        if max(overlap_graph2.values()) != 1 :
            return -1
        else :
            return 1

f = 1

for i in range(len(save_cases.keys())) :
    now_list = save_cases[i]
    if check_tree(now_list) == 1:
        print("Case {} is a tree.".format(f))
    else :
        print("Case {} is not a tree.".format(f))
    f+=1