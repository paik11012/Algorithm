num = 1234


def rev(x):
    sr = ''
    while 1:
        r = x % 10  # 4
        sr = sr + chr(r+ord('0'))
        x = x // 10
        if x == 0: break

    s = ''
    for i in range(len(sr)-1,-1,-1):
        s = s + sr[i]

    return s


print(rev(num))
print(type(rev(num)))
