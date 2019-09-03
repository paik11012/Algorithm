import sys
from pprint import pprint
sys.stdin = open('03.txt', 'r')

def search_map(start):  # 재귀함수, 시작 번호
    global result  #  함수 밖에 있는 변수 끌어오기
    visited[start] = True  # 우선 start 바꿔주기, 자기처리
    for next in range(1, v+1):  # 시작노드에 등록된 노착노드부터 끝까지 검색
        if box[start][next] == 1 and visited[next] == False: # 연결되어 있고 방문하지 않았으면
            if next == g:  # 궁금한 노드의 열이며
                result = 1  # 갈 수 있는 곳
                return  # 함수 끝내고 return none
            search_map(next)  # 다음 노드로 가서 검색하라

tc = int(input())  # 3
for num in range(1, tc+1):
    v, e = map(int, input().split())  # 노드 간선
    box = [[0]* (v+1) for _ in range(v+1)]  # 0이 있는 큰 박스, 헷갈리니까 7 * 7 만들고 0행 0열은 버린다

    for i in range(e):
        x, y = map(int,input().split())
        box[x][y] = 1
    s, g = map(int, input().split())  # 1 6 궁금한 노드
    visited = [False] * (v+1)  # 방문했던 곳 표시용
    result = 0  # 갈 수 있으면 1 없으면 0, 우선 갈 수 없다고 표시
    search_map(s)  #시작 하는 곳에서 찾기
    print('#{} {}'.format(num, result))


