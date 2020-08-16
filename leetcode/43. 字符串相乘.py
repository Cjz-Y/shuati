class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0 for i in range(len(num1) + len(num2) + 2)]
        lena = len(num1) - 1
        lenb = len(num2) - 1
        for ii in range(lena, -1, -1):
            x = 0
            i = lena - ii + 1
            for jj in range(lenb, -1, -1):

                j = lenb - jj + 1
                ans[i + j - 1] = x + ans[i + j - 1] + int(num1[ii]) * int(num2[jj])
                x = int(ans[i + j - 1] / 10)
                ans[i + j - 1] %= 10
                print('i = %d, j = %d, ans[%d] = %d' % (i, j, (i + j -1), ans[i + j - 1]))
            ans[i + lenb + 1] = x


        result = ''
        for i in range(len(ans) - 1, 0, -1):
            if result != '':
                result += str(ans[i])
            elif ans[i] != 0 or i == 1:
                result += str(ans[i])

        return result


if __name__ == '__main__':
    b = "0"
    a = "0"

    solution = Solution()

    print(solution.multiply(a, b))