import sys
input= sys.stdin.readline

N,M = map(int,input().split())

people_dict = {}

for _ in range(N):
    temp = input().split()
    temp=temp[0]
    people_dict[temp] = 1

hear_watch = []
cnt = 0
for _ in range(M):
    temp = input().split()
    temp=temp[0]
    try: people_dict[temp] += 1
    except KeyError : people_dict[temp] = 1

    if people_dict[temp] == 2 :
        hear_watch.append(temp)
        cnt +=1

hear_watch.sort()
print(cnt)
for i in range(cnt):
    print(hear_watch[i])

