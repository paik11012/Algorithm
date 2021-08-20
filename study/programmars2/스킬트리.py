'''BACDE와 같은 스킬들을 하나하나 보면서
그 순서가 CBD이면 답에 더하고
그렇지 않으며 break'''

def solution(skill, skill_trees):
    answer = 0
    skill_list = []  # ['C', 'CB', 'CBD']
    for s in range(len(skill)):
        skill_list.append(skill[0:s+1])
    
    for one_skill in skill_trees:  # BACDE
        temp = ''
        for o in one_skill:
            if o in skill:  # 해당하는 것만 남기기
                temp+=o
        for possible_skill in skill_list:
            if possible_skill == temp:
                answer += 1
        # print(temp)
        if temp == '': answer += 1  # 해당하는게 하나도 없는 스킬도 가능하다 
    return answer


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA", "E"]))  # 답3
