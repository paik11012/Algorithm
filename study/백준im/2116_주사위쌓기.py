#  포문 6개 돌리고(각 숫자) 그리고 그 각 숫자에서 주사위 갯수 만큼 포문 돌리기
# 1~6 어디서 시작할 것인지 정하고, 각각 옆면에 올 수 있는 숫자 중 가장 큰 숫자 찾기
# copy 이용하기
import sys
import copy
sys.stdin = open('2116.txt','r')
n = int(input())
t_dices = []
for j in range(n):
    k = list(map(int, input().split()))
    t_dices.append(k)
maxx = 0
for k in range(6):  # 처음 여섯개 할당(주사위 1~6 어느것에서 시작할 것인가 확인)
    dices = []  # 여기서 카피를 해야지 for문의 갯수 만큼 사용 가능
    dices = copy.deepcopy(t_dices)
    bottom = k  # 0~5
    if bottom == 0:  # 위치 짝지어 주기
        top = dices[0][5]
    elif bottom == 1:
        top = dices[0][3]
    elif bottom == 2:
        top = dices[0][4]
    elif bottom == 3:
        top = dices[0][1]
    elif bottom == 4:
        top = dices[0][2]
    elif bottom == 5:
        top = dices[0][0]
    bot = dices[0][k]
    dices[0].remove(bot)  # bottom, top은 최댓값 구하는데 사용하지 않으니 지우기
    dices[0].remove(top)
    for d in range(1, n):  # 1 2 3 4 5 # 주사위번호 d를 한개씩 늘려서 5가 될 때까지 돌리기
        bot_idx = dices[d].index(top)  # 위치 이용해 짝 할당
        if bot_idx == 0:  # 위치
            topp = dices[d][5]
        elif bot_idx == 1:
            topp = dices[d][3]
        elif bot_idx == 2:
            topp = dices[d][4]
        elif bot_idx == 3:
            topp = dices[d][1]
        elif bot_idx == 4:
            topp = dices[d][2]
        elif bot_idx == 5:
            topp = dices[d][0]
        bot = dices[d][bot_idx]
        del dices[d][bot_idx]  # bot, top 지우기
        dices[d].remove(topp)
        top = topp  # for문의 top자리에 topp넣기
    temp = 0
    for i in range(n):
        temp += max(dices[i])
    if temp > maxx:  # 최댓값 maxx에 저장하기
        maxx = temp
        # print(maxx)
print(maxx)
