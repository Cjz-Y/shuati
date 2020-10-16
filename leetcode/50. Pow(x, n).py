class Solution:
    def myPow(self, x: float, n: int) -> float:

        def func(N):
            ans = 1.0
            temp_x = x
            while N > 0:
                if N % 2 == 1:
                    ans *= temp_x
                temp_x *= temp_x
                N //= 2
            return ans
        
        return func(n) if n >= 0 else 1.0 / func(-n)

        return temp if n >= 0 else 1.0 / temp
