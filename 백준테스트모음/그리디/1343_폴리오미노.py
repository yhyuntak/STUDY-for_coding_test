def solution():

    input_list = list(input().split())

    # 하나씩 확인하면서, X인 부분들을 찾는 느낌.
    save_space = []
    result_list = []
    count = 0
    for idx,t in enumerate(input_list[0]) :
        # . 를 만나면 어떤 작업을 하자.
        if t == '.' :

            result = []
            if count % 2 == 1 :
                return -1
            # 사전순으로 빠르게 배열해야하니 A가 무조건 앞에 와야댐.
            # 그럴려면 count가 4로 나눴을 때 몫이 존재해야함.
            # 그만큼 AAAA를 넣어주면 됨.
            if count > 0 :
                four = count//4
                two = (count-four*4)//2
                four_list = ['AAAA' for _ in range(four)]
                two_list = ['BB' for _ in range(two)]

                result.append(''.join(four_list))
                result.append(''.join(two_list))
            result.append('.')
            result_list.append(''.join(result))
            count = -1
        count+=1

        if idx == len(input_list[0])-1 :

            result = []
            if count % 2 == 1 :
                return -1
            # 마지막에 .을 못만나고 끝날수도. 그럼 그땐 이렇게
            four = count//4
            two = (count-four*4)//2
            four_list = ['AAAA' for _ in range(four)]
            two_list = ['BB' for _ in range(two)]

            result.append(''.join(four_list))
            result.append(''.join(two_list))
            result_list.append(''.join(result))
    last_result = ''.join(result_list)
    return last_result
print(solution())