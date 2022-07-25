import sys
read = sys.stdin.readline

T = int(read())
result_array = []
for i in range(T):

    # '\n' 벗기는 작업
    temp = read().split()
    temp = temp[0]
    state = 0
    for idx,j in enumerate(temp) :
        if j == '(' :
            state += 1
        elif j == ')' :
            state -= 1
        # state가 -1이 나오는 순간 이 문자열은 VPS가 아니다.
        if state < 0 and idx <= len(temp):
            result_array.append('NO')
            break
        elif state == 0 and idx == len(temp) -1 :
            # 끝나는 순간 state 가 0 이면 이것은 VPS다
            result_array.append('YES')
        elif state > 0 and idx == len(temp) - 1:
            result_array.append('NO')
for k in range(T):
    print(result_array[k])