"""

이중 루프를 돌아야함.
1일차~ N일차까지 돌건데,
먼저 N일차에 일을 끝낼 수 있는 T_i=1이 나오면 일단 더해.
그리고 1~N-1일차 중 N일차에 올 수 있는 것들과 N일차의 것을 더한 것과 N일차에 있는 것을 비교해서 더 큰 값을 취하면 끝.
"""

N = int(input())
schedule = [[]]
maximum = 0
for _ in range(N):
    schedule.append(list(map(int,input().split())))
d = [0 for _ in range(N+2)] # N+1일차에 정산해버리자.

for day in range(1,N+2):
    for prev in range(1,day):
        if prev + schedule[prev][0] <= day : # 1~N-1일차 중 일을 했을때, N일보다 작거나 같으면,
        #prev의 dp_table에 기록된 것 + prev 일차 와  있는 것을 비교해서 더 큰 값을 취하면 끝.
            d[day] = max(d[day],d[prev]+schedule[prev][1])
    #
    # # day+T_i가 N+1을 넘기면 안됌.
    # if day+T_i <= N+1 :
    #     print(day,T_i)
    #     d[day+T_i] = max(d[day+T_i],d[day]+P_i) # 원래 있던 것보다 지금 새로 하는 일 + 여태까지 해온 일이 더 많은 이득을 가져오면 바꾸자.
    #     print(d)
print(d[-1])