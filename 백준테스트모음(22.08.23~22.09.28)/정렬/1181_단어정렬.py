import sys
read = sys.stdin.readline

N = int(read())
array= []
check_dict = {}
for _ in range(N):
    temp =read().split()
    temp = temp[0]
    if check_dict.get(temp) is None :
        check_dict[temp] = 1
        array.append(temp)
    # else :
    #     check_dict[temp] += 1


array.sort(key=lambda x:(len(x),x))
for a in range(len(array)):
    print(array[a])