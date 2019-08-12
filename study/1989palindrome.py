def palindrome(a):

    n = len(a)
    new = list(a)
    for i in range(int(n // 2)):  # 0, 1
        result = 1
        if new[i] != new[-1 - i]:  # 0 = 4, 1 = 3
            result = 0
    return result


num = int(input())
for tot in range(1, num + 1):
    a = input()
    print("#{0} {1}".format(tot, palindrome(a)))