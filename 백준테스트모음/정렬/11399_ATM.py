"""
사람들이 1번부터 n번까지.
i번 사람이 도ㅓㄴ을 인출하는 시간이 Pi분

이거 그냥 정렬하는문제인데?

"""

N = int(input())
array = []
temp = list(map(int,input().split()))
temp.sort()
sums = 0
temp_sum = 0
for i in range(N):
    temp_sum +=  temp[i]
    sums += temp_sum
    # print(temp_sum,sums)
print(sums)