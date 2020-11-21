import sys

s = sys.stdin.readline().strip().split()

temp = 0
for char in s:
    if char.islower():
        temp += 1

print(abs(len(s) - temp - temp) // 2)