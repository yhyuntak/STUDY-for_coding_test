
"""
일이 끝나야 요금을 받는다고 생각하자.
"""

import sys
read = sys.stdin.readline

N = int(read())
days = []
for day in range(N):
    days.append(list(map(int,read().split())))
d = [0 for _ in range(N+1)]
max_fees = 0
for i in range(N):
    now_t,now_p = days[i]
    max_fees = max(max_fees,d[i])
    if i + now_t <= N :
        d[i+now_t] = max(max_fees+now_p, d[i+now_t])
print(max(d))

