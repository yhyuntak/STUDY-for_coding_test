from collections import deque

N,K = map(int,input().split())

array = deque([i for i in range(2,N+1)])

count = 0
save_array = []
while array :
    now = array.popleft()
    # p를 지우고
    count += 1
    if count == K :
        print(now)
        break

    temp_array = []
    while array :
        temp = array.popleft()
        if temp % now == 0 :
            count += 1
        else :
            temp_array.append(temp)
        if count == K :
            break
    if count == K :
        print(temp)
        break
    array = deque(temp_array)
