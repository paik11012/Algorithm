# import sys
# sys.stdin = open('1961.txt','r')
a = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
def r_90(a):
    n = len(a)
    re_90 = ''
    for i in range(n):  # 2
        for j in range(len(a)):  # 2
            re_90 += re_90[j][n-i-1]  # [0][2] = [0][0]
            return re_90
    return re_90
def r_180(a):
    n = len(a)
    re_180 = [[0]* n for _ in range(n)]
    for i in range(n):  # 2
        for j in range(n):  # 2
            re_180[n-i-1][n-j-1] = a[i][j]  # [0][2] = [0][0]
    return re_180
def r_270(a):
    n = len(a)
    re_270 = [[0]* n for _ in range(n)]
    for i in range(n):  # 2
        for j in range(n):  # 2
            re_270[n-j-1][n-i-1] = a[i][j]  # [0][2] = [0][0]
    return re_270
jo = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(r_90(jo), r_180(jo), r_270(jo))