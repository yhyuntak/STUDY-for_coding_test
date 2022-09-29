import sys
read = sys.stdin.readline

N = int(read())
K = int(read())

start = 1
end = K

while start <= end :
    m = (start + end) // 2
    num_cnt = 0

    for n in range(1,N+1):
        num_cnt += min(m//n,N)

    if num_cnt < K :
        # m을 크게하기위해 start를 변경
        start = m + 1
    else :
        end = m - 1
print(start)