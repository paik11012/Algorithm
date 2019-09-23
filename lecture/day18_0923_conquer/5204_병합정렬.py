import sys
sys.stdin = open('5204.txt', 'r')


def merge_sort(nl):
    left = []
    right = []
    m = len(nl)//2
    if len(nl) == 1:
        return nl  # 요소가 하나밖에 없으면 끝
    left = merge_sort(nl[:m])
    right = merge_sort(nl[m:])
    # print(left, right)
    return merge(left, right)


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1  # 한 번 정렬 할 때마다 cnt 1씩 늘리기
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
            else: result.append(right[0])
        elif len(left) > 0:
            result.append(left[0])
        elif len(right) > 0:
            result.append(right[0])
    return result


num = int(input())
for _ in range(num):
    n = int(input())
    n_list = list(map(int, input().split()))
    cnt = 0
    m = n // 2
    r = merge_sort(n_list)
    print(r)
    print(n_list)