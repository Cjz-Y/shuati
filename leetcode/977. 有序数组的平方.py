from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        max_value = -999999
        min_value = 999999
        index = -1

        ans = []

        for i in range(len(A)):
            max_value = max(max_value, A[i])
            min_value = min(min_value, A[i])
            if A[i] == 0 or (i >= 1 and A[i] * A[i - 1] < 0):
                index = i

        if max_value * min_value < 0:
            # print(index)
            left = index - 1
            right = index
            while left >= 0 or right < len(A):
                # print(left, right, (left >= 0 and right >= len(A)))
                # 取left
                if left >= 0 and (right >= len(A) or abs(A[left]) <= abs(A[right])):
                    ans.append(A[left] ** 2)
                    left -= 1

                if right < len(A) and (left < 0 or abs(A[left]) >= abs(A[right])):
                    ans.append(A[right] ** 2)
                    right += 1
            return ans
        else:
            if (max_value * min_value == 0 and max_value == 0) or (max_value < 0):
                for i in range(len(A) - 1, -1, -1):
                    ans.append(A[i] ** 2)
                return ans

            ans = [a ** 2 for a in A]
            return ans

