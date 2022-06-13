import time
n,m,k = map(int,input().split())
number_list = list(map(int,input().split()))

if len(number_list) == n:
    number_list.sort(reverse=True)
    maximum = number_list[0]
    second = number_list[1]
    answer = 0
    count = 1

    answer_1_tiem = time.time()
    for i in range(m):
        if count <= k :
            answer += maximum
            count += 1
        else :
            answer += second
            count = 1
    answer_1_tiem = time.time()-answer_1_tiem
    print(answer,answer_1_tiem)

    answer_2_tiem = time.time()
    temp = m * maximum
    iter = m // (k+1)

    diff = maximum - second
    answer_2 = temp - diff*iter
    answer_2_tiem = time.time()-answer_2_tiem
    print(answer_2,answer_2_tiem)

else :
    raise Exception('Dont match numbers')
