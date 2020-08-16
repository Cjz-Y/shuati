from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        result.append([1])
        for i in range(1, numRows):
            temp_array = []
            for j in range(i + 1):
                temp_int = 0
                if j - 1 >= 0:
                    temp_int += result[i - 1][j - 1]
                if j < i:
                    temp_int += result[i - 1][j]
                temp_array.append(temp_int)

            result.append(temp_array)

        return result
