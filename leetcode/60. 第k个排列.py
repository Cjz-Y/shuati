class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f = [1, 1]
        for i in range(2, n):
            f.append(f[i - 1] * i)

        # print(f)

        hold = [i + 1 for i in range(n)]
        # print(hold)

        k -= 1
        index = 1
        ans = []
        while index <= n:
            temp = k // f[n - index]
            ans.append(str(hold[temp]))
            hold.remove(hold[temp])
            k -= f[n - index] * temp
            # print('temp = %d' % temp)
            # print('hold = %s' % hold)
            # print('ans = %s' % ans)
            index += 1
        return ''.join(ans)

if __name__ == '__main__':
    n = 4
    k = 2

    print(Solution().getPermutation(n, k))

