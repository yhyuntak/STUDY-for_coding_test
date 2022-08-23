import sys
read = sys.stdin.readline

A,B = map(int,read().split())

"""
2로 나눠지는지 보고
나눠지지 않으면 1을 빼보면된다.
이를 반복하는 느낌으로.
"""
count = 0
while A <= B :
    # 먼저 A와 B가 같을 경우 바로 끝내야.
    if A==B :
        print(count+1)
        break
    # 다를 경우 아래 로직 실행
    BB = str(B)
    # B가 2로 나눠지는가?
    if B % 2 == 0 :
        B = int(B/2)
        count += 1
    elif BB[-1] == "1":
        # 일의 자리의 수에 1을 뺄 수 있는가?
        BB = BB[:-1]
        B = int(BB)
        count += 1
    else :
        # 둘다 안된다면, 이제 더이상 루프를 진행하면 안된다.
        print(-1)
        break

    if A >B :
        print(-1)
        break