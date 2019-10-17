# 평균은 o(nlogn) 최악의 경우에는 o(n^2)
def getboth(arr, pivot, myleft, myright):
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            myleft.append(arr[i])
        else:  # i가 pivot보다 더 크면 right에 더하기
            myright.append(arr[i])


def quicksort(arr, start, end):  # arr의 start부터 end까지 정렬하는 함수
    if start >= end:
        return None
    else:
        pivot = arr[start]
        myleft = []
        myright = []
        getboth(arr, pivot, myleft, myright)  # 큰거

        # 합치기
        print(arr)
        for k in range(len(myleft)-1):
            arr[start+k] = myleft[k]
        arr[len(myleft)] = pivot
        for kk in range(len(myright)):
            arr[start+len(myleft)+kk] = myright[kk]

        quicksort(arr, start, len(myleft)-1) # 왼쪽
        quicksort(arr, start+len(myleft)+1, end) # 오른


n = [2, 3, 0, 7, 2, 5, 4, 3, 1, -1]
quicksort(n, 0, 9)
print(n)
