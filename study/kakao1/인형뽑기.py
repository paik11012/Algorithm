def solution(board, moves):
    copy = board
    q = []
    for a in range(len(moves)): # a갯수만큼 1 5 3 5 1 2 1 4
        for i in range(5):
            if copy[i][moves[a]-1] != 0:
                q.append(copy[i][moves[a]-1])
                copy[i][moves[a]-1] = 0 # 바꿔주기    
                break
    answer = 0
    # q = [4, 3, 1, 1, 3, 2, 4]
    lenq = (len(q) * len(q-1)) // 2
    print(lenq)
    # for j in range(lenq): # 6 번 동안 확인
    #     if q[j] == q[j+1]:
    #         q.pop(j)
    #         q.pop(j+1)
    #         lenq -= 2
    #         print(lenq)
    # return answer