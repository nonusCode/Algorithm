import sys

sys.stdin = open("5515.2016년요일맞추기.txt", 'r')

# 1
for tc in range(1, int(input())+1):
    m, d = map(int, input().split())

    sol = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = 3
    for i in range(m-1):
        res += sol[i]
    res += d
 
    print(f"#{tc} {res % 7}")

# 2
# from calendar import weekday

# for tc in range(1, int(input())+1):
#     m, d = map(int, input().split())

#     print(f"#{tc}", weekday(2016, m, d))

# 3
# from datetime import date

# for tc in range(1, int(input())+1):
#     m, d = map(int, input().split())

#     print(f"#{tc}", date(2016, m, d).weekday())