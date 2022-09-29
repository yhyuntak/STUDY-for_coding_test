# 220907
"""
블로그 시작한지 N일이 지남
X일 동안 가장 많이 들어온 방문자 수와 그 기간들?을 알고싶다
X일동안 가장 많이 들어온 방문자 수와 기간이 몇개인지 구하자

"""

import sys
read =sys.stdin.readline
N,X = map(int,read().split())
blogs = [0]
blogs += list(map(int,read().split()))

# 이건 2개의 pointer를 X 간격 만큼 배치하고 하나씩 이동하면서 체크해야할 문제임
start_idx = 1
end_idx = start_idx+X
sliding_window = sum(blogs[start_idx:end_idx])
save_array = [sliding_window]

while end_idx <= N :
    sliding_window -= blogs[start_idx]
    sliding_window += blogs[end_idx]

    save_array.append(sliding_window)
    start_idx+=1
    end_idx+=1

maximum_val = max(save_array)
if maximum_val == 0 :
    print("SAD")
else :
    print(maximum_val)
    print(save_array.count(maximum_val))


# 220801
# def solution(N,X,array):
#
#     if max(array) == 0 :
#         print("SAD")
#         return None
#     # 인덱스 0부터 X만큼 멀어진 간격내를 매번 더하면서 탐색
#
#     # 슬라이딩 윈도우 문제라고 한다.
#     # 왼쪽부터 하나씩 진행할 것임. 단, 매번 모든 값을 더하는게 아니라
#     # 값을 넣었다 뺐다 하는 느낌으로 연산을 진행하는 듯하다. 이럼 매번
#     # 전체 list의 합을 할 필요가 없으니 좋은 듯.
#     # 시간초과 걸리는 이유가 X = 200,000 이면 매 루프마다 엄청난 연산이 필요하구나..
#     # 슬라이딩 윈도우를 쓰면 이런 문제를 해결할 수 있을 듯.
#
#     # 시작값을 최대로 초기화
#     max_val = sum(array[:X])
#     max_count = 1
#     temp_val = max_val
#     for i in range(X,N):
#         temp_val += array[i]
#         temp_val -= array[i-X]
#
#         if max_val == temp_val :
#             max_count += 1
#         elif max_val < temp_val :
#             max_val = temp_val
#             max_count = 1
#
#     print(max_val)
#     print(max_count)
#
#     return None
#
# N,X = map(int,input().split())
# array = list(map(int,input().split()))
# solution(N,X,array)