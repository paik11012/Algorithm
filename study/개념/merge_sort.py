arr = [1, 2, 5, 1, -20, 5, 22, 9, -99, 121]


def merging(s1, e1, s2, e2):
    # arr의 두 배열을 비교하면서 합치는 함수
    temp = []
    f_idx = s1
    b_idx = s2
    while f_idx <= e1 and b_idx <= e2:
        if arr[f_idx] <= arr[b_idx]:
            temp.append(arr[f_idx])
            f_idx += 1
        else:
            temp.append(arr[b_idx])
            b_idx += 1
    # 하나가 튕겨나간 상황
    if f_idx > e1:
        while b_idx <= e2:
            temp.append(arr[b_idx])
            b_idx += 1
    else:
        while f_idx <= e1:
            temp.append(arr[f_idx])
            f_idx += 1

    for j in range(len(temp)):
        arr[s1+j] = temp[j]



def mergesort(arr, start, end):
    # arr의 start부터 end까지 병합정렬 하는 함수
    if start == end:
        return
    else:
        mid = (start+end)//2
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        merging(start, mid, mid+1, end)



mergesort(arr, 0, 9)
print(arr)