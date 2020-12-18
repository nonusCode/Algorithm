def solution(phone_number):
    res = len(phone_number[:-4]) * '*' + phone_number[-4:]
    
    return res

# 1
phone_number = "01033334444"

# 2
# phone_number = "027778888"

print(solution(phone_number))