# def sharp(i, j):
#     return i + (i+j-1)*(i+j-2)//2

# print(sharp(3,3))



def ssharp(x,y):
    return (x ** 2 + x)/2 + x * y - x + (y **2 -3*y+2)/2
print(int(ssharp(5,5)))


def pos(num):
    # num1 = (x1+y1-2)*(x1+y1-1) // 2 + x1
    A = 0
    while 1:
        if (A * A - A) // 2 < num <= (A * A + A) // 2:
            x = num - (A * A - A) // 2
            y = A + 1 - x
            break
        else:
            A += 1  # A를 하나씩 더하면서 값 찾기
    return x, y


for T in range(int(input())):
    p, q = map(int, input().split())
    pos1 = pos(p)
    pos2 = pos(q)
    x, y = pos1[0] + pos2[0], pos1[1] + pos2[1]
    print('#{} {}'.format(T + 1, (x + y - 2) * (x + y - 1) // 2 + x))