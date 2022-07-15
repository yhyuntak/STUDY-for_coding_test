import sys
read = sys.stdin.readline

T = int(read())
A = 300
B = 60
C = 10
button_array = [A,B,C]
if T % C > 0 : # 1의자리수에 값이 있다면 무조건 불가능
    print(-1)
else :
    # 제일 큰 버튼부터 눌러서 몫을 카운트하고 나머지는 넘긴다.
    summation = []
    for i in range(3):
        summation.append(T // button_array[i])
        T = T % button_array[i]

    for j in range(3):
        print(summation[j],end=' ')
