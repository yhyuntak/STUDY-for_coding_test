N =int(input())
array = []
for _ in range(N):
    array.append(list(map(int,input().split())))

array.sort(key=lambda x : [x[0],x[1]])
for a in array :
    print(*a)