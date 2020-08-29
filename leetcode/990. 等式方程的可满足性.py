from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        parent = [i for i in range(26)]
        start_index = ord('a')

        for equation in equations:
            if equation[1] == '=':
                one = ord(equation[0]) - start_index
                two = ord(equation[3]) - start_index

                while parent[one] != one:
                    parent[one] = parent[parent[one]]
                    one = parent[parent[one]]

                while parent[two] != two:
                    parent[two] = parent[parent[two]]
                    two = parent[parent[two]]

                parent[one] = two

        for equation in equations:
            if equation[1] == '!':
                one = ord(equation[0]) - start_index
                two = ord(equation[3]) - start_index

                while parent[one] != one:
                    parent[one] = parent[parent[one]]
                    one = parent[parent[one]]

                while parent[two] != two:
                    parent[two] = parent[parent[two]]
                    two = parent[parent[two]]

                if one == two:
                    return False
        return True
