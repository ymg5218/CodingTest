def solution(skill, skill_trees):
    answer = 0
    
    # 키 : 값
    # 스킬 : 순번
    skill_dict = {}

    for i in range(len(skill)):
        skill_dict[skill[i]] = i
    
    for skill_tree in skill_trees:
        seq = 0
        isValid = True

        # 순번에 맞지 않게 먼저 마스터하려는 스킬 있는지 탐색
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill_dict:
                # 순번에 맞는 순서의 스킬이면 seq + 1
                if skill_dict[skill_tree[i]] == seq:
                    seq += 1
                # 아니면 불가능한 스킬트리
                else:
                    isValid = False
        if isValid:
            answer += 1

    return answer

if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    
    print(solution(skill, skill_trees))