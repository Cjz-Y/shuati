class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p

        f = [[False] * len(s) for i in range(len(p))]

        f[0][0] = True


        for i in range(1, len(p)):
            if p[i] == "*":
                f[i][0] = True
            else:
                break

        last_round_first_true = 0
        for i in range(1, len(p)):
            if f[i][0]:
                current_round_first_true = 0
            else:
                current_round_first_true = -1

            for j in range(1, len(s)):
                if p[i] == s[j] or p[i] == '?':
                    if f[i - 1][j - 1]:
                        f[i][j] = True
                elif p[i] == '*':
                    if last_round_first_true != -1 and j > last_round_first_true:
                        f[i][j] = True
                    elif f[i - 1][j]:
                        f[i][j] = True
                if f[i][j] and current_round_first_true == -1:
                    current_round_first_true = j

            last_round_first_true = current_round_first_true

        for i in range(len(p)):
            print(f[i])

        return f[len(p) - 1][len(s) - 1]

if __name__ == '__main__':
    s = "a"
    p = "a*"

    print(Solution().isMatch(s, p))
