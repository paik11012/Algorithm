def solution(board, moves):
    global answer
    copy = board
    q = [0]
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

