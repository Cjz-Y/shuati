class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0 for i in range(len(num1) + len(num2) + 1)]
        n1 = len(num1)
        n2 = len(num2)

        for ii in range(n1 - 1, -1 , -1):
            i = n1 - ii
            for jj in range(n2 - 1, -1, -1):
                j = n2 - jj

                target = i + j - 1
                result[target] += int(num1[ii]) * int(num2[jj])

                result[target + 1] += int(result[target] / 10)
                result[target] = result[target] % 10

        ans = ''
        for i in range(len(result) - 1, 0, -1):
            if ans != '':
                ans += str(result[i])
            elif result[i] != 0 or i == 1:
                ans += str(result[i])

        return ans

        return ''.join(list(reversed(result)))

