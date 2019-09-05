import sys
sys.stdin = open('2628.txt','r')
r, c = map(int, input().split())
num = int(input())
row = []
col = []
for _ in range(num):
    d, n = map(int, input().split())
    if d == 0: col.append(n)  # col 리스트
    if d == 1: row.append(n)  # row 리스트
row2 = sorted(row)
column2 = sorted(col)  # 작은 수에서 큰 수 리스트
row_num = []
col_num = []

for i in range(len(row2)-1):
    row_num.append(row2[i+1]-row2[i])  # row끼리의 차이를 row_num에 담는다
if row2:
    row_num.append(row2[0])  # 가장 작은 row는 못 넣었으니 담기
    row_num.append(r-row2[-1])  # row길이에서 가장 큰 row 뺀 것 담기
else: row_num.append(r)

for i in range(len(column2)-1):
    col_num.append(column2[i+1]-column2[i])
if column2:
    col_num.append(column2[0])
    col_num.append(c-column2[-1])
else: col_num.append(c)

maxx = 0  # 가장 큰 곱 구하기
for x in range(len(row_num)):
    for y in range(len(col_num)):
        multiple = row_num[x] * col_num[y]
        if maxx < multiple:
            maxx = multiple
print(maxx)

# 2*4 (3-2)*4 (8-3)*4 (10-4)*2 (10-4)*(3-2) 10-4 * 8-3  = 각 잘라진 범위의 크기

