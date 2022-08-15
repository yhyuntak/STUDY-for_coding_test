import sys
read = sys.stdin.readline

T = int(read())

for t in range(T):
    N = int(read())
    first_row = list(map(int, read().split()))
    second_row = list(map(int, read().split()))
    g = [first_row,second_row]
    # 핵심은 삼각형 형태로 보는 것!

    d = [[0 for _ in range(N)] for _ in range(2)]

    if N == 1 :
        print(max(g[0][0],g[1][0]))
        continue

    # 초기 값은 2번째 열까지
    d[0][0] = g[0][0]
    d[1][0] = g[1][0]
    d[0][1] = d[1][0] + g[0][1]
    d[1][1] = d[0][0] + g[1][1]
    # 첫번째 행 -> 두번째 행 순으로 읽자.
    for n in range(2,N):
        for r in range(2):
            now_row = g[r][n]
            # 3개의 칸의 maximum 값을 찾자.
            max_val = d[(r-1)%2][n-1]
            max_val = max(max(max_val,d[0][n-2]),d[1][n-2])

            d[r][n] = max_val + now_row

    first_max = max(d[0])
    second_max = max(d[1])
    result = max(first_max,second_max)

    print(result)