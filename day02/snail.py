def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    if snail[x][y] != 0: return True
    return False

    
snail = [[0]*5 for i in range(5)]
X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

for i in range(1, 26):
    snail[X][Y] = i
    X += dx[d]
    Y += dy[d]
    if iswall(X+dx[d],Y+dy[d]):
        d = (d + 1) % 4

print(snail)