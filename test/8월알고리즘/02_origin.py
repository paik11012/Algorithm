import sys
sys.stdin = open('02.txt','r')
total = int(input())
for tot in range(1, total+1):
    n, m, k = map(int,input().split())
    arr = []
    for _ in range(n):
        line = list(map(int,input().split()))
        arr.append(line)
# n = 4 m = 5 k = 3
# # x = 2 j = 3
    n_list = []
    for x in range(n - k + 1):  # 0 1
        for y in range(m - k + 1):  # 0 1 2
            smallsum = 0
            for z in range(k): # 0 1 2
                smallsum += sum(arr[x+z][y:y+z]) # 첫 왼쪽 위에 설정 (00 01 02 10 11 12 20 21 22)
            for zz in range(k-2):
                smallsum -= sum(arr[x+zz+1][[y+1:y+k-1]]) 
            n_list.append(smallsum)
    print(n_list)

    print('#{} {}'.format(tot, max(n_list)))