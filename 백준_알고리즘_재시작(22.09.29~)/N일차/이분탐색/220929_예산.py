# 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다.
# 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법

"""
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.

2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
  상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

"""

# 일정 금액 이상은 다잘라버리고 최대치만 주고 나머지는 그냥 주는거네
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))
M = int(input())

min_val = 0
max_val = max(array)

# 이거 sys 한거랑 안한거랑 속도비교해보자

while min_val <= max_val :

    mid = (min_val+max_val)//2

    sums = 0
    for a in array :
        if a <= mid :
            sums += a
        else :
            sums += mid

    if sums > M : # 기준보다 크거나 같으면 금액을 더 낮춰야함.
        max_val = mid - 1
    else :
        min_val = mid + 1

print(max_val)

