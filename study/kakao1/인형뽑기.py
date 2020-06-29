'''
이 문제의 키 포인트: 새로운 숫자를 넣을 때 이미 큐에 있는 맨 마지막 숫자랑 비교하자
그리고 인형을 뽑은 후 그 자리를 0으로 바꿔 주어야 한다

처음 생각한 방향: 재귀함수를 쓰면 어떨까?(새로운게 들어오면 없애고 다시 비교 시작)
그러나 너무 복잡...
'''

def solution(board, moves):
    global answer
    copy = board
    q = [0] # 시작 시 비교 대상이 있어야 하므로 넣기
    for a in range(len(moves)): # a갯수만큼 1 5 3 5 1 2 1 4
        for i in range(len(board)):
            if copy[i][moves[a]-1] != 0:
                if q[-1] == copy[i][moves[a]-1]: # 같으면
                    q.pop()
                    answer += 2
                else: # 다르면
                    q.append(copy[i][moves[a]-1])
                copy[i][moves[a]-1] = 0 # 바꿔주기
                break
    print(q)
    return answer
# [0, 4, 3, 1, 1, 3, 2, 4]
answer = 0
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))

