from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [99999 for i in range(amount + 1)]
        f[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    f[i] = min(f[i], f[i - coin] + 1)


        if f[amount] == 99999:
            return -1
        else:
            return f[amount]
