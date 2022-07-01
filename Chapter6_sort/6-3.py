array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1] : # 작으면 위치를 바꿔준다.
            array[j],array[j-1] = array[j-1],array[j]
        else : # 작지 않으면 이 위치가 맞다고 판단해서 for j 를 break
            break

print(array)
