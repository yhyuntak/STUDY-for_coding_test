import sys
input = sys.stdin.readline

S,C = map(int,input().split())
green_onions = []
for _ in range(S):
    green_onions.append(int(input()))

s = 1
e = max(green_onions)

while s<=e :

    m = (s+e)//2
    temp = 0
    for g in green_onions :
        temp += (g//m)
    if temp >= C :
        s = m+1
    else :
        e = m-1
rest = sum(green_onions)-e*C
# for g in green_onions :
#     rest += g%e

print(rest)