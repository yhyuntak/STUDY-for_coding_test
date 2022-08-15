import sys
read = sys.stdin.readline
N = int(read())
M = int(read())

array = sorted(list(map(int,read().split())))

# 양끝을 처음으로 시작
# 값을 더했을 때, 목표값보다 작다면 왼쪽을 키워주고
# 목표값보다 크다면 오른쪽 값을 줄이자.
# left와 right 가 만나기 전까지 실행

left_idx = 0
right_idx = N-1

results = 0
while left_idx<right_idx :
    left = array[left_idx]
    right = array[right_idx]

    temp_sum = left+right
    if temp_sum == M :
        results+=1
        # 사용했으니 두 idx를 옮겨주자
        left_idx += 1
        right_idx -= 1
    elif temp_sum < M :
        # 더한게 작다면 left를 올리자
        left_idx += 1
    else :
        right_idx -= 1

print(results)

