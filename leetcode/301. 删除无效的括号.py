from typing import List



class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def back_ans(index, result: str):
            if index == len(middle):
                ans.append(result)
                return

            for i in range(len(middle[index])):
                back_ans(index + 1, result + middle[index][i])


        def back(str, index, delete_num):
            # 通过回溯来得到中间的正确结果

            print('back start: str = %s, index = %d, delete num = %d' % (str, index, delete_num))

            # 如果index > len(pos) 或者是当前需要删除的右括号 == 0，则可以记录一次结果了
            if delete_num == 0:
                temp_middle.append(''.join(str))
                return
            if index < 0:
                return

            n = len(pos[index]) - 1
            # 当前需要删除几个右括号，他的取值的最小值为 需要删减的右括号减去右边还剩下多少右括号，保证这一趟回溯是合法的
            for i in range(max(0, delete_num - left_have[index]), min(len(pos[index]), delete_num) + 1):
                temp_str = str.copy()
                # print(temp_str, index, i, pos[index], start, n)

                for j in range(i):
                    print(n - j)
                    print(pos[index][n-j])
                    print(pos[index][n - j] - start)
                    del temp_str[pos[index][n - j] - start]

                back(temp_str, index - 2, delete_num - i)

        ans = []
        middle = []

        # 将每一段需要整理的字符串进行整理 (())()) -> 2212 -> [[0,1],[2,3],[4],[5,6]] 因为过程中还会出现字母，所以需要记录索引值
        pos = []

        temp = 0
        index = 0

        # 去除掉开始不是括号的字符
        while index < len(s) and s[index] != '(' and s[index] != ')':
            index += 1
        middle.append([s[:index]])

        start = index
        while index < len(s):
            # 如果是左括号的话 一直往前遍历 知道碰到右括号  然后记录左括号的索引
            if s[index] == '(':
                temp_pos = []

                while index < len(s) and s[index] != ')':
                    if s[index] == '(':
                        temp_pos.append(index)
                        temp += 1
                    index += 1

                pos.append(temp_pos)

            # 如果是右括号的话 一直往前遍历 直到碰到左括号  然后记录右括号的索引
            elif s[index] == ')':
                temp_pos = []

                while index < len(s) and s[index] != '(':
                    if s[index] == ')':
                        temp_pos.append(index)
                        temp -= 1
                    index += 1

                pos.append(temp_pos)


                # 如果出现temp<0，则说明当前这段字符串不合法，右括号多了，需要删减右括号， 当前这段字符的起止为 start:index + 1
                if temp < 0:
                    # 整理右括号多的情况
                    temp_middle = []
                    temp_str = list(s[start:index])


                    # 左边 还有多少括号
                    left_have = [0 for i in range(len(pos))]
                    for i in range(3, len(pos), 2):
                        left_have[i] = left_have[i - 2] +len(pos[i - 2])

                    back(temp_str, len(pos) - 1, -temp)

                    middle.append(temp_middle)
                    start = index
                    pos = []
                    temp = 0
            print('start = %d, temp = %d' % (start, temp))

        print('循环结束括号情况 temp = %d' % temp)
        # 整理左括号多的情况
        if temp > 0:
            print("处理左括号的问题")


            temp_str = list(s[start:index])
            print("start = %d" % start)
            print('temp str = %s' % temp_str)

            # 判断是否有结尾的左括号，有的话 直接删除
            if len(pos) % 2 == 1:
                for i in range(len(pos[-1]) - 1, -1, -1):
                    # print(pos[-1][i] - start)
                    del temp_str[pos[-1][i] - start]
                    temp -= 1
                pos.pop()

            print("删除完结尾多余括号之后")
            print(temp_str, pos)

            # 如果是删除左括号，开始配对号的括号队中的左括号是无法删除的 ()(() -> 第一个左括号是无法删除的
            index = 1
            end_pos = start
            while index < len(pos) and len(pos[index]) == len(pos[index - 1]):
                if index + 1 < len(pos):
                    end_pos = pos[index + 1][0]
                else:
                    end_pos = len(s)
                del pos[1]
                del pos[0]
                print(pos)

            middle.append([''.join(temp_str[:end_pos - start])])
            temp_str = temp_str[end_pos - start:]
            start = end_pos

            print("处理完前面正常配对之后")
            print(temp_str, pos)




            # 整理右括号多的情况


            left_have = [0 for i in range(len(pos))]
            for i in range(2, len(pos), 2):
                left_have[i] = left_have[i - 2] + len(pos[i - 2])

            temp_middle = []
            back(temp_str, len(pos) - 2, temp)
            middle.append(temp_middle)

        else:
            temp_middle = [s[start:index]]
            middle.append(temp_middle)

        print('middle = %s' % middle)
        back_ans(0, "")

        return ans


if __name__ == '__main__':
    a = "()(()(("

    print(Solution().removeInvalidParentheses(a))

