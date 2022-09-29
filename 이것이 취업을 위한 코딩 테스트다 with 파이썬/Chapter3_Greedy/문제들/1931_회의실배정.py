import sys
read = sys.stdin.readline

N = int(read())
time_array = []
for i in range(N):
    time_array.append(list(map(int,read().split())))

# 회의가 빨리 끝나는 순대로 정렬하자. 그래서 제일 빨리 끝나는 것을 시작으로 다음 타임에 바로 올 수 있는걸 가져오는거지.
print(time_array)
# time_array.sort(key = lambda x: x[0])
# print(time_array)
time_array.sort(key=lambda x: x[1])
print(time_array)
count = 1
end = time_array[0][1]
for j in range(1,N):
    if time_array[j][0] >= end :
        count +=1
        end = time_array[j][1]

print(count)

