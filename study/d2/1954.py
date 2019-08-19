from pprint import pprint
l=[]  # 숫자 전체 리스트
num = 4
for i in range(1, (num*num)+1): # 1부터 16
    l.append(i)
t = len(l)//num; result=[]; start=0  # t = 4
for j in range(1,t+1):  # 1 2 3 4
    end = num * j  # 4 8 12 16
    result.append([i for i in l[start:end]])  #리스트채로 append 4개씩
    start = end  # start를 방금 end 즉 4로 바꾸어라
    
pprint(result)
dx = [0,1,0,-1] #우 하 좌 상
dy = [1,+0,-1,0]

def iswall(x,y):
    if x < 0 or x >= num+1: return True
    elif y < 0 or y >= num_1: return True
    else result[x][y] =! 0: return True


for x in range(result):
    for y in range(result[0]):
        for i in range(num):
            testX = x + dx[i]
            testY = y + dy[i]


            if iswall(testX,testY) == False:
                





