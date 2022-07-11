import sys

x = int(sys.stdin.readline())

for _ in range(x):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
