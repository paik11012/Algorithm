
x, y = 4, 4
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]



def is_wall(x, y):


    if x  <0 or x > =5 : return True
    if y < 0 or x > =5 : return True
    else:
        return False

sums = 0
for x in range(len(arr)): # 0 1 2 3 4 행
    for y in range(len(arr[0])): # 0 1 2 3 4 열
        for I in range(4): # 0 1 2 3
            testx = x + dx[I]
            testy = y + dy[I]
            if is_wall(testx, testy) == False:
                sums += abs(arr[x][y] - arr[testx][testy])
print(sum)


