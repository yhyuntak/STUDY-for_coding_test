array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):

    if len(array) <= 1 : # 원소가 한개일 경우
        return array
    pivot = array[0]
    tail = array[1:]

    '''
    어차피 바꿔주고 왼쪽 오른쪽을 할빠엔 
    아래처럼 그냥 간단하게 바꾸는 개념없이 더 작은걸 왼쪽 더 큰걸 오른쪽으로 생각하자
    '''
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    print(array,pivot)
    print(left_side,right_side)
    # 여기서 재귀가 들어가네.. 지린다
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))