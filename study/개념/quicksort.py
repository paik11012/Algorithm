# 평균은 o(nlogn) 최악의 경우에는 o(n^2)
# 2n -> n번  (swap 교재에)
def getleft(arr, pivot, start, end, myleft):
    for i in range(start, end+1):  # 맨 앞이 pivot 이니까 빼고 돌려고 1부터 시작
        if arr[i] <= pivot:
            myleft.append(arr[i])


def getright(arr, pivot, start, end, myright):
    for i in range(start, end+1):
        if arr[i] > pivot:
            myright.append(arr[i])


def quicksort(arr, start, end):  # arr의 start부터 end까지 정렬하는 함수
    if start >= end:
        return None
    else:
        pivot = arr[start]
        myleft = []
        myright = []
        getleft(arr, pivot, start+1, end, myleft)  # 작은거
        getright(arr, pivot, start+1, end, myright)  # 큰거
        # 합치기
        for k in range(len(myleft)):  # 왼쪽
            arr[start+k] = myleft[k]
        arr[start+len(myleft)] = pivot  # 피봇, 기준점 정하기
        for kk in range(len(myright)):  # 큰거
            arr[start+len(myleft)+kk+1] = myright[kk]
        quicksort(arr, start, start+len(myleft)-1) # 왼쪽
        quicksort(arr, start+len(myleft)+1, end) # 오른쪽


n = [2, 3, 0, 7, 2, 5, 4, 3, 1, -1]
quicksort(n, 0, 9)
print(n)
