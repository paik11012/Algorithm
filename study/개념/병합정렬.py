def merge(arr, s1, e1, s2, e2):
    idx1 = s1
    idx2 = s2
    temp = []
    while idx1 <= e1 and idx2 <= e2:  # 배열에 남아있는 동안, 한 배열이 없어질 때 까지
        if arr[idx1] >= arr[idx2]:
            temp.append(arr[idx2])
            idx2 += 1
        else:
            temp.append(arr[idx1])
            idx1 += 1

    if idx1 > e1:  # 1이 다 튕겨져 나갔으면
        while idx2 <= e2:
            temp.append(arr[idx2])
            idx2 += 1
    else:
        while idx1 <= e1:  # 1이 다 튕겨져 나갔으면
            temp.append(arr[idx1])
            idx1 += 1
    for i in range(len(temp)):
        arr[s1+i] = temp[i]


def merge_sort(arr, start, end):
    if start >= end:  # 길이가 1개일 때 끝내라
        return None
    else:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, mid+1, end)


n = [1, 3, 0, 7, 2, 5, 4, 3, 1, -1]
merge_sort(n, 0, 9)
print(n)
