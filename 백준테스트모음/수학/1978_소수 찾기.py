from collections import deque

N = int(input())
array = list(map(int,input().split()))
temp_dict = {}
for j in array:
    temp_dict[j] = 1

arrange_list = deque([i for i in range(2,max(array)+1)])
save_list = []

while arrange_list :

    now = arrange_list.popleft()

    temp_list = []

    while arrange_list :
        check = arrange_list.popleft()
        if check % now != 0 :
            temp_list.append(check)
        else :
            continue
    arrange_list = deque(temp_list)

    # 여기까지 왔다는 것은 소수라는 것임
    if temp_dict.get(now) is not None :
        save_list.append(now)

print(len(save_list))
