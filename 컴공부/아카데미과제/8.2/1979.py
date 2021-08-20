n, k = 5, 3
num_list = [
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1]]

total = 0
for i in range(n): # 0 1 2 3 4 행
    if num_list[i].count(1) == k: # 1이 3개 있으면서
        for zo in range(n-k+2): # 0 1 2 3 확인
            if num_list[i][zo] == 0:
        # 0 2개가 붙어있음
                total += 1
print(total)


# colunm_list = []
# for a in range(n): # 0 1 2 3 4 열
#     for b in range(n): # 0 1 2 3 4 열
#         colunm_list.append(num_list[b][a])  
# # print(colunm_list)


# # (0,5) (5,10) (10,14) (15,19) (20,24) (25,29)

# a = []  # 새로운 열 행렬 만들기!!! 드디어 끝
# for k in range(n): # 30 / 5 = 6 -> 0 1 2 3 4 5
#     new = colunm_list[k*5:k*5+5] # 행렬 5개 만들기
#     a.append(new)
# # print(a) 

# for i in range(n): # 0 1 2 3 4 행
#     if a[i].count(1) == 3 and a[i].count(0) == 2:
#         for j in range(n-k+1): # 0 1 2
#             if a[i][j] == 1 and a[i][j+1] == 1 and a[i][j+2] == 1:
#                 total += 1
# print(total)