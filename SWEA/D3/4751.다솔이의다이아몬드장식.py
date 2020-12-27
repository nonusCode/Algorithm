import sys

sys.stdin = open("4751.다솔이의다이아몬드장식.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()

    print(".."+"#"+"...#"*(len(S)-1)+"..\n"+"."+"#."*(len(S)*2)+"\n"+"#."+".#.".join(S)+".#\n"+"."+"#."*(len(S)*2)+"\n"+".."+"#"+"...#"*(len(S)-1)+"..")