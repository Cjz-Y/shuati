from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        current = '0' * n
        ans = [current]
        use = set()
        use.add(current)

        while current:

            next = None
            sl = list(current)

            for i in range(len(current)):
                if sl[i] == '0':
                    sl[i] = '1'
                else:
                    sl[i] = '0'

                temp = ''.join(sl)
                if temp not in use:
                    use.add(temp)
                    next = temp
                    ans.append(temp)

                    break
                else:
                    if sl[i] == '0':
                        sl[i] = '1'
                    else:
                        sl[i] = '0'

            current = next

        ans = [int(item, 2) for item in ans]

        return ans

