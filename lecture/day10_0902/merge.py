def merge_sort(m):  # 나누는 함수
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]  # 두 개로 나누기
    #리스트 크기가 1이 될 때까지 merge호출, 계속 나누기
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):  # 병합하는 함수
    result = []  # 병합할 곳
    while len(left) > 0 and len(right) > 0:  # 양 리스트에 원소가 남아있을 때까지
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else: result.append(right.pop(0))

    if len(left) > 0:  # 남아있는 것 붙이기
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


data = [1, 10, 3, 8, 22, 5, 19, 25]
print(merge_sort(data))


