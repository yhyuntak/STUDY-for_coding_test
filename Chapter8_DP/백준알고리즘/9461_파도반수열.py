T = int(input())
N_array = []
for _ in range(T):
    N_array.append(int(input()))


def dp(N):
    # dp table 초기 설정
    dp_table = [0]*101
    dp_table[1] = 1
    dp_table[2] = 1
    dp_table[3] = 1
    dp_table[4] = 2
    dp_table[5] = 2

    for i in range(6,N+1):
        dp_table[i] = dp_table[i-5]+dp_table[i-1]
    return dp_table[N]

for j in range(T):

    print(dp(N_array[j]))
