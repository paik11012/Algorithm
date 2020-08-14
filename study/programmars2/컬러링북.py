from pprint import pprint

def solution(m, n, picture):
    answer = 32
    pprint(picture)
    return answer

m = 6	
n = 4	
picture= [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

print(solution(m, n, picture))

'''bfs생각하기
'''