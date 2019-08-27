num = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
visited = [False] * 8
# stack = []
# node = []
# stack.append(1)
# while stack != []:  # stack에 뭐가 있는 동안 (while stack:)
#     node = stack.pop()
#     if visited[node] == False:
#         visited[node] = True
#         print(node, end = '')
#         stack += num[node]
#         #stack.extends(num[node])
#         #stack = stack + num[node]
​
​
def dfs(node):  # 기다리고 있다는 것 기억!!!! 안에 있던 것들이 끝나야 처음에 들어갔던 1까지 끝난다   
    visited[node] = True
    print("{0} ".format(node), end='')
    for i in num[node]: # [2, 3]
        if visited[i] == False:
            dfs(i)
​
dfs(1)  # dfs는 반환하는 함수가 아니라 node 각각을 출력하는 함수