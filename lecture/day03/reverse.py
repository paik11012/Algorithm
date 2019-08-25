a = [1, 2, 3, 4, 5, 6, 7, 10, 'b']


def rev(number):
    b = []
    for i in range(len(number)):
        b.append(a[len(number) - i - 1])
    return b


print(rev(a))

# sr = ''
# for i in range(len(s)-1,-1,-1)
#     sr = sr + s[i]

# b = '1', '2', '3', '4'
# # 아스키코드 값
# re = ord('1')-ord('0')
# print(re)