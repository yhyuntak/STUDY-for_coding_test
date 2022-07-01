'''
뭔가 계산이 연속적으로 되어있으니까 DP를 떠올려야 될듯??
피보나치도 계속해서 계산이 되는 모양이니까!

그리고 /5,/3,/2,-1의 조합이 무수히 많은데 그중에서 가장 작은 것을 골라야하므로
그리디 방법으로 접근하면 안된다.
'''

x = int(input())

# 5,3,2 순으로 나눠보고..?

d=[0]*30001

for i in range(2,x+1):
    d[i] = d[i-1]+1

    if i %2 == 0 :
        d[i] = 

count = 0



while x != 1 :

    if x // 5 != 0:
        count += 1
        count += x % 5
        x -= x % 5
        x = x // 5

    elif x // 3 != 0:
        count += 1
        count += x % 3
        x -= x % 3
        x = x // 3

    elif x // 2 != 0:
        count += 1
        count += x % 2
        x -= x % 2
        x = x // 2

    print(x,count)