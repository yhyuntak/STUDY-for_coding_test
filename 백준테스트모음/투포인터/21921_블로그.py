def solution(N,X,array):

    if max(array) == 0 :
        print("SAD")
        return None
    # 인덱스 0부터 X만큼 멀어진 간격내를 매번 더하면서 탐색

    # 슬라이딩 윈도우 문제라고 한다.
    # 왼쪽부터 하나씩 진행할 것임. 단, 매번 모든 값을 더하는게 아니라
    # 값을 넣었다 뺐다 하는 느낌으로 연산을 진행하는 듯하다. 이럼 매번
    # 전체 list의 합을 할 필요가 없으니 좋은 듯.
    # 시간초과 걸리는 이유가 X = 200,000 이면 매 루프마다 엄청난 연산이 필요하구나..
    # 슬라이딩 윈도우를 쓰면 이런 문제를 해결할 수 있을 듯.

    # 시작값을 최대로 초기화
    max_val = sum(array[:X])
    max_count = 1
    temp_val = max_val
    for i in range(X,N):
        temp_val += array[i]
        temp_val -= array[i-X]

        if max_val == temp_val :
            max_count += 1
        elif max_val < temp_val :
            max_val = temp_val
            max_count = 1

    print(max_val)
    print(max_count)

    return None

N,X = map(int,input().split())
array = list(map(int,input().split()))
solution(N,X,array)