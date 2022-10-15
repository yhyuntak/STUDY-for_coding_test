

"""

이때, i번 세로선의 결과가 i번이 나와야 한다. 그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성하시오.

"""

C,M,R = map(int,input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

def move():
    for c in range(C):
        move_c = c
        for r in range(R):
            if board[r][move_c] :
                move_c += 1
            elif move_c > 0 and board[r][move_c-1] :
                move_c -= 1
        if move_c != c :
            return False
    return True
#

def dfs(n,r,c):
    print(n,r,c)
    for _ in range(R):
        print(board[_])
    print(move())
    print()

    if move() :
        print(n)
        return

    if n >= 3 :
        return

    if c >= C-1 : # 열이 칸을 넘어가면 r을 1 키워주고 c는 0으로
        r += 1
        c = 0

    for br in range(r,R):
        for bc in range(c,C-1): # 제일 끝칸은 아예 배제.

            if board[br][bc] == 0 :  # 해당 칸에 가로선이 없으면
                board[br][bc] = 1 # 그어보자.
                dfs(n+1,r,c+2) # 그리고 2칸 뛰기.
                board[br][bc] = 0 # 다시 초기화.

            elif bc > 0 and board[br][bc-1] : # 왼쪽에 칸이 있다면 한칸 점핑
                dfs(n,r,c+1)

            elif board[br][bc+1] == 1 :
                dfs(n,r,c+2)

dfs(0,0,0)

print(move())

