# 220916 (복기하기위해 한번더)

N = int(input())
d = [10e5 for _ in range(N+1)]
d[0] = 0

for day in range(3,N+1):
    if day-5 >= 0 and d[day-5] != 10e5:
        d[day] = min(d[day],d[day-5]+1)

    if d[day-3] != 10e5 :
        d[day] = min(d[day],d[day-3]+1)


if d[N] != 10e5 :
    print(d[N])
else :
    print(-1)


# 220914 (dp로품)
"""
설탕 N키로 배달을.
3과 5키로가 있음

최대한 적은 봉지의 수를.

정확히 N키로를 만들자. 최소의 봉지로

"""

N = int(input())
d = [10e5 for _ in range(N+1)]
d[0] = 0
for i in range(3,N+1):
    # 먼저 5로 나눠보는게 가장 봉지의 수를 줄이는 것임.
    if i-5 >= 0 and d[i-5] != 10e5 :
        d[i] = min(d[i],d[i-5]+1)
    if d[i-3] != 10e5 :
        d[i] = min(d[i],d[i-3]+1)
if d[N] != 10e5 :
    print(d[N])
else :
    print(-1)