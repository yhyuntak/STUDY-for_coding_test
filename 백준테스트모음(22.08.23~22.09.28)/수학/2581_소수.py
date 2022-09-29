

"""
에라토스테네의 체를 이용하면 범위내에 있는 소수들을 빠르게 찾을 수 있다.

"""

def check_value(val):

    return

M = int(input())
N = int(input())

"""
M이상 N이하의 수들 중 소수를 찾기 위해
2부터 N까지의 수를 일단 나열해보자.
"""
from collections import deque

array = deque([i for i in range(2,N+1)])
# 에라토스테네스의 체는 다음과 같은 방식
# array에서 제일 작은 수부터 하나씩 꺼내서, 나눠지는 수들은 다 빼버린다.
# 그리고 현재 선택된 수를 저장한다.
# 나눠지는 수가 없더라도 그냥 저장한다.
# 저장된 수들이 소수들이다.

# 그렇다면 array를 queue로 만들면 편할 듯.
save_array = []
while array :
    now = array.popleft()
    temp_array = deque()
    for i in range(len(array)) :
        # 남은 array를 돌리면서 나눠지는게 있으면 pop상태로 두기
        temp = array.popleft()
        if temp % now == 0 :
            continue
        else :
            # 0이 아니라면 나눠지지 않는 것이므로 temp_array에 저장
            temp_array.append(temp)
    # array를 temp_array로 갱신
    # temp_array는 나눠지지 않은 목록들을 갖고 있다.
    array = temp_array
    if now >= M :
        save_array.append(now)
if len(save_array) == 0 :
    print(-1)
else :
    print(sum(save_array))
    print(min(save_array))
