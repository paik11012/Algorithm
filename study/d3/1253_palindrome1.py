import sys
from pprint import pprint
sys.stdin = open('1253.txt','r')

n = int(input())
box = []
for _ in range(8):
    box.append(list(str(input())))
pprint(box)
cnt = 0
for x in range(8): # 0~7
    for y in range(8-n+1):  # 시작점 설정  # 0~4까지
        flag = False
        for z in range(n//2): # 0 1
            if box[x][y] == box[x][(n-1)-y]:  # 03, 12 매칭
                flag = True
                print(x,y,x,n-1-y)
            else: break
        if flag == True:  # flag가 true면
            cnt += 1
print(cnt)
#         else:  # 홀수
#             flag = False
#             for z in range(n//2): # 0 1
#                 if out_idx(x, y) and box[x][y] == box[x][n-y]:
#                     flag = True
#                 else: break
#             if not flag:
#                 cnt += 1
# print(cnt)


