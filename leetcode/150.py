from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if '+' == token or '-' == token or '*' == token or '/' == token:
                first = stack.pop()
                second = stack.pop()
                if '+' == token:
                    new = first + second
                elif '-' == token:
                    new = second - first
                elif '*' == token:
                    new = second * first
                else:
                    new = int(second / first)
                stack.append(new)
            else:
                stack.append(int(token))

        return stack.pop()


