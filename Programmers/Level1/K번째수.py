def solution(array, commands):
    res = []
    for i in range(len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        res.append(tmp[commands[i][2]-1])
    
    return res

# 1
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))