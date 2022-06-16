N = int(input())
plans = input().split()
position = [1,1]

def move(pos,state,N):
    
    if state == 'R' :
        pos[1] += 1
    elif state == 'L':
        pos[1] -= 1
    elif state == 'U':
        pos[0] -= 1
    elif state == 'D':
        pos[0] += 1
    if pos[0] < 1 :
        pos[0] = 1
    elif pos[0] > N :
        pos[0] = N

    if pos[1] < 1 :
        pos[1] = 1
    elif pos[1] > N:
        pos[1] = N


for plan in plans:
    move(position,plan)

print(str(position[0])+' '+str(position[1]))