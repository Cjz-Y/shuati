import sys

s = sys.stdin.readline().strip()

encode_s = []
for item in s:
    encode_s.append(str(ord(item) - ord('A')))

encode_s = ''.join(encode_s)
f = [-1 for i in range(len(encode_s))]

def back(index, string):
    if index > len(string):
        return 0
    if index == len(string):
        return 1
    # print(index)
    if f[index] != -1:
        return f[index]

    result_1 = back(index + 1, string)
    # print(index, result_1)
    f[index] = result_1
    if string[index] != '0' and index + 1 < len(string) and int(string[index:index + 2]) <= 25:
        result_2 = back(index + 2, string)
        # print(index, result_2)
        f[index] += result_2
    return f[index]

back(0, encode_s)
print(f[0] - 1)
