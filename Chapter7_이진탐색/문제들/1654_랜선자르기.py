import sys
read = sys.stdin.readline

K,N = map(int,read().split())
length_array = [0]*K

for i in range(K):
    length_array[i] = int(read())
#sort는 지금은 상관없다.

length_array.sort()

start = 1
end = max(length_array)

while (start<=end) :
    length = (start + end) // 2
    cnt = 0
    for j in range(K):
        cnt += length_array[j] // length # 랜선 자르고 개수 더하기
    # print("start : {} end : {} length : {} cnt : {} N : {}".format(start,end,length,cnt,N))
    if cnt >= N : start = length +1
    else :  end = length-1
print(end)


