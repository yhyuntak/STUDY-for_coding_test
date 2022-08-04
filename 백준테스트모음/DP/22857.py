import sys
read = sys.stdin.readline

N,K = map(int,read().split())
array = list(map(int,read().split()))

# 이 문제는 슬라이딩윈도우 문제인거 같은데
# 일단 값을 하나씩 먹어가면서 최대 길이를 저장하자.
# 다음 값을 확인했을 때, 최대 길이가 갱신된다면, 교체하는 느낌.

# 먼저 시작 지점을 찾자.
max_val = 0
for start,a in enumerate(array) :
    if a % 2 == 0 :
        max_val = 1
        break

from collections import deque
temp_window = deque([a])

count = 0
for aa in range(start+1,len(array)) :
    now = array[aa]
    if now % 2 == 1 :
        # K가 0인데 홀수를 만나면 현재 홀수를 추가하고
        # 앞에 K가 홀수인 것을 뺄때까지 pop하기.
        if K - count <= 0 :
            while K-count <= 0:
                temp_val = temp_window.popleft()
                if temp_val % 2 == 1 :
                    count -= 1
                else :
                    continue
        count += 1
        # 깎고 temp_window에 일단 추가
        temp_window.append(now)
    else :
        temp_window.append(now)

    max_val = max(max_val,len(temp_window)-count)
    # print(count,temp_window,max_val)
print(max_val)
