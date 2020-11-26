import sys

sys.stdin = open("1216.회문2.txt", 'r')

# 1
# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(map(str, input())) for _ in range(100)]
#     arr1 = list(zip(*arr))

#     res = 0
#     c_tmp = 0
#     r_tmp = 0
#     for i in range(100):
#         for j in range(100):
#             for k in range(99, 0, -1):
#                 if arr[i][j:k+j] == arr[i][j:k+j][::-1]:
#                     c_tmp = len(arr[i][j:k+j])
#                     break
#                 if arr1[i][j:k+j] == arr1[i][j:k+j][::-1]:
#                     r_tmp = len(arr1[i][j:k+j])
#                     break
#                 if res < max(r_tmp, c_tmp):
#                     res = max(r_tmp, c_tmp)
    
#     print(f"#{tc} {res}")


# 2
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    arr1 = list(zip(*arr))
 
    for k in range(99, 0, -1):
        for i in range(100):
            for j in range(101 - k):
                if arr[i][j:k+j] == arr[i][j:k+j][::-1]:
                    print(f"#{tc} {k}")
                    break
                if arr1[i][j:k+j] == arr1[i][j:k+j][::-1]:
                    print(f"#{tc} {k}")
                    break
             
            else: 
                continue
            break
        else: 
            continue
        break