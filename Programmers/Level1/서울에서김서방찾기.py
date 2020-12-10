def solution(seoul):
    for i, v in enumerate(seoul):
        if v == "Kim":
            res = f"김서방은 {i}에 있다"

    return res

# 1
seoul = ["Jane", "Kim"]

print(solution(seoul))