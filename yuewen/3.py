import sys

n = int(sys.stdin.readline().strip())

data = []
for i in range(n):
    line = sys.stdin.readline().strip().split(',')
    data.append(line)

def better(a, b):
    return a[1] > b[1] or (a[1] == b[1] and (a[3] > b[3] or (a[3] == b[3] and (a[2] > b[2] or (a[2] == b[2] and a[0] >= b[0])))))

def qsort(head, tail, data):
    if head < tail:
        i, j = head, tail
        temp = data[head]
        while i < j:
            while i < j and better(data[j], temp):
                j -= 1
            data[i] = data[j]
            while i < j and better(temp, data[i]):
                i += 1
            data[j] = data[i]
        data[i] = temp
        qsort(head, i - 1, data)
        qsort(i + 1, tail, data)

qsort(0, len(data) - 1, data)

for i in range(len(data)):
    print(data[i][0])