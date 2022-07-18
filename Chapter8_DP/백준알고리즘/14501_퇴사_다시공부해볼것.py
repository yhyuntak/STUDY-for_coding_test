import sys
readline = sys.stdin.readline

N = int(readline())
T, P = [], []
for _ in range(N):
    t, p = map(int, readline().split())
    T.append(t)
    P.append(p)

d = [0] * (N+1)

for i in range(N - 1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않음
    if i + T[i] > N:
        d[i] = d[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        d[i] = max(d[i+1], P[i] + d[i + T[i]])

print(d[0])