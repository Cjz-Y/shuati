from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def back(index, result: str):
            if index == len(middle):
                ans.append(result)
                return

            for i in range(len(middle[index])):
                back(index + 1, result + middle[index][i])


        ans = []
        middle = []

        start = 0
        zuo = []
        you = []

        temp = 0
        index = 0
        while index < len(s):
            if s[index] == '(':
                temp += 1
                zuo.append(index)
            elif s[index] == ')':
                you.append(index)
                if temp != 0:
                    temp -= 1
                else:
                    # 整理右括号多的情况
                    temp_middle = []
                    temp_str = list(s[start:index + 1])

                    for i in range(len(you)):
                        if i == 0 or you[i] != you[i - 1] + 1:
                            temp_ans_str = temp_str.copy()
                            temp_ans_str.pop(you[i] - start)
                            temp_middle.append(''.join(temp_ans_str))

                    middle.append(temp_middle)
                    start = index + 1
                    zuo = []
                    you = []
                    temp = 0
            index += 1

        # 整理左括号多的情况
        if temp > 0:
            # 整理右括号多的情况
            temp_middle = []
            temp_str = list(s[start:index])

            for i in range(len(zuo)):
                if i == 0 or zuo[i] != zuo[i - 1] + 1:
                    temp_ans_str = temp_str.copy()
                    temp_ans_str.pop(zuo[i] - start)
                    temp_middle.append(''.join(temp_ans_str))

            middle.append(temp_middle)
        else:
            temp_middle = [s[start:index]]
            middle.append(temp_middle)


        back(0, "")

        return ans






