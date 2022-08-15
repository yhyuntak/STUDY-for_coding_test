N = int(input())
cow_dict = {}
count = 0

for _ in range(N):
    cow,loc = map(int,input().split())

    if cow_dict.get(cow) is None :
        cow_dict[cow] = loc
    # 이제 소가 길을 건너는지 확인하자.
    else :
        before_loc = cow_dict[cow]

        # 위치가 바뀌었으면 count를 세자
        if before_loc !=  loc :
            count += 1

        # 다시 갱신
        cow_dict[cow] = loc

print(count)