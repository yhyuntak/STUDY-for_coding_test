array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):

    if start >= end : # 원소가 한개일 경우
        return
    pivot = start
    left = start +1
    right = end

    # left와 right가 엇갈리기 전까지 고
    while left <= right:

        # left가 pivot보다 작으면 계속 넘기면서 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right가 pivot보다 크면 계속 땡기면서 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right : # 엇갈렸다면
            # 피벗과 right를 교체하자
            array[pivot],array[right] = array[right],array[pivot]

        else : # 엇갈리지 않으면
            # left와 right를 교체하자
            array[left],array[right] = array[right],array[left]

    # right가 첫번째 pivot의 위치이므로 다음 quick sort의 좌측의 end+1가 되고
    # 우측의 start-1이 된다. 
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)