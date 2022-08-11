import sys
read =sys.stdin.readline
from collections import deque

N= int(read())
array = list(map(int,read().split()))

d = [a for a in array]
# d[0].append(array[0])
g = array
for i in range(1,N):
    for j in range(i):
        if g[i] > g[j] :
            d[i] = max(d[j] + g[i] , d[i])
        # 아닐 경우 그대로 유지.
# print(d)
print(max(d))

"""
5
3 2 4 2 1
"""