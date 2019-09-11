import sys
from pprint import pprint
sys.stdin = open('1253.txt','r')


def out_idx(i, j):
    if i < 0 or i > 7: return True
    if j < 0 or j > 7: return True
    return False


n = int(input())
box = []
for _ in range(8):
    box.append(list(str(input())))
pprint(box)
cnt = 0
for x in range(8):
    for y in range(8):  # 시작점 설정
        if n % 2 == 0: # 짝수
            flag = False
            for z in range(n//2): # 0 1
                if out_idx(x, y) and box[x][y] == box[x][(n-1)-y]:  # 03, 12 매칭
                    flag = True
                else: break
            if not flag:  # flag가 true면
                cnt += 1
        else:  # 홀수
            flag = False
            for z in range(n//2): # 0 1
                if out_idx(x, y) and box[x][y] == box[x][n-y]:
                    flag = True
                else: break
            if not flag:
                cnt += 1
print(cnt)


