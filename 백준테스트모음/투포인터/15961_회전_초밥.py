"""
같은 초밥이 2개 있을수도

2가지 행사

1. k개의 접시를 연속해서 먹는다면 할인된 정액 가격으로 제공
2. 1번을 참여하면 초밥 하나를 무료로 제공. 벨트위에 없더라도 제공함

가능한한 다양한 초밥을 먹으려고 한다.


"""
import sys
read = sys.stdin.readline

from collections import Counter

N,d,k,c = map(int,read().split())
circle_array = []
for _ in range(N):
    circle_array.append(int(read()))

# 연속적인 개념이니 슬라이딩 윈도우를 적용해보자.
# 초기값 설정
from collections import defaultdict
hash_dict = defaultdict(int)
# 보너스는 무조건 먹으니 +1
hash_dict[c] = 1

start_idx = 0
end_idx = 0
for i in range(k):
    hash_dict[circle_array[i]] += 1
    end_idx+=1

# result_array = [0 for _ in range(N)]
# result_array[0] = len(hash_dict)
max_val = len(hash_dict)
# 슬라이딩 윈도우를 하면서 뺏다 더했다 하기
while start_idx != N :
    # print(hash_dict)
    hash_dict[circle_array[end_idx]] += 1
    hash_dict[circle_array[start_idx]] -= 1

    if hash_dict[circle_array[start_idx]] == 0 :
        del hash_dict[circle_array[start_idx]]
    max_val = max(max_val,len(hash_dict.keys()))
    start_idx+=1
    end_idx+=1
    end_idx %= N

print(max_val)
