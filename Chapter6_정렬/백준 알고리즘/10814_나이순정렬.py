import sys
read = sys.stdin.readline

N = int(read())
age_array = [0]*201 # 1살~200살
member_array = []
for i in range(N):
    age,name = read().split()
    age = int(age)
    ordered = age_array[age] + 1
    age_array[age] += 1
    member_array.append([age,name,ordered])
member_array.sort(key=lambda x:(x[0],x[2]))
# member_array.sort(key=lambda x:x[2])
for j in range(N):
    print("{} {}".format(member_array[j][0],member_array[j][1]))

