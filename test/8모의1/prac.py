import sys
from pprint import pprint
sys.stdin = open('answer.txt','r')

tc = int(input())
for tcc in range(1, tc+1):
    num = int(input())
    num = num+6

    maap = []  # ['CXXXXXXXC', ~]
    for i in range(3, num-3):
        j = input().split()
        maap += j
    str_map = []  # [['C', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'C'],
    for i in maap:
        new = list(i)
        str_map.append(new)
    # pprint(str_map)
    empty = [ [0] * (num+3) for _ in range(num+3)]
    # pprint(empty)
    for i in range(num):
        for j in range(num):
            if str_map[i][j] == 'A':  # 앞 뒤 한 칸 바꾸기
                empty[i-1][j] = 'X'
                empty[i][j+1] = 'X'
                empty[i+1][j] = 'X'
                empty[i][j-1] = 'X'
            elif str_map[i][j] == 'C':  # 앞뒤 세 칸 바꾸기
                empty[i - 1][j] = 'X'
                empty[i - 2][j] = 'X'
                empty[i - 3][j] = 'X'
                empty[i][j + 2] = 'X'
                empty[i][j + 2] = 'X'
                empty[i][j + 3] = 'X'
                empty[i + 2][j] = 'X'
                empty[i + 2][j] = 'X'
                empty[i + 3][j] = 'X'
                empty[i][j - 2] = 'X'
                empty[i][j - 2] = 'X'
                empty[i][j - 3] = 'X'
            else: empty[i][j] = str_map[i][j]

    pprint(empty)