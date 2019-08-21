num = 5
a = [[0] * i for i in range(1,num+1)]
# 빈 0 리스트 만들기
a[0][0] = 1
for i in range(num):
    for j in range(i):
        if a[i][-1] == 0 or a[i][0] == 0:
            a[i][-1] = 1
            a[i][0] = 1
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]  # 이중배열 리스트
print(a)
new = ''
for z in a:
    new = ''
    for y in z:
        new += str(y)+' '
    print(new)