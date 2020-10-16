class Solution:
    def totalNQueens(self, n: int) -> int:


        def search(index, result):

            if index == n:
                nonlocal ans
                ans += 1
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
        ans = 0

        search(0, [])

        return ans