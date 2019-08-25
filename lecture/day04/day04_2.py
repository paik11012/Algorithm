import sys
sys.stdin = open('2.txt', 'r')

def is_palindrome(wd):  # wd는 비교할 문자
    for z in range(len(wd)//2):
        result = False
        if wd[z] == wd[-1-z]:
            result = True
    return result


total = int(input())
for tot in range(1, total+1):
    ran, pat = map(int, input().split())  # 10 10
    new_list = [] * ran
    for i in range(pat):
        a = input()
        for k in range(ran - pat + 1):  # 1 에서
            word = a[k:k + pat]  # 원하는 pat만큼 나옴
            if is_palindrome(word) == True:
                b = word


    print('#{0} {1}'.format(tot,b))

