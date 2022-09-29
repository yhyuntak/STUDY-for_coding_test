#220907
"""
피보나치는 0,1,1,2,... 해서 d[i] = d[i-1] + d[i-2] 로 구성된다.
n이 주어졌을 때, n번째 수는?
"""

n = int(input())
d = [0 for _ in range(n+1)]

if n >= 1 :

    d[1]=1

    for i in range(2,n+1):
        d[i] = d[i-1] + d[i-2]
    print(d[n])

else :
    print(d[n])