from pprint import pprint
import sys
sys.stdin = open('sample.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    row, col, num = map(int, input().split())
    box = [[0] * col for _ in range(row)]  # 먼저 만들어놓은 박스(숫자 넣을 리스트 때문에 만든 박스)

    for _ in range(num):
        r1, c1, r2, c2, color = map(int, input().split())
        check = []
        flag = False
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                if box[x][y] > color:
                    flag = True   # flag를 넣어서!!!!
        if flag == False:
            for x in range(r1, r2 + 1):
                for y in range(c1, c2 + 1):
                    box[x][y] = color


    r = [0] * 11  # 숫자 11개 저장할 공간
    for i in range(row):  # new box를 돌며 각각 숫자를 만나면 그 숫자 index에 위치한 r에 1을 더하라
        for j in range(col):
            r[box[i][j]] += 1
    print('#{} {}'.format(tcc,max(r)))   # tc 생략함



