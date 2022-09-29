import sys
read = sys.stdin.readline
N = int(read())
array = []
for _ in range(N):
    array.append(int(read()))

# 역순으로 정렬하면, 가장 비싼것들부터 나열됨.
array.sort(reverse=True)
# 가장 비싼것들 중 3번째 있는 건 가장 싼거보다 비싼건 맞으니까. 차라리 싼걸 돈 내는게 절약하는 방법.
from collections import deque
array = deque(array)
result = 0
while array :
    if len(array) >= 3:
        a = array.popleft()
        b = array.popleft()
        array.popleft()
        result = result + a + b
    else :
        result += sum(array)
        break

print(result)
#
