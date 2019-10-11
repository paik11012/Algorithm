myarray = [-1, 1, 1, 2, 5, 100, -99, -55, 55, 7]
# [-99, -55, -1, 1, 1, 2, 5, 7, 55, 100]
# [-1, -99, -55, 1, 1, 2, 5, 55, 100, 7]

def merging(arr, s1, e1, s2, e2):
    # 리스트 arr의 정렬되어있는 s1~e1, s2~e2 두 구간을 합치는 함수
    temp_list = []

    f_idx = s1
    b_idx = s2
    while f_idx <= e1 and b_idx <= e2:
        if arr[f_idx] <= arr[b_idx]:
            temp_list.append(arr[f_idx])
            f_idx += 1
        else:
            temp_list.append(arr[b_idx])
            b_idx += 1

    if f_idx > e1:
        while b_idx <= e2:
            temp_list.append(arr[b_idx])
            b_idx += 1
    else:
        while f_idx <= e1:
            temp_list.append(arr[f_idx])
            f_idx += 1

    for i in range(len(temp_list)):
        arr[s1+i] = temp_list[i]

# 1. 함수를 말로 정의 한다
def mergeSort(arr, start, end):
    # 리스트(배열) arr의 start부터 end까지 병합(합병)정렬 하는 함수

    # 기저조건(Base condition)
    if start >= end:
        return None
    else:
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merging(arr, start, mid, mid+1, end)

mergeSort(myarray, 1, 8)
print(myarray)