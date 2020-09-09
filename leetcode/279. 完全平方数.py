class Solution:
    def numSquares(self, n: int) -> int:

        bag = []
        temp = 1

        index = 1
        while temp < n:
            bag.append(temp)
            index += 1
            temp = index * index

        null = 999999
        f = [null for i in range(n + 1)]
        f[0] = 0

        for i in range(n + 1):
            if f[i] != null:
                for value in bag:
                    if i + value <= n:
                        f[i + value] = min(f[i + value], f[i] + 1)

        return f[n]