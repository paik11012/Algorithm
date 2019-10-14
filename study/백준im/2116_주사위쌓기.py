import sys
import copy
sys.stdin = open('2116.txt','r')
n = int(input())
t_dices = []
for j in range(n):
    k = list(map(int, input().split()))
    t_dices.append(k)

result = []
for k in range(6):  # 처음 여섯개 할당
    dices = []  # 여기서 카피를 해야지 그 만큼 사용 가능
    dices = copy.deepcopy(t_dices)
    bottom = k
    if bottom == 0:  # 위치
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
    d = 1  # 주사위 번호
    bot = dices[0][k]
    dices[0].remove(bot)
    dices[0].remove(top)
    # print('top', top)  # 2 4
    # print(dices)  # 2 3 1 6 5 4
    print(dices)
    for d in range(1, 6):  # 1 2 3 4 5 # 주사위번호 d를 한개씩 늘려서 5가 될 때까지 돌리기
        print(dices[d])
        # bot_idx = dices[d].index(bot)
        # print(bot_idx)
    #     if bot_idx == 0:  # 위치
    #         topp = dices[d][5]
    #     elif bot_idx == 1:
    #         topp = dices[d][3]
    #     elif bot_idx == 2:
    #         topp = dices[d][4]
    #     elif bot_idx == 3:
    #         topp = dices[d][1]
    #     elif bot_idx == 4:
    #         topp = dices[d][2]
    #     elif bot_idx == 5:
    #         topp = dices[d][0]
    #     bot = dices[d][bot_idx]
    #     dices[d].remove(bot)
    #     dices[d].remove(topp)
    # print(dices)




