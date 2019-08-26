from pprint import pprint
for T in range(int(input())):
    n = int(input())
    box = []
    for _ in range(n):
        box.append(list(map(int,input().split())))
    
    islands = []
    dx = [-1,-1,0,1,1]
    dy = [0,-1,-1,-1,0]
    for i in range(n):
        for j in range(n):
            if box[i][j] == 0: continue
            isAdded= False
            for island in islands:
                for d in range(5):
                    if not 0<=i+dy[d]<n: continue
                    if not 0<=j+dx[d]<n: continue
                    if box[i+dy[d]][j+dx[d]] == 0 : continue
                    if (i+dy[d], j+dx[d]) in island:
                        if (i,j) not in island:
                            island.append((i,j))
                            isAdded = True
                            break
            if not isAdded:
                islands.append([(i,j)])
    #first 
    merge = 1
    while merge > 0:
        merge = 0 
        for i in range(len(islands)-1):
            for area in islands[i]:
                for area1 in islands[i+1]:
                    if abs(area[0]-area1[0])<=1 and abs(area[1]-area1[1])<=1:
                        merge +=1
                        break
                if merge >0:
                    break
            if merge >0:
                break
        if merge > 0:
            islands[i] = islands[i] + islands[i+1]
            del(islands[i+1])
            
            

    
    print('#{} {}'.format(T+1, len(islands)))