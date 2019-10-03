import sys
from pprint import pprint
import copy
sys.stdin = open('17136.txt', 'r')


def per(idx):
    global per_list
    if idx >= n:
        arr2 = [0, 0, 0, 0, 0]
        for j in range(5):
            arr2[j] = arr[j]
        per_list.append(arr2)
    else:
        for i in range(5, 0, -1):
            if not visited[i]:
                visited[i] = True
                arr[idx] = i
                # print(arr)
                per(idx + 1)
                visited[i] = False




def change():
    global minn, per_list
    copied = [[0] * 10 for _ in range(10)]  # box의 카피본 만들고
    # cnt, map초기화, cnt비교
    for kk in range(len(per_list)):  # 순열의 갯수만큼 반복
        papers = [0, 5, 5, 5, 5, 5]
        cnt = 0
        for ii in range(10):  # 한 번 순열 불러 올 때 마다 box 카피해 오기
            for jj in range(10):
                copied[ii][jj] = box[ii][jj]
        for r in per_list[kk]:  # kk= 5 4 3 2 1 부터 1 2 3 4 5
            for x in range(10):
                for y in range(10):
                # r을 불러오는 것이 이 자리에 있으면, 한 자리에서 54321을 보게 된다
                    if box[x][y] == 1:  # box에 무엇인가 들어있으면
                        if x + r < 10 and y + r < 10:  # 범위를 벗어나지 않는다면 r은 1부터 5, x y 는 0부터 9까지
                            print(x+r, y+r)
                            flag = True  # 범위 내 모든 수가 1인지 확인하는 flag 한 개라도 벗어나면 false
                            # 색종이의 갯수 확인
                            if papers[r] > 0:
                                # print(papers, per_list[kk], cnt)
                                # pprint(copied)
                                for p in range(r):  # 5 = 0 1 2 3 4
                                    for q in range(r):
                                        if copied[x + p][y + q] != 1:
                                            flag = False
                                if flag:  # flag가 True이면
                                    for p in range(r):  # 5 = 0 1 2 3 4
                                        for q in range(r):
                                            copied[x + p][y + q] = 0  # 방문 처리
                                    papers[r] -= 1  # 그 크기의 종이 빼주기
                                    cnt += 1
        remain_one = False  # 1이 남아있지 않는다
        for xx in range(10):  # 1이 남아있으면 끝
            for yy in range(10):
                if copied[xx][yy] == 1:
                    remain_one= True  # 1이 남았다
        if not remain_one:  # false일 때만 비교, 1이 없으면
            # -1이면 무조건 넣기
            # -1이 아니면 비교하기
            if minn == -1:
                minn = cnt
            else:
                if cnt < minn:  # 최소값 갱신하며 저장하기
                    minn = cnt


minn = -1
box = []
for _ in range(10):
    box.append(list(map(int, input().split())))
per_list = []
arr = [0] * 5
visited = [False] * 6
n = 5
per(0)
# print(per_list)
change()
print(minn)
