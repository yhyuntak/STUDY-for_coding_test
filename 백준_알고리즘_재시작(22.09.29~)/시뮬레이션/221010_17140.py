"""

어매 문제가 빡센데

A[r-1][c-1]의  값이 k가 되는 최소 시간은?
"""

import sys
read = sys.stdin.readline
result_r,result_c,k = map(int,read().split())
A = []
for _ in range(3):
    A.append(list(map(int,read().split())))

time = 0

while time <= 100 :

    # 행,열의 개수를 비교해야한다.
    len_row = len(A)
    len_col = len(A[0])

    # 먼저 각 행,열의 개수와 정답의 인덱스를 비교
    if result_r <= len_row and result_c <= len_col :
        # for jj in range(len_row):
        #     print(A[jj])
        if A[result_r-1][result_c-1] == k :
            break

    if len_row >= len_col : # 행 >= 열일 경우 R연산을
        """
        R연산
        """
        # 각 row를 살펴봐야함.
        # 이때 최대 row의 길이를 체크해야함.
        max_row_len = 3 # 이건 3으로 초기화해야함.
        save_rows = []
        for r in range(len_row) :
            each_row = A[r]
            # 각각의 수의 개수도 세야함.
            num_dict = {}
            for each_row_val in each_row :
                if each_row_val == 0 :
                    continue
                else:
                    try: num_dict[each_row_val] += 1
                    except : num_dict[each_row_val] = 1
            # 한 행의 개수를 모두 측정했다.
            # 그럼 새로운 행을 만들어봐야함.
            # 1. 먼저 등장 횟수가 커지는 순으로 : x[1], 2. 이게 여러개면 수가 커지는 순으로 : x[0]
            sort_list = sorted(list(num_dict.items()),key=lambda x : (x[1],x[0]))
            new_row = []
            cnt = 0
            for a,b in sort_list :
                new_row.append(a)
                new_row.append(b)
                cnt += 2
                if cnt >= 100 : # 개수가 100개를 넘어가면 안된다.
                    break
            max_row_len = max(max_row_len,cnt)
            save_rows.append(new_row)

        # 마지막으로 길이가 차이나는 만큼 0을 추가해서 A를 재생성
        A = []
        for save_row in save_rows :
            A.append(save_row+[0 for _ in range(max_row_len-len(save_row))])

    else :  # 행 < 열 일 경우 C연산을
        """
        C연산
        """
        # 각 col을 살펴봐야함.
        # 이때 최대 col의 길이를 체크해야함.
        max_col_len = 3
        save_cols = []
        for c in range(len_col):
            each_col = []
            for r in range(len_row):
                each_col.append(A[r][c])
            # 각각의 수의 개수도 세야함.
            num_dict = {}
            for each_col_val in each_col:
                if each_col_val == 0:
                    continue
                else:
                    try:
                        num_dict[each_col_val] += 1
                    except:
                        num_dict[each_col_val] = 1
            # 한 열의 개수를 모두 측정했다.
            # 그럼 새로운 열을 만들어봐야함.
            # 1. 먼저 등장 횟수가 커지는 순으로 : x[1], 2. 이게 여러개면 수가 커지는 순으로 : x[0]
            sort_list = sorted(list(num_dict.items()), key=lambda x: (x[1], x[0]))
            new_col = []
            cnt = 0
            for a, b in sort_list:
                new_col.append(a)
                new_col.append(b)
                cnt += 2
                if cnt >= 100 : # 개수가 100개를 넘어가면 안된다.
                    break
            max_col_len = max(max_col_len, cnt)
            save_cols.append(new_col)

        # 마지막으로 길이가 차이나는 만큼 0을 추가해서 A를 재생성
        # 근데 col은 미리 A를 선언하는게 좋을듯.
        A = [[0 for _ in range(len(save_cols))] for _ in range(max_col_len)]
        for c,save_col in enumerate(save_cols):
            for r,val in enumerate(save_col) :
                A[r][c] = val
    time += 1

if time > 100 :
    print(-1)
else :
    print(time)