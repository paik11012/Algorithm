def battle(card1, card2):
    if data[card1] == data[card2]:  # 카드의 번호가 작은것이 승리
        if data[card1] < data[card2]:
            return card1
        return card2
    if data[card1] == '1': # 가위
        if data[card2] == '2'  # 바위
            return card2
        else: return card1
    if data[card1] == '2': # 바위
        if data[card2] == '3'  # 보
            return card2
        else: return card1
    if data[card1] == '3': # 보
        if data[card2] == '1':  # 가위
            return card2
        else: return card1


def mydiv(s, e):  # 순서 번호 입력
    # 종료 조건
    if s == e:  # 한 장으로 나눠진 경우
         return s
    # 여러장인 경우
    p = (s + e) // 2 # 기준점
    card1 = mydiv(s, p)  # 한 장까지 분할하라, 카드의 번호를 반환하라
    card2 = mydiv(p+1, e)
    # 여기서 둘 매치
    winner_no = battle(card1, card2)
    return winner_no  # 승자의 카드 인덱스 반환



n = 6
data = [2, 1, 1, 2, 3, 3]
winner = mydiv(0, n-1)
print(winner+1)