import sys
sys.stdin = open('2628.txt','r')
r, c = map(int, input().split())
num = int(input())
row = []
column = []
for _ in range(num):
    a, b = map(int, input().split())
    if a == 0:
        row.append(b)
    elif a == 1:
        column.append(b)
minn = 00
row.append(c)
row.append(0)
column.append(r)
column.append(0)
row.sort()
column.sort()
for i in range(len(row)-1):
    for j in range(len(column)-1):
        comp = (row[i+1]-row[i]) * (column[j+1]-column[j])
        if minn < comp:
            minn = comp
print(minn)
