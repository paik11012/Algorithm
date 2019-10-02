import sys
from pprint import pprint
import copy
sys.stdin = open('17136.txt', 'r')


def change(papers, cnt):
    global minn
    for k in range(6):  # 빠져나오는 조건 설정 종이가 모자라면 빠져나오기
        if papers[k] < 0:
            minn = -1
            return
    visited = [[0] * 10 for _ in range(10)]  # box 카피본
    for ii in range(10):
        for jj in range(10):
            visited[ii][jj] = box[ii][jj]

    for x in range(10):
        for y in range(10):
            if box[x][y]:  # box에 무엇인가 들어있으면
                for r in range(5, 6):  # 5부터 넣어봐라
                    # visited = copy.deepcopy(box)
                    if x + r < 10 and y + r < 10:  # 범위를 벗어나지 않는다면
                        flag = True  # 범위 내 모든 수가 1인지 확인하는 flag 한 개라도 벗어나면 false
                        for p in range(r):  # 5 = 0 1 2 3 4
                            for q in range(r):
                                if box[x + p][y + q] != 1:
                                    flag = False
                        if flag:  # flag가 True이면
                            for p in range(r):  # 5 = 0 1 2 3 4
                                for q in range(r):
                                    visited[x + p][y + q] = 0  # 방문 처리
                            papers[r] -= 1
                            change(papers, cnt + 1)  # 재귀 호출
                            flag = True
                            papers[r] += 1
                            for p in range(r):  # 5 = 0 1 2 3 4
                                for q in range(r):
                                    visited[x + p][y + q] = 0  # 방문 처리
                              # visited 초기화
    if cnt < minn:  # 최소값 갱신하며 저장하기
        minn = cnt
    return


n = 10
minn = 999999
box = []
for _ in range(10):
    box.append(list(map(int, input().split())))
change([0, 5, 5, 5, 5, 5], 0)
print(minn)

