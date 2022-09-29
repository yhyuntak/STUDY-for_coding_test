import sys
read =sys.stdin.readline
T = int(read())
result_array = []
for _ in range(T):
    N = int(read())
    array = []
    for _ in range(N):
        x,y = map(int,read().split())
        if x == 1 : interview = [x,y]
        else : array.append([x,y])
    array.sort()
    cnt = 1
    for i in range(N-1):
        now = array[i]
        if now[1] < interview[1] and now[0]>interview[0]:
            cnt += 1
            interview = now
    result_array.append(cnt)

for m in range(T):
    print(result_array[m])