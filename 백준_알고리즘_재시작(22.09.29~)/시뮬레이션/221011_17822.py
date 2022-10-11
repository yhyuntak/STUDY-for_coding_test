"""


원판의 회전은 독립적으로 이루어진다.

회전 방향은 각각 반시계,시계다.

총 T번 회전

1. 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.

2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다. 아마 i번째 판의 j번째 수들을 기준으로 살펴보는 듯하다.
- 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
- 인접한 수가 없으면 원판의 평균보다 큰 값은 1을 더해주고 작은 것들은 -1을 해준다. (같은건 관리안하는듯)

"""

N,M,T = map(int,input().split())

circles = [[]]
from collections import deque
for m in range(N):
    # 이게 넣고 빼고 넣고 빼고를 해야해서 queue를 쓰는게 좋을 것 같다.
    # 그리고 M은 4개로 고정이 아니다.
    # 조건에서 i번째 판의 j번째 요소는 (i,j)로 표현되므로 i번째 queue에 j번째 요소를 생각하는게 맞다.
    temp = list(map(int,input().split()))
    circles.append(deque(temp))
idk = []
for _ in range(T):
    idk.append(list(map(int,input().split())))
t = 0
while t < T :
    # T번 움직일 것이다.
    # x: 원판의 번호 , d : 원판의 방향(시계-0,반시계-1), k : d방향으로 움직일 횟수
    i,d,k = idk[t]

    # 현재 원판 선택
    # 근데 배수로 진행됨.
    for i_p in range(i,N+1,i):
        now_circle = circles[i_p]
        # 원판의 방향 선택
        if d == 0 : #시계
            # k번 회전할 것이다.
            for k_ in range(k):
                # 시계방향이면 queue의 pop() -> appendleft() 순이다
                temp = now_circle.pop()
                now_circle.appendleft(temp)
        else : # 반시계
            # k번 회전할 것이다.
            for k_ in range(k):
                # 반시계방향이면 queue의 popleft() -> append() 순이다
                temp = now_circle.popleft()
                now_circle.append(temp)
        # 바뀐 판 저장
        circles[i_p] = now_circle

    # 회전했으면 이제 원판에 수가 남아있는지 확인하자.
    """
    근데 이게 원판 전체를 체크하는 거였다. 
    """
    save_near = [[] for _ in range(N+1)]
    # 근데 인접하면서 같은 수가 있었는지 체크하기 위해서 cnt를 도입하자.
    # cnt가 0이면 그런 수는 없는 거로해서 평균을 구해야한다.
    cnt = 0
    # i번째 원판의 j번째 요소들을 전부 체크하는 이중 루프 생성
    for i in range(1,N+1):
        now_circle = circles[i]

        # 비어있는 칸은 'x'로 표현할 것을 염두에 둘 것.
        # 원판에 수가 남아 있는지 확인하려면 'x'의 개수가 원판의 수의 개수랑 같은지 보자.
        if len(now_circle) != now_circle.count('x') : # 수가 남아 있다면
            # 인접하면서 수가 같은 것들을 찾는 알고리즘 실행
            # 1. 인접하면서 수가 같은게 있으면,
            # 근데 현재 남아있는 수의 index를 모르니 for문으로 접근하자.
            for j,val in enumerate(now_circle) :
                if val == 'x' :
                    continue
                else : # 비어있지 않은 수
                    # 인접한 것들을 찾자. 원판들끼리와 원판 내부를 동시에 체크
                    """
                    근데 이게 아마 문제에 원판 내에서 인접하면서 동시에 원판들끼리 비교해도 인접한게 있을 것 같다. 
                    # 그럼 'x'로 바꿀 위치들만 따로 저장해서 마지막에 바꿔주는게 맞다.
                    """
                    # 인접한 것의 조건은 먼저 2가지를 고려해야한다.
                    # 1. 현재 판이 제일 안쪽판(1)인가 제일 마지막인가(M) -> 원판들 끼리 비교
                    # j번째 요소의 원판의 좌우를 확인
                    # print("{}번째 판의 {}번째 요소 값 : {} 현재 서클 : {}".format(i,j+1,val,now_circle))
                    for c_ in [-1,1]:
                        check_circle = i+c_
                        if check_circle <= 0 : # 만약 0보다 작으면 continue.
                            continue
                        elif check_circle > N : # 만약 N보다 크면 continue
                            continue
                        else : # 해당되면
                            if now_circle[j] == circles[check_circle][j] :
                                if j not in save_near[i] : # 현재 원판만 이걸 고려하면 된다.
                                    save_near[i].append(j)
                                    save_near[check_circle].append(j)
                                    # now_circle[j] = 'x'
                                    # circles[i+c_][j] = 'x'
                                    cnt += 1
                    # 2. 현재 판의 요소가 M번째 요소인가 1번째 요소인가에 따라 다르게.
                    # 이제 원판 내부에서 비교를 시작해보자.
                    # 현재 j번째 요소를 살펴보는 중이었다.
                    for c__ in [-1,1]: # 좌우를 살피면 된다.
                        check_element = (j+c__)%M
                        if now_circle[j] == circles[i][check_element] :
                            if check_element not in save_near[i]:  # 현재 원판만 이걸 고려하면 된다.
                                save_near[i].append(check_element)
                            if j not in save_near[i]:  # 현재 원판만 이걸 고려하면 된다.
                                save_near[i].append(j)
                                # now_circle[j] = 'x'
                                # circles[i+c_][j] = 'x'
                                cnt += 1
        else :
            # 수가 남아있지 않다면 continue다.
            continue

    # print(save_near)
    # 만약 바꿔줄게 하나도 없었으면 모든 원판의 적힌 수의 평균을 기준으로 값을 조정해야하네.
    if cnt == 0 :
        # 평균 알고리즘 실행
        sums = 0
        sums_cnt = 0
        for iii in range(1,N+1):
            for jjj in range(M):
                if circles[iii][jjj] != 'x' :
                    sums += circles[iii][jjj]
                    sums_cnt += 1
        if sums_cnt == 0 :
            t = 10e9
        else :
            means = sums/sums_cnt
            for iii in range(1,N+1):
                for jjj in range(M):
                    if circles[iii][jjj] != 'x' :
                        if circles[iii][jjj] > means :
                            circles[iii][jjj] -=1
                        elif circles[iii][jjj] < means :
                            circles[iii][jjj] += 1

    else : # save_near에 따라 정보 수정.
        for iiii,sn in enumerate(save_near):
            sn = save_near[iiii]
            if len(sn) > 0 :
                for snn in sn :
                    circles[iiii][snn] = 'x'
    t+=1
# T번 회전한 후 원판들의 수를 더한다.
# print(circles)
results = 0
for iii in range(1, N + 1):
    for jjj in range(M):
        if circles[iii][jjj] != 'x':
            results += circles[iii][jjj]
print(results)