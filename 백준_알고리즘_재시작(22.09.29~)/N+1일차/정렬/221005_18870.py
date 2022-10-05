# 자기보다 작은 수의 개수를 세는 알고리즘

import sys
read = sys.stdin.readline

N= int(read())

array = list(map(int,read().split()))

arr2 = sorted(list(set(array))) # 이렇게하면 유니크한 값들만 남고, 정렬됨.
dic = {arr2[i] : i for i in range(len(arr2))} # 이렇게 dict을 짜면 아래에서 for문을 돌렸을 때, 좋음
# 왜냐하면 아래에서 for문으로 하나씩 값을 읊어봤자, 자신보다 작은게 몇개 있는지 파악하고 싶은거니까,
# dict에 저장된 자신의 len이 자기보다 아래에 몇개 있는지를 표현해주는 것임. 그래서 좋네

for i in array:
    print(dic[i], end = ' ')
