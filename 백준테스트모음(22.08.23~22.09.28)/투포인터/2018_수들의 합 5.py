
N = int(input())
now, end = 0, 1
ans = 0
# 1부터 N까지 훑기
for start in range(1,N+1):
    # end를 먼저 움직이고 start를 끌고가는 느낌.
    # now가 N보다 작고 end도 N보다 작아야 while문 돌기.
    while end < N and now < N :
        # now에 end 더하기.
        now += end
        # end를 다음 수로 보내기
        end += 1
    # loop가 깨졌을 때, now가 N이라면, start~end가 N을 만들 수 있는 연속된 자연수의 set이다.
    if now == N :
        ans+=1
    # 마지막으로 now에 start를 빼줌으로써 start를 끌고오기
    now -= start

print(ans+1)

