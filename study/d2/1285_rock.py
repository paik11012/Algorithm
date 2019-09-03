import sys
sys.stdin = open('1285.txt', 'r')
total = int(input())
for t in range(1, total+1):
    n = int(input())
    rock_list = list(map(int, input().split()))

    new = []
    for i in rock_list:
        i = abs(i)
        new.append(i)
    # print(new)
    min = new[0]
    for k in range(len(new)):
        if min > new[k]:
            min = new[k]
    print('#{} {} {}'.format(t, min, new.count(min)))