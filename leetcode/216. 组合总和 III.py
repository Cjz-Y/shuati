from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def back(result, index, num, m):

            # print("result = %s, index = %d, num = %d, m = %d" % (result, index, num, m))
            if num == k - 1:
                if m not in use and 10 > m >= index:
                    temp = result.copy()
                    temp.append(m)
                    ans.append(temp)
                return

            for i in range(index, 10):
                if m - i > 0:
                    use.add(i)
                    result.append(i)
                    back(result, i + 1, num + 1, m - i)
                    result.pop()
                    use.remove(i)

        use = set()
        ans = []

        back([], 1, 0, n)

        return ans