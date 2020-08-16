from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        is_all_nine = True
        for digit in digits:
            if (digit != 9):
                is_all_nine = False
                break

        if is_all_nine:
            result = [1]
            for i in range(len(digits)):
                result.append(0)

            return result

        else:
            temp = 1
            for i in range(len(digits) - 1, -1, -1):
                if temp == 1:
                    digits[i] += 1
                    temp = int(digits[i] / 10)
                    digits[i] = digits[i] % 10
                else:
                    break
            return digits