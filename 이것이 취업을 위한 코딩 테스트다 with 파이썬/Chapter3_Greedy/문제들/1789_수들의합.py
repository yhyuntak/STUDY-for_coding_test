import sys
read = sys.stdin.readline

S = int(read())

if S == 1 :
    print(1)
else :
    summation = 0
    array = []
    for i in range(1,S):
        summation += i
        if summation > S :
            summation -= i
            break
        array.append(i)

    print(len(array))