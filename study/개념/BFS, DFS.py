import collections


def bfs(x):
    visited = [False] * (n + 1)
    q = collections.deque([])
    visited[x] = True
    q.append(x)
    while q:
        node = q.popleft()
        print(node)
        for i in info_list[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n = 5
info_list = [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
bfs(1)

print('--------------------------------')


def dfs(node):
    visitedd[node] = True  # 자기처리
    print(node)
    for i in connected_list[node]:
        if not visitedd[i]:
            dfs(i)


nums = 5  # node가 5개
connected_list = [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
visitedd = [False] * (nums+1)
dfs(1)

print('--------------------------------')


def permutation(arr, visit, check):
    """
    순열 재귀로 구현
    :param arr: 순열을 돌릴 수열을 저장한 리스트
    :param visit: 순열이 쌓이는 리스트
    :param check: 들린노드를 체크하는 리스트
    """
    if len(visit) == len(arr):
        # 만약 visit이 원래 수열의 길이와 같다면 출력
        print(visit)
    else:
        for i in range(len(arr)):  # 0 1 2
            # 후보군을 전부 다 돌면서 이미 들린 노드인지 아닌지 체크
            if check[i] is not True:  # 만약 들리지 않은 노드라면 visit 리스트에 추가하고 check에 들린 노드 표시
                visit.append(arr[i])
                check[i] = True
                permutation(arr, visit, check)
                # 재귀를 빠져나온 뒤 원위치
                visit.pop()
                check[i] = False
            else:
                continue  # 만약 들린 노드라면 더 이상 탐색하지 않음


arr = [1, 2, 3]
permutation(arr, [], [False for _ in range(len(arr))])