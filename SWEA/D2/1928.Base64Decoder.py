import sys
from base64 import b64decode

sys.stdin = open("1928.Base64Decoder.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()
    
    print(f"#{tc} {b64decode(S).decode('UTF-8')}")