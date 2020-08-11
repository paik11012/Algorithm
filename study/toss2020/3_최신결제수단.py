'''최근 사용한 결제수단 리스트, 5개 까지, 중복 없음'''
def solution(chars):
    answer = ''
    card_list = []
    cards = chars.split(' ')
    for card in cards:
        if card not in card_list:
            card_list.append(card)
            answer = card + ' ' + answer
            print(answer)

chars = '우리 우리 우리 하나 우리 국민'
print(solution(chars))