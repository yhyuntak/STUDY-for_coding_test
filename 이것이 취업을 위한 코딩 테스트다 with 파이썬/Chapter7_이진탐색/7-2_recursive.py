def binary_search(array,target,start,end):
    if start>end:
        return None

    mid = (start+end)//2

    # 우연히 중간점이 타겟이면
    if array[mid] == target:
        return mid

    # 그 외에는 일반적인 이진 탐색으로

    # 중간값이 타겟보다 크면 왼쪽만 살펴보자.
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    # 중간값이 타겟보다 작으면 오른쪽만 살펴보자.
    else:
        return binary_search(array,target,mid+1,end)


n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result =binary_search(array,target,0,n-1)
if result == None:
    print("찾는 원소가 없습니다.")
else :
    print(result+1)

def bina(array,target,start,end):
    if start > end :
        return None

    mid = (start+end)//2

    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return bina(array,start,mid-1)
    else:
        return bina(array,mid+1,end)
