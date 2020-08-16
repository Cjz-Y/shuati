from typing import List


class Solution:

    def back(self, not_full, not_start, result):
        if not_start == 0 and not_full == 0:
            self.ans.append(result)
            return

        if not_full > 0:
            self.back(not_full - 1, not_start, result + ')')
        if not_start > 0:
            self.back(not_full + 1, not_start - 1, result + '(')



    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.back(0, n, '')
        return self.ans