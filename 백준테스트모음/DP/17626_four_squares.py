import math
import sys

read = sys.stdin.readline

N = int(read())

if N < 4 :
    dp_table = [0, 1, 2, 3, 1]

else :

    dp_table = [0 for _ in range(N+1)]

    # 1부터 4까지의 최소의 경우의 수

    dp_table[1] = 1
    dp_table[2] = 2
    dp_table[3] = 3
    dp_table[4] = 1

    now_pow = 2
    for n in range(5,N+1): # N이 최대 50000이니까 그냥 돌려도 될듯.
        if n % math.pow((now_pow+1),2) == 0 :
            now_pow += 1
            dp_table[n] = 1
        else :
            # 이거 모든 경우를 확인해야겠는데..?
            dp_table[n] = 1e9
            for np in range(1,now_pow+1):
                dp_table[n] = \
                    min(dp_table[int(math.pow(np,2))] + dp_table[n - int(math.pow(np,2))],\
                        dp_table[n])

    # 만약 n이 5가 넘어가면 now_pow를 1을 빼서 해볼까
    #
    # if dp_table[N] > 4 :
    #     now_pow -= 1
    #     dp_table[N] = dp_table[int(math.pow(now_pow,2))] + dp_table[n - int(math.pow(now_pow,2))]

    print(dp_table[N])

"""
시간초과인데 좀 잘 모르겠다 일단 스킵.
"""