def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)

# 1
s = "AB"
n = 1

# 2
# s = "z"
# n = 1

# 3
# s = "a B z"
# n = 4

print(solution(s, n))