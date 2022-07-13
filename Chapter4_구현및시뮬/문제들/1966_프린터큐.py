import sys
read = sys.stdin.readline
from collections import deque

T = int(input())
N_array = []
M_array = []
K_array = []

for t in range(T):

    N, M = map(int, read().split())
    # N은 문서의 개수, M은 내가 궁금한 문서가 현재 몇번째에 놓여있는지
    K = list(map(int, read().split()))

    N_array.append(N)
    M_array.append(M)
    K_array.append(K)

cnt_array = []

for i in range(T):

    N = N_array[i]
    M = M_array[i]
    K = K_array[i]

    q = deque(K)
    ordered = [-1]*N
    ordered[M] = 1
    q_ordered = deque(ordered)
    cnt = 0

    # 무한 루프를 돌아야함.
    while True :
        now = q.popleft()
        now_orderd = q_ordered.popleft()
        # q에서 자신을 제외되었고,
        # 남은 queue에서 자기보다 큰게 없으면 출력하면 되니까 max()를 사용하자
        if len(q) < 1 :
            cnt += 1
            cnt_array.append(cnt)
            break
        if max(q) <= now :
            cnt += 1
            if now_orderd == 1 :
                cnt_array.append(cnt)
                break
        # 만약 자신보다 큰게 존재한다면, 다시 queue의 오른쪽에 넣자.
        else :
            q.append(now)
            q_ordered.append(now_orderd)

for z in range(len(cnt_array)):

    print(cnt_array[z])