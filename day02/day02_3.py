# def bin(n,key):
#     l = 1
#     r = n
#     cnt = 0

#     while 1:
#         mid = int((l+r)/2)
#         cnt +=1
#     if mid == key:
#         return cnt
#         break
#     elif




import sys
sys.stdin = open('sample_3.txt','r')


def binary_search(a, key):  # 400개가 든 리스트 a
    start, end = 0, len(a)  # len(a) = 400
    a_cnt = 0  # 몇 번 나누어지는지 세서 나눌 것
    while start <= end:  # start와 end가 같을 때까지
        middle = (start + end) // 2  # 2로 나눈 몫을 반영
        if middle == key:
            a_cnt += 1
            return a_cnt
        elif a[middle] > key:  # 키가 중간값보다 오른쪽에 위치하면
            end = middle - 1  # end를 하나 전 값 가져오기
            a_cnt += 1
        else:
            start = middle + 1  # 키가 중간값보다 왼쪽에 위치하면
            a_cnt += 1


total = int(input())
for tot in range(1, total+1):
    book, A, B = map(int, input().split())
    a = []  # 1부터 A까지 리스트
    for k in range(1, A+1):
        a.append(k)
    b = []  # 1부터 B까지 리스트
    for k in range(1, B+1):
        b.append(k)

    print(binary_search(a, A))