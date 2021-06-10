def solution(absolutes, signs):
    res = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            res += absolutes[i]
        else:
            res -= absolutes[i]
    
    return res

# 1
absolutes = [4, 7, 12]
signs = [True, False, True]

# 2
# absolutes = [1, 2, 3]
# signs = [False, False, True]

print(solution(absolutes, signs))