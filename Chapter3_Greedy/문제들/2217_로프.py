import sys
read = sys.stdin.readline
N = int(read())

weight_array = []
for _ in range(N):
    weight_array.append(int(read()))

# weight를 maximum 부터 k개를 세서 k개의 로프 중 제일 못드는 놈의 곱하기 k가 최대 출력 무게이다.
# 따라서 weight를 내림차순으로 정렬
weight_array.sort(reverse=True)

result_array = []
for k in range(N):
    maximum_weight = weight_array[k]*(k+1)
    result_array.append(maximum_weight)
print(max(result_array))