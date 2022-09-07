#220907
import math

n = int(input())
array = list(map(int,input().split()))
a = array[0]
b = array[1]
aa,bb = a,b
while a%b != 0:
    a,b = b,a%b

# 최대 공약수 : b
# 최소 공배수 : aa*bb//b

# 이 문제는 공약수들을 구하는 것이니.. 최대 공약수의 약수들을 구하면 될 것 같다.
temp = []
for i in range(1,math.floor(math.sqrt(b))+1):
    if b % i == 0 :
        temp.append(i)
        if i != b//i :
            temp.append(b//i)
temp.sort()
if n == 2:
    for j in temp :
        print(j)
else :
    for j in temp :
        if array[2] % j == 0:
            print(j)
