
# 220926

"""
c개의 공유기를 n개의 집에 적당히 설치해서.. 가장 인접한 두 공유기 사이의 거리를 최대로하라.
와 .. 완전 생각의 전환이네 이거
문제 적으면서 주석으로 설명함.
"""

N,C = map(int,input().split())
iptime = []
for _ in range(N):
    iptime.append(int(input()))
iptime.sort()

# 첫번째 집과 마지막 집은 공유기의 최대 거리이다.
# 그리고 최소 거리는 집이 서로 거리 1로 이웃한 상태이므로 1이다.
# 이 두개를 이용해서 이분 탐색해서, 공유기를 한대씩 두면서 몇개의 공유기를 둘 수 있는지 확인하는 작업을!

min_dist = 1
max_dist = iptime[-1]-iptime[0]

len_iptime = len(iptime)
# 이제 이분 탐색시작
answer = 0

while min_dist <= max_dist :
    # 먼저 현재 공유기가 첫번째 집에 설치되어 있다고 가정하자.
    current_iptime = iptime[0]
    # 공유기와 공유기가 설치될 수 있는 기준이 될 거리 지정
    crit_dist = (min_dist+max_dist)//2
    # 이제 여기가 핵심이다. 각 공유기들을 현재 공유기와 비교하면서 거리를 재고, 기준이 되는 거리와 비교해서
    # 거리보다 크거나 같으면 공유기를 현재 공유기와 탐색된 공유기를 설치하자.
    # 그리고 count를 세서 crit_dist를 움직이는 여부로 작동시킨다. cnt는 현재 공유기가 설치되있다고 가정해서 1로 시작한다.
    cnt = 1
    for i in range(1,len_iptime) :
        temp_iptime = iptime[i]
        if temp_iptime-current_iptime >= crit_dist : # 비교해서 크거나 같으면
            cnt += 1 # temp도 설치시키자!
            # 그럼 이제 temp가 설치됬으니, 현재 설치된 공유기는 temp로 업데이트!
            current_iptime = iptime[i]

    # 위 과정을 거치면 현재 기준 거리로 공유기가 몇대까지 설치 되는지 cnt를 통해 알 수 있다.

    # cnt가 공유기의 수보다 크거나 같으면 기준 거리를 키우자.
    if cnt >= C :
        min_dist = crit_dist + 1
        answer = crit_dist
    else : # cnt가 공유기의 수보다 적으면 기준 거리를 줄이자.
        max_dist = crit_dist - 1

print(max_dist)