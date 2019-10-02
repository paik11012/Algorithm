import sys
sys.stdin = open('4881.txt','r')


def small(idx, cnt):
    global minn
    # 가지치기 코드
    if cnt > minn:
        return
    if idx >= n:  # 세 칸이 채워지면 비교
        if cnt < minn:
            minn = cnt
            print(minn)
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                arr[idx] = i
                small(idx + 1, cnt + box[idx][i-1])
                visited[i] = False
                # print(cnt)


n = int(input())
box = []
for _ in range(n):
    k = list(map(int, input().split()))
    box.append(k)
minn = 9999
visited = [False] * (n+1)
arr = [0] * n
small(0, 0)
print(minn)
