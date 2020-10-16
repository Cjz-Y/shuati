class Solution:
    def maxDepth(self, s: str) -> int:

        temp = -1
        left_index = -1

        ans = 0

        index = 0
        while index < len(s):
            if s[index] == '(':
                if temp == -1:
                    temp = 1
                    left_index = index
                else:
                    temp += 1
            elif s[index] == ')':
                temp -= 1
                if temp == 0:
                    deep = self.maxDepth(s[left_index + 1: index])
                    ans = max(ans, deep + 1)

                    temp = -1
                    left_index = -1

            index += 1

        return ans
