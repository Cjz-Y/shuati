from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        l = list(s)
        l.sort()
        ans = []
        use = set()
        def back(result, index):
            if index == len(s):
                ans.append(result)
                return

            for i in range(len(l)):
                if i not in use and (i == 0 or l[i] != l[i - 1] or (i - 1) in use):
                    use.add(i)
                    back(result + l[i], index + 1)
                    use.remove(i)

        back('', 0)
        return ans

