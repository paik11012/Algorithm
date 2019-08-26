from pprint import pprint
box = [[1, 0, 2, 0, 1, 0, 1],
       [0, 2, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 2, 2],
       [0, 0, 0, 0, 0, 1, 0],
       [0, 0, 2, 1, 0, 2, 1],
       [0 ,0 ,1, 2, 2, 0, 2]]

new_box = [[0] * 7 for _ in range(7)]
for i in range(7):
    for j in range(7):
        new_box[i][j] = box[j][i]

# pprint(new_box)

for i in range(7):
    new = ''
    for j in range(7):
        new += str(new_box[i][j])
    print(new)


