import sys

n, p, q = map(int, sys.stdin.readline().strip().split())

f = [0 for i in range(n)]

a = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(a)):
    f[a[i]] = 1

a = list(map(int, sys.stdin.readline().strip().split()))

all = 0
for num in a:
    f[num] += 1
    if f[num] == 2: all += 1

print(p - all, q - all, all)
