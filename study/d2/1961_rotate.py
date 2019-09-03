# import sys
# sys.stdin = open('1961.txt','r')
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

num = len(a)
empty90 = [[0]*num for i in range(num)]
empty180 = [[0]*num for i in range(num)]
empty270 = [[0]*num for i in range(num)]

for i in range(num):  # 0 1 2
    for j in range(num):  # 0 1 2
        empty270[i][j] = a[j][2-i]

for i in range(num):
    for j in range(num):
        empty90[i][j] = a[2-j][i]

for i in range(num):
    for j in range(num):
        empty180[i][j] = a[2-i][2-j]








