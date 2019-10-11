def com(n, m):
    for i in range(n*m):
        x = i//m
        y = i % m
        print((x, y))


com(2, 4)