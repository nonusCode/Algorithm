def solution(arr1, arr2):
    tmp = []
    res = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        res.append(tmp)
        tmp = []
    
    return res

# 1
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

# 2
# arr1 = [[1], [2]]
# arr2 = [[3], [4]]

print(solution(arr1, arr2))