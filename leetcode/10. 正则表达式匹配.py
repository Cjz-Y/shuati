class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p

        g = []
        index = 0
        pl = list(p)
        while index < len(pl):
            if index + 1 < len(pl) and pl[index + 1] == '*':
                g.append(True)
                del pl[index + 1]
            else:
                g.append(False)
            index += 1

        p = ''.join(pl)

        f = [[False] * len(s) for i in range(len(p))]

        f[0][0] = True

        for i in range(1, len(p)):
            if g[i] and f[i - 1][0]:
                f[i][0] = True
            else:
                break

        for i in range(1, len(p)):

            for j in range(1, len(s)):
                if p[i] == s[j] and f[i - 1][j - 1]:
                    f[i][j] = True
                elif p[i] == s[j] and g[i] and f[i][j - 1]:
                    f[i][j] = True
                elif p[i] == '.' and f[i - 1][j - 1]:
                    f[i][j] = True
                elif p[i] == '.' and g[i] and f[i][j - 1]:
                    f[i][j] = True
                elif g[i] and f[i - 1][j]:
                    f[i][j] = True

        print(s)
        print(p)
        for i in range(len(p)):
            print(f[i])

        return f[len(p) - 1][len(s) - 1]

if __name__ == '__main__':
    s = 'mississippi'
    p = 'mis*is*p*.'

    print(Solution().isMatch(s, p))