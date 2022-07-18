import sys
read = sys.stdin.readline

N = int(read())
array = sorted(list(map(int,read().split())))
M = int(read())

# 각 지방의 요청금액은 min(array)부터 max(요청금액) 까지로 볼 수 있다.
start = 0
end = max(array)

# 반복문을 돌면서 mid을 갱신한다.
while start <= end :
    mid = (start + end) // 2
    summation = 0
    # mid보다 작은 것들은 그냥 다 더하고, 큰것들은 mid만큼 더한다.
    for value in array :
        if value <= mid :
            summation += value
        else :
            summation += mid

    # 이진탐색을 위한 조건문 발동
    # 목표는 합계가 목표값보다 작거나 같아야한다.

    print("start : {} mid : {} end : {} summation : {} target : {}".format(start,mid,end,summation,M))
    # 만약 합계가 목표값보다 크면 mid를 줄여야한다 -> end를 mid-1로
    if summation > M :
        end = mid - 1
    # 만약 합계가 목표값보다 작거나 같으면(최대이면) -> start를 mid+1로
    else :
        start = mid + 1

print(start,mid,end,summation)

