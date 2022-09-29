def binary_search(array,target,start_idx,end_idx):

    if start_idx > end_idx :
        return False
    mid_idx = (start_idx+end_idx)//2

    # mid_idx가 target과 일치하면 True 반환
    # 이 조건이 recursive를 끝내는 주 조건문이 된다.

    if target == array[mid_idx]:
        return True

    # mid보다 target이 왼쪽에 있을 경우(작을경우) end idx를 mid idx로 업데이트 후 recursive 실행
    elif target < array[mid_idx] :
        return binary_search(array,target,start_idx,mid_idx-1)
    elif target > array[mid_idx] :
        return binary_search(array,target,mid_idx+1,end_idx)

import sys
read = sys.stdin.readline

N = int(input())
N_array = list(map(int,read().split()))

# 이진 탐색에서 핵심은 array를 오름차순으로 정렬하는 것!!
# 어차피 지금 문제는 수가 있냐 없냐를 표현하는 것이므로 정렬하자!
N_array.sort()

M = int(read())
M_array = list(map(int,read().split()))


for i in range(M):
    target = M_array[i]
    print(int(binary_search(N_array,target,0,N-1)))

