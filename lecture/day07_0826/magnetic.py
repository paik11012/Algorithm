box = [[1, 0, 2, 0, 1, 0, 1],
       [0, 2, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 2, 2],
       [0, 0, 0, 0, 0, 1, 0],
       [0, 0, 2, 1, 0, 2, 1],
       [0 ,0 ,1, 2, 2, 0, 2]]


cnt = 0
for i in range(7):
    flag = False
    for j in range(7):
        if box[j][i] == 1:
            flag = True
        if box[j][i] == 2 and flag == True:
            cnt += 1
            flag = False

print(cnt)
