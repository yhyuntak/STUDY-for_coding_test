N = int(input())
d = [0] * (N+1)
INF = 1e9
d[1] = INF
d[2] = INF

for i in range(3,N+1):
    if i == 3 :
        d[i] = 1
        continue
    elif i == 4 :
        d[i] = INF
        continue
    a = i-3
    b = i-5

    d[i] = min(d[a],d[b])+1

if d[N] < 1e7 :
    print(d[N])
else :
    print(-1)