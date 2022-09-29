"""
규칙 2개
1. 포도주 선택시, 모두 마시고 다시 원위치
2. 연속으로 놓여있는 3잔을 마실 수 없다.

될수있는대로 많이 맛볼 것이고, 1부터 n까지의 포도주 잔이 있다.

ex)
6 10 13 9 8 1이 있으면
6 10 9 8 을 마셔서 33을 최대로 먹을 수 있다.

"""

"""
d[i] = g[i] + (g[i-1]+d[i-3] vs d[i-2])

d[1] = 6
d[2] = 10+6
d[3] = 13+10
d[4] = 9 + (13+d[1] vs d[2]) = 9 + (13+6 vs 10+6) = 6 13 9
d[5] = 8 + (9+d[2] vs d[3]) = 8 + (9+16 vs 13+10) = 6 10 9 8
d[6] = 1 + (8+d[3] vs d[4]) = 1 + (8+13+10 vs 6+13+9) = 8+13+10+1 


"""

import sys
read = sys.stdin.readline

n = int(read())
array = [0]
d = [0 for _ in range(n+1)]

for _ in range(n):
    array.append(int(read()))

if n == 1 :
    print(array[1])
elif n == 2 :
    print(sum(array))
else :
    d[1] = array[1]
    d[2] = array[2] + array[1]
    for i in range(3,n+1):
        d[i] = array[i] + max( array[i-1]+d[i-3] , d[i-2])
        d[i] = max(d[i],d[i-1])
    print(d[-1])