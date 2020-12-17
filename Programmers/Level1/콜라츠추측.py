def solution(num):
    cnt = 0
    while True:
        if cnt >= 500:
            if num != 1:
                return -1
        else:
            if num == 1:
                return cnt

        if num % 2 == 0:
            num = num // 2
            cnt += 1
        else:
            num = (num*3) + 1
            cnt += 1

# 1
num = 6

# 2
# num = 16

# 3
# num = 626331

print(solution(num))