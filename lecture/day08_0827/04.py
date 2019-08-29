def find_min(n):
    pass



n = 3
mymap = [[2, 1, 2],[5, 8, 5],[7, 2, 2]]
visited = [0] * n
mymin = 99999 # 최소값 저장용
submin = 0 #중간 열별 값 저장용, 최소값보다 작으면 최소값에 저장
find_min(0)
print(mymin)