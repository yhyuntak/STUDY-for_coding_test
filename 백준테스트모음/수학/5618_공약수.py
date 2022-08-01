import sys
read = sys.stdin.readline
import math

T = int(read())

N_list = list(map(int,read().split()))

# 공약수로 최댓값이 나눠지는지 확인하자.
# 왜냐하면 최댓값의 약수로 해야 모든 경우를 체크할 수 있기 때문.
N_list.sort()
max_N = max(N_list)
root_max_N = math.floor(math.sqrt(max_N))

common_array = []
for commom_val in range(1,root_max_N+1):
    if max_N % commom_val == 0 : # 나눠떨어진다면,
        # 최댓값의 공약수들을 저장하자
        common_array.append(commom_val)
        common_array.append(int(max_N // commom_val))


common_array.sort()
N_list.sort(reverse=True)
# 최댓값의 공약수들로 다른 수들을 나눠서 나눠지면 출력하기로 끝
for common in common_array:
    # 다른 수들도 나눠떨어지는지 확인할 것
    count = 1
    for j in range(1,T) :
        if N_list[j] % common == 0:
            count += 1
    # 나눠 떨어진다면 ( count == T ) 추가하기
    if count == T :
        print(common)