# DFS



```python
def DFS(y):
	visited = [0] * (8)
	stack = [0] * 1-
	top = -1
	
	top += 1  # push
	stack[top] = v
	
	while top =! 1:  # 스택이 비어있을 때까지
		v = stack[top]  # v는 스택 맨 위에 있는 것
        top -= 1
        if visited[v] != 1:  # 방문 안했으면 자기처리
            visited[v] = 1
            print(v)  # 이동경로 표시하기
            for i in range(1, 8):  # 이웃처리, 방문 안했으면 스택에 넣기
                if G[v][i] and not visited[i]:  # 
                    top += 1
                    stack[top] = i  # 맨 위에 것 빼내기
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7]
visited = [0]
G = [[0]*8 for _ in range(8)]	
```

```python
def DFS(y):
	print(v)
	visited[v] = True
	for i in range(1, 8): 
		if G[v][i] and not visited[i]:  # 
         	DFS(i)
         	
         	
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0]
G = [[0]*8 for _ in range(8)]
```

## 

## 좋은방법 경로 찾기

```python
num = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]

visited = [False] * 8
stack = []  # 방문할 곳
path = []
stack.append(1)  # 1

while stack:  # stack이 0이 될 때까지
    node = stack.pop()
    if not visited[node]:  # visited의 값이 false라면
        visited[node] = True
        path.append(node)  # 1
        stack += num[node]  # 2 3

result = ''
for i in path:
    result += str(i)
print(result)
```

## 1267 작업순서

```

```





# 백트래킹

뒤지다가 갈 필요 없으면 안가기







## 퀵정렬

가운데 기준, 가운데보다 작은건 왼쪽으로 큰건 왼쪽으로

(가운데 = 피봇)

