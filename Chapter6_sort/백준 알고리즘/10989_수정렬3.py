# 이 문제는 계수정렬 문제이다.
# 특정한 조건 하에서만 아주 효율적으로 작동한다.
import sys
read = sys.stdin.readline

N = int(read())

array = [0] * 10001
for j in range(N):
    array[int(read())] += 1

for i in range(10001):
    if array[i] != 0 :
        # 0이 아니면 입력받을 때 해당 숫자가 나왔었다는 것을 의미
        for k in range(array[i]):
            print(i)
