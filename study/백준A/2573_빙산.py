import sys
from pprint import pprint
import collections
sys.stdin = open('2573.txt', 'r')

'''
빙산이 물을 만나면 물을 만난 회수 만큼 빙산을 1씩 줄여나가고 0이 되면 물이 된다
한 턴을 돌릴 때마다 빙산의 갯수가 몇 개 남았는지 확인해나가고 그 빙산의 개수가 2개가 되면
몇 번 턴을 돌렸는지 세어 그 횟수를 반환한다
빙산을 녹인다 -> 빙산이 몇 개 남았는지 확인한다 -> 빙산이 2개 이상이면 break, 2개 미만이면 1년을 더하고 또 녹인다
1. 빙산이 2개인가?
2. 아니라면 주변 0의 개수만큼 ice 값을 녹여준다.
3. iceCnt 를 갱신
4. ans(년의 횟 수)++
'''


def bfs(xi, yi):  # 섬 몇개인지 세기
    # while을 한 번 돌릴 때마다 섬이 몇 개 남았는지 센다
    while cntt < 2:
        # 녹이기
        for ii in range(4):  # 5m 7n
            # 범위를 넘지 않았고, 주변에 숫자가 있고, 방문하지 않았다면
            if box[xi + four_x[ii]][yi + four_y[ii]] != 0 and visited2[xi + four_x[ii]][yi + four_y[ii]] == 0:
                visited2[xi + four_x[ii]][yi + four_y[ii]] = 1  # 방문 처리
                box[xi + four_x[ii]][yi + four_y[ii]] -= 1  # 박스에 하나씩 빼기
                q.append((xi + four_x[ii], yi + four_y[ii]))

        visited[xi][yi] = 1 # 빙산 세기
        q.append((xi, yi))
        while q:
            X, Y = q.popleft()
            for i in range(4):  # 5m 7n
                # 범위를 넘지 않았고, 주변에 숫자가 있고, 방문하지 않았다면
                if 0 <= X + four_x[i] <= n and 0 <= Y + four_y[i]<= m and box[X + four_x[i]][Y + four_y[i]] != 0 and visited[X + four_x[i]][Y + four_y[i]] == 0:
                    visited[X + four_x[i]][Y + four_y[i]] = 1
                    box[X + four_x[i]][Y + four_y[i]] -= 1  # 박스에 하나씩 빼기
                    q.append((X + four_x[i], Y + four_y[i]))




m, n = map(int, input().split())
box = []
for _ in range(m):
    box.append(list(map(int, input().split())))

four_x = [1, 0, -1, 0]
four_y = [0, 1, 0, -1]
visited = [[0] * n for _ in range(m)]
visited2 = [[0] * n for _ in range(m)]
q = collections.deque([])
cntt = 0
years = 0
for i in range(m):
    for j in range(n):
        if box[i][j] != 0 and visited[i][j] == 0:
            cntt += 1  # 처음에 들어갈 때 cntt늘려주기
            bfs(i, j)

