import sys
from pprint import pprint

sys.stdin = open('17136.txt', 'r')


def change(papers, cnt, cnt_00):
    global minn
    for k in range(6):  # 빠져나오는 조건 설정 종이가 모자라면 빠져나오기
        if papers[k] < 0:
            minn = -1
            return
    if cnt_00 < 0: return  # 끝나는 조건 모든 1이 visit하면 끝
    for x in range(10):
        for y in range(10):
            if box[x][y]:
                for paper in range(5, 0, -1):  # 5 4 3 2 1
                    if x + paper < 11 and y + paper < 11:  # 범위를 벗어나지 않는다면  # 5, 0에서 시작
                        flag = True  # 범위 내 모든 수가 1인지 확인하는 flag 한 개라도 벗어나면 false
                        for p in range(paper):  # 5 = 0 1 2 3 4
                            for q in range(paper):
                                if box[x + p][y + q] != 1:
                                    flag = False
                        if flag:  # flag가 True이면
                            for p in range(paper):  # 5 = 0 1 2 3 4
                                for q in range(paper):
                                    box[x + p][y + q] = 0  # 방문 처리
                                    cnt_00 -= 1
                                    print(cnt_00)
                                    pprint(box)
                            papers[paper] -= 1
                            # print(box)
                            change(papers, cnt + 1, cnt_00)
                            flag = True
                            papers[paper] += 1
                            for p in range(paper):  # 5 = 0 1 2 3 4
                                for q in range(paper):
                                    box[x + p][y + q] = 1  # 방문 처리
                                    cnt_00 += 1
                            # 재귀를 돌린 후 원상복귀 시킨다
                return
    if cnt < minn:
        minn = cnt
    return


n = 10
minn = 999999
box = []
for _ in range(10):
    box.append(list(map(int, input().split())))
cnt_0 = 0
for x in range(10):
    for y in range(10):
        if box[x][y] == 1:
            cnt_0 += 1
change([0, 5, 5, 5, 5, 5], 0)
print(minn)


