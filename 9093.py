import sys

T = int(sys.stdin.readline())
for _ in range(T) :
    s = list(sys.stdin.readline().rstrip().split())

    ss = []
    for i in s :
        ss.append(i[::-1])

    print(*ss)
