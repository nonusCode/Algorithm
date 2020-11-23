import sys

sys.stdin = open("2056.연월일달력.txt", 'r')

for tc in range(1, int(input())+1):
    N = input()

    res = ''
    if N[5] == '0':
        res = -1
    elif N[5] == '2' and N[6] == '3' or N[7] == '9':
        res = -1
    else:
        res = f"{N[:4]}/{N[4:6]}/{N[6:]}"
    
    print(f"#{tc} {res}")