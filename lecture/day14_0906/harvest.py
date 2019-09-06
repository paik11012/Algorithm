import sys
sys.stdin = open('harverst.txt','r')

n = int(input())
map = []
for _ in range(n):
    i = list(str(input()))
    map.append(i)
for i in range(n):  # 숫자로 만들기
    for j in range(n):
        map[i][j] = int(map[i][j])
if n % 2 == 0:
    mid = n//2
else: mid = n//2+1

# for x in range(1, n+1):  # 줄 수
#     print(x, abs(3-x)+1)  # 줄 수, 시작 숫자
summ = 0
for x in range(1, n+1):  # 줄 수
    for j in range(2*(mid-abs(mid - x))-1):
        # print(x, abs(3-x)+1+j)  # 줄 수, 시작 숫자
        summ += map[x-1][abs(mid-x)+1+j-1]  # 인텍스 맞추어 주려고 하나 뺌
print(summ)

