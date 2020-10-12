class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        pa = [[False] * len(a) for i in range(len(a))]
        pb = [[False] * len(b) for i in range(len(b))]

        for i in range(len(a)):
            pa[i][i] = True
            pb[i][i] = True
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                pa[i - 1][i] = True
            if b[i] == b[i - 1]:
                pb[i - 1][i] = True

        last_temp = True
        for length in range(3, len(a) + 1):
            temp = False
            for start in range(len(a) - length + 1):
                end = start + length - 1
                pa[start][end] = pa[start + 1][end - 1] and a[start] == a[end]
                pb[start][end] = pb[start + 1][end - 1] and b[start] == b[end]
                # print(pa[start][end], pb[start][end])
                temp = temp or (pa[start][end] or pb[start][end])

            if not temp and not last_temp:
                # print(length)
                break
            last_temp = temp

        # print(pa)
        # print(pb[5][16])

        if pa[0][len(a) - 1] or pb[0][len(b) - 1]:
            return True
        else:
            for i in range(len(a) // 2):
                right = len(a) - i - 1
                # print(i, right)
                if a[i] != b[right]:
                    break
                if i == right or right - i == 1:
                    return True
                if pb[i + 1][right - 1]:
                    return True

                if pa[i + 1][right - 1]:
                    return True

            for i in range(len(a) // 2):
                right = len(a) - i - 1
                # print(i, right)
                if b[i] != a[right]:
                    break
                if i == right or right - i == 1:
                    return True
                if pa[i + 1][right - 1]:
                    return True

                if pb[i + 1][right - 1]:
                    return True

            return False

