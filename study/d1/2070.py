# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
# 3 8 
# 7 7 
# 369 123      
# #1 <

total =int(input())
for k in range(1,total+1):
    a, b = map(int,input().split())
    if a > b:
        new = ">"
    elif a == b:
        new = "="
    else:
        new = "<"
    print('#{} {}'.format(k, new))