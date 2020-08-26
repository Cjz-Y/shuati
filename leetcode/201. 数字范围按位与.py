class Solution:

    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        while m < n:
            n = n & (n - 1)
        return n

    def rangeBitwiseAnd_(self, m: int, n: int) -> int:
        if m == 0:
            return 0

        div = [2 << i for i in range(31)]
        m_index, n_index = -1, -1
        for i in range(len(div) - 1, -1, -1):
            if m_index == -1 and m >= div[i]:
                m_index = i
            if n_index == -1 and n >=div[i]:
                n_index = i
            if m_index != -1 and n_index != -1:
                break
        print(m_index, n_index)
        if n_index - m_index >= 2 or (n_index - m_index == 1 and m == div[m_index]):
            return 0
        else:
            if n_index - m_index == 1:
                return div[n_index]
            else:
                if m % 2 == 0:
                    ans = m
                    for i in range(m + 2, n + 1, 2):
                        ans &= i
                        if ans == 0:
                            return ans
                    return ans
                else:
                    ans = m
                    for i in range(m + 1, n + 1, 2):
                        ans &= i
                        if ans == 0:
                            return ans
                    return ans

if __name__ == '__main__':
    a = 600000000
    b = 2147483645

    solution = Solution()

    print(solution.rangeBitwiseAnd(a, b))