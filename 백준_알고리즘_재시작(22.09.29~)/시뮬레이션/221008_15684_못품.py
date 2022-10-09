# 2차원 배열 사용해서 다시 풀어보자.
import sys
input = sys.stdin.readline

C,M,R = map(int,input().split())

lines = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    a,b = map(int,input().split())
    lines[a-1][b-1] = 1

def check():
    for c in range(C): # 세로열 검사
        save_c = c
        for r in range(R): # 가로행을 내려가자.
            if save_c == 0 : # 현재 c가 0이면 지금 선분만 파악
                if lines[r][save_c] == 1 : # 가로선이 있으면 오른쪽으로
                    save_c+=1
                else : continue # 그냥 내려가기.
            else : # c가 0이 아니면 왼쪽과 현재를 파악해야함.
                if lines[r][save_c-1] == 1 :  # 왼쪽
                    save_c -= 1
                elif lines[r][save_c] == 1 : # 오른쪽
                    save_c += 1
                else : continue # 그냥 내려가기.
        if c != save_c : # 하나라도 현재 경로와 맞지 않으면, false 리턴
            return False
    # 만약 여기까지 뚫으면 다 맞는것이므로 true 리턴
    return True
def dfs(cnt,row,col):
    global ans

    if check(): # 출발점에 잘 도착하면 현재 dfs 종료
        ans = min(ans,cnt)
        return

    elif cnt == 3 or ans <= cnt :
        # 도착을 제대로 못해서 cnt가 3까지 카운트가 증가했으면 아래 코드에서 4로 증가할테니 멈추기.
        # 현재 minimum보다 cnt가 더 커지면 아래 코드를 돌려볼 필요가 없다. 왜냐하면 ans가 더 작거나 같다는 뜻은 이미 길을 최소로 찾았다는 이야기니까.
        return

    for i in range(row,R):
        if i == row : # 행이 변경되지 않았으면,
            k = col # 입력으로 받은 열부터 for문을 실행.
        else : # 행이 변경됬으면,
            k = 0 # 열은 0부터 다시 실행.
        for j in range(k,C-1): # C-1의 이유는 마지막 열은 포함하지 않는 것.
            if lines[i][j] == 0 and lines[i][j+1] == 0 : # 가로선을 현재 위치에 놓을 때, 오른쪽에 선이 없는 경우,
                # 이때 가로선을 둘껀데, 만약 왼쪽에 있다면?
                if lines[i][j-1] == 1 and j > 0 : # 단, 열은 1이상이어야함.
                    continue
                # 가로선을 두자.
                lines[i][j] = 1
                dfs(cnt+1,i,j+2) # 현재 위치에 그렸으니 열을 +2 해서 위 조건문을 통해 새로운 가로선을 둘 수 있는지 판단
                # 그리고 dfs가 끝나면 다른 선의 경우도 봐야하므로 빼기
                lines[i][j] = 0


if M == 0 :
    print(0)
else :
    ans = 4 # 3이 맥시멈이니 3보다 큰 아무 값으로 초기화.
    dfs(0,0,0)
    print(ans if ans < 4 else -1 )