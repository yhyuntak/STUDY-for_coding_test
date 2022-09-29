import sys
read = sys.stdin.readline
from collections import defaultdict

N = int(read())
array = []
for _ in range(N):
    array.append(int(read()))
array.sort()
for a in array :
    print(a)