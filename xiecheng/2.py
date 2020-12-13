import sys

line = sys.stdin.readline().strip()

operation = []
num = []

index = 0
flag = 1
while index < len(line):
    if line[index] == '|' or line[index] == '&':
        operation.append(line[index:index + 2])
        index += 2
    else:
        if line[index] == '!' or line[index] == '(':
            operation.append(line[index])
        # 如果index 是操作数的话
        elif line[index] == 'T' or line[index] == 'F':
            # 如果操作栈顶是！, 直接逆转然后放在num中
            if operation and operation[-1] == '!':
                if line[index] == 'T':
                    num.append('F')
                else:
                    num.append('T')
                operation.pop()
            # 如果操作栈顶是&&，那么判断是否有效，有效的话，计算一波
            elif operation and operation[-1] == "&&":
                if not num:
                    flag = -1
                    break

                if num[-1] == 'F' or line[index] == 'F':
                    num[-1] = 'F'
                operation.pop()
            # 其他的先不用管，直接进站吧
            else:
                num.append(line[index])
        # 是)括号
        else:
            while operation[-1] != '(':
                a = num.pop()
                b = num.pop()
                if a == 'T' or b == 'T':
                    num.append('T')
                else:
                    num.append('F')
                operation.pop()
            operation.pop()

        index += 1

if flag == -1:
    print(-1)
else:
    while operation:

        if operation[-1] == '||':
            a = num.pop()
            b = num.pop()
            if a == 'T' or b == 'T':
                num.append('T')
            else:
                num.append('F')
        elif operation[-1] == '&&':
            a = num.pop()
            b = num.pop()
            if a == 'T' and b == 'T':
                num.append('T')
            else:
                num.append('F')
        else:
            a = num.pop()
            if a == 'T':
                num.append('F')
            else:
                num.append('T')

        operation.pop()
    print(num[-1])



