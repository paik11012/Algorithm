import sys
from pprint import pprint
sys.stdin = open('03.txt', 'r')

def search(start):
    global result
    visited[start] = True
    for next in range(1, node+1):  # node로 하는 이유? 끝 노드까지 방문해야 해서
        if box[start][next] == 1 and visited[next] == False:
            if next == e:
                result = 1
                return
            search(next)

tc = int(input())  # 3
for num in range(1, tc+1):
    node, line = map(int, input().split())  # 노드 간선
    box = [[0]* (node+1) for _ in range(node+1)]  # 0이 있는 큰 박스, 헷갈리니까 7 * 7 만들고 0행 0열은 버린다
    for _ in range(line):
        x, y = map(int, input().split())
        box[x][y] = 1
    s, e = map(int, input().split())
    visited = [False] * (node+1)
    result = 0
    search(s)
    print('#{} {}'.format(num,result))





