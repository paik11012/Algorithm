import sys
from pprint import pprint
sys.stdin = open('17136.txt', 'r')


def change():
    for k in range(6):  # 빠져나오는 조건 설정 종이가 모자라면 빠져나오기
        if papers[k] < 0:
            return
    else:
        for x in range(10):
            for y in range(10):
                if box[x][y] == 1:
                    for paper in range(5, 0, -1):
                        if x + paper < 10 and y + paper < 10:  # 범위를 벗어나지 않는다면
                            flag = True  # 범위 내 모든 수가 1인지 확인하는 flag 한 개라도 벗어나면 false
                            for p in range(paper):  # 5 = 0 1 2 3 4
                                for q in range(paper):
                                    if box[x+p][y+q] != 1:
                                        flag = False
                            if flag:  # flag가 True이면
                                for p in range(paper):  # 5 = 0 1 2 3 4
                                    for q in range(paper):
                                        box[x+p][y+q] = 0  # 방문 처리
                                papers[paper] -= 1


n = 10
box = []
papers = [0, 5, 5, 5, 5, 5]
for _ in range(10):
    box.append(list(map(int, input().split())))
visited = [[0] * 10 for _ in range(10)]
change()

pprint(box)
print(papers)
