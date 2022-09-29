"""
해결 : 파랑
해결 못 : 빨강

칠하는 방법
1. 연속된 문제 선택
2. 전부 원하는 같은 색으로

파란색의 시작과 끝을 찾고 칠하고
그 안에 빨간색들을 칠하면 최적.?

그냥 다 파란색으로 치하고 빨간색으로 칠하면 되는거 아님? -> X
전부 파란색으로 칠했다고 가정하자 -> +1
그리고 for문으로 돌면서 빨강으로 시작해서 빨강으로 끝나는 지점을 찾고 (연속해서 칠해야함으로) 묶어서 +1 처리

"""
import sys
from collections import deque
read = sys.stdin.readline
N = int(read())
array = read().split()
array = array[0]

# 이 문제는 각각 연속해있는 갯수를 구하자.
# 그리고 연속한 값이 더 적은 것에 +1을 하면 된다.
before = array[0]

red_count = 0
blue_count = 0
for i in range(1,len(array)) :
    if before != array[i] : # 이전 것과 현재가 다르면
        # 이전 값이 B면 이전 값을 R로 갱신
        if before == "B" :
            # 그러면서 B의 카운트를 세기
            blue_count += 1
            # print(before,array[i],blue_count,red_count)
            before = "R"
        else :
            # 그러면서 R의 카운트를 세기
            red_count += 1
            # print(before, array[i], blue_count, red_count)
            before = "B"
# 다 끝났을 때 마지막 체크
if before == "B":
    blue_count +=1
else :
    red_count +=1
print(min(blue_count,red_count)+1)
