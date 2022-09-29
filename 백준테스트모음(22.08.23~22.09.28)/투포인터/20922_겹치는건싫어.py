import sys
read = sys.stdin.readline

N,K = map(int,read().split())
array = list(map(int,input().split()))

# 이거 다 돌수밖에없지만
# 이것도 슬라이딩 윈도우 문제인듯.

save_dict = {}
from collections import deque

save_list = deque()
best_length = 0
for a in array :


    if save_dict.get(a) is None:
        save_list.append(a)
        save_dict[a] = 1
    else :
        # 여기선 K를 넘냐 안넘냐를 확인.
        # print(a,save_dict.get(a),save_list)
        if save_dict.get(a) >= K :
            # 파악한 후, 슬라이딩윈도우 방식으로 처음 요소를 제거하고 마지막 요소를 추가해.
            # 근데 중복되는 요소가 어디에 있는지 알 수 없음 그러니까 여기서 지금 수 a가 줄때까지
            # 숫자를 버려버려야해. 동시에 dict의 수도 줄이기.
            while save_dict.get(a) >= K :
                left_val = save_list.popleft()
                # print(save_list)
                save_dict[left_val] -= 1

            # 끝나면 다시 원래대로 for문으로 돌아간다.
            save_list.append(a)
            save_dict[a] += 1
        else :
            save_list.append(a)
            save_dict[a] += 1

    best_length = max(best_length,len(save_list))

print(best_length)