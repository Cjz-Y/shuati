from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def search(index, result):
            if index == n:
                temp_ans = []
                for i in range(n):
                    temp_str = ['.' for i in range(n)]
                    temp_str[result[i]] = 'Q'
                    temp_str = ''.join(temp_str)
                    temp_ans.append(temp_str)

                ans.append(temp_ans)
                return

            for i in range(n):
                if i not in use and i + index not in beside_sum and i - index not in beside_diff:
                    beside_sum.add(i + index)
                    beside_diff.add(i - index)
                    use.add(i)

                    result.append(i)
                    search(index + 1, result)
                    result.pop()

                    beside_sum.remove(i + index)
                    beside_diff.remove(i - index)
                    use.remove(i)




        beside_sum = set()
        beside_diff = set()
        use = set()
        ans = []

        search(0, [])

        return ans
