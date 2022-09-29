import math

def find_max(A,B,min_crit,max_crit):

    max_list = []
    for i in range(1,math.floor(math.sqrt(A))+1):
        if min_crit % i == 0 :
            max_list.append(min_crit//i)
            max_list.append(i)
    max_list.sort(reverse=True)

    for m in max_list :
        if max_crit % m == 0 :
            print(m)
            break

def find_min(A,B,min_crit,max_crit):
    i = 1

    while True:
        if (min_crit * i) % max_crit == 0 :
            print(min_crit*i)
            break
        else :
            i+=1

A,B = map(int,input().split())

# 최대 공약수와 최소 공배수
min_crit = min(A,B)
max_crit = max(A,B)
find_max(A,B,min_crit,max_crit)
find_min(A,B,min_crit,max_crit)