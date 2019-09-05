import sys
sys.stdin = open('세로읽기.txt', 'r')
tc = int(input())  # 6 4 5 6 6
for tcc in range(1, tc + 1):
    print('#{} '.format(tcc), end='')
    character = []  # [['A', 'A', 'B', 'C', 'D', 'D'], ['a', 'f', 'z', 'z'], ['0', '9', '1', '2', '1'], ['a', '8', 'E', 'W', 'g', '6'], ['P', '5', 'h', '3', 'k', 'x']]
    maxx = 0  # 가장 긴 글자 수
    for i in range(5):
        cha = str(input())
        character.append(list(cha))
        if maxx < len(cha):
            maxx = len(cha)
    for j in range(5): # 몇 개가 부족한 것인가
        if (maxx - len(character[j])) >= 1:
            for i in range(maxx - len(character[j])):
                character[j].append('')  # 부족한 부분 모두 0으로 채우기
    for x in range(maxx):
        for y in range(5):
            print(character[y][x], end='')
    print()