class Solution:
    def calculate(self, s: str) -> int:
        int_start = ord('0')
        int_end = ord('9')

        num = []
        opr = []
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue

            if int_start <= ord(s[index]) <= int_end:
                temp = index
                while temp < len(s) and int_start <= ord(s[temp]) <= int_end:
                    temp += 1
                integer = int(s[index:temp])
                num.append(integer)

                if len(opr) != 0:
                    if opr[-1] == '*':
                        a = num.pop()
                        b = num.pop()
                        num.append(a * b)
                        opr.pop()
                    elif opr[-1] == '/':
                        a = num.pop()
                        b = num.pop()
                        num.append(b // a)
                        opr.pop()


                index = temp


            elif s[index] == '+' or s[index] == '-' or s[index] == '*' or s[index] == '/':
                opr.append(s[index])
                index += 1

        while opr:
            operation = opr.pop()
            a = num.pop()
            b = num.pop()
            if opr and opr[-1] == '-':
                if operation == '+':
                    num.append(b - a)
                else:
                    num.append(b + a)
            else:
                if operation == '+':
                    num.append(b + a)
                else:
                    num.append(b - a)

        return num[-1]

