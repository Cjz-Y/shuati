class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = numRows * 2 - 2

        m = (len(s) // n) + 1 if len(s) % n != 0 else len(s) // n

        array = []
        for i in range(m):
            start = n * i
            array.append(s[start:start + n])

        ans = ""
        for i in range(len(array)):
            ans += array[i][0]

        begin_index = 1
        end_index = n - 1
        while begin_index <= end_index:
            for i in range(len(array)):
                if begin_index < len(array[i]):
                    ans += array[i][begin_index]
                if end_index < len(array[i]) and end_index != begin_index:
                    ans += array[i][end_index]
            begin_index += 1
            end_index -= 1

        return ans