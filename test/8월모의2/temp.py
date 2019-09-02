box = [[1, 1, 2, 2],
       [4, 3, 9, 3],
       [1, 4, 1, 3],
       [4, 4, 4, 4]]
sum1 = 0
sum2 = 0
size = 3
num = 4  # 몇개 더할 것인가

# 큰 대각선 구하는 예시
# for i in range(num):  # 0 1 2 3
#     sum1 += box[i][i]
# for i in range(num):
#     sum2 += box[i][num-1-i]  # 0 1 2 3,
max_ab = 0
for x in range(num - size + 1):  # 0 1
    for y in range(num - size + 1):  # 0 1 시작점 잡기
        sum1 = 0
        sum2 = 0
        for a in range(size):  # 0 1 2
            sum1 += box[x+a][y+a]
        for b in range(size):  # 0 1 2
            sum2 += box[x+size-b-1][y+b]
        ab = abs(sum1 - sum2)
        if ab > max_ab:
            max_ab = ab
print(max_ab)

