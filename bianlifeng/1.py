import sys

s = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

swap_map = {}
for i in range(n):
    temp = sys.stdin.readline().strip()
    index = temp.find('->')
    key = temp[:index]
    value = temp[index + 2:]
    swap_map[key] = value


ans = []
str_start = 0
left = -1
right = -1
for i in range(len(s)):
    if s[i] == "{" and s[i - 1] == "{":
        left = i + 1
    if s[i] == "}" and s[i - 1] == "}":
        if left != -1 and i - left == 1:
            ans.append(s[str_start: left - 2])
            ans.append("{{}}")
            left = -1
            str_start = i + 1

        if left != -1:
            temp = s[left:i - 1]
            temp = swap_map.get(temp, temp)
            ans.append(s[str_start:left - 2])
            ans.append(temp)
            left = -1
            str_start = i + 1

ans.append(s[str_start:])
print(''.join(ans))

