import sys
read = sys.stdin.readline

N = int(input())
g = list(map(int,input().split()))

d = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if g[i] > g[j] : # 이어 붙일 수 있다는 증거
            d[i] = max(d[j]+1,d[i])
print(max(d))

