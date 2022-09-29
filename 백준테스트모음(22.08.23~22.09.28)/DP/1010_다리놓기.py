# 220921
# 서쪽에 N개, 동쪽에 M개 있다
"""
겹쳐서 지을 수 없다.
"""

T = int(input())

# 그래프를 그려서 규칙을 찾아보는 방법도 좋은듯.
d = [[0 for _ in range(31)] for _ in range(31)]

for n in range(1,31):
    for m in range(1,31):
        if n == 1 :
            d[n][m] = m
        else :
            d[n][m] = d[n][m-1] + d[n-1][m-1]

for _ in range(T):
    N,M = map(int,input().split())
    print(d[N][M])



