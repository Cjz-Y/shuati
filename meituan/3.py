import sys

n = map(int, sys.stdin.readline().strip())

a = list(map(int, sys.stdin.readline().strip().split()))

ans = a[0]

for i in range(1, len(a)):
    ans ^= a[i]

for i in range(1, n):
    for j in range(1, i + 1):
