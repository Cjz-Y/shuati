class Solution:
    def countVowelStrings(self, n: int) -> int:
        cur_a, cur_e, cur_i, cur_o, cur_u = 1, 1, 1, 1, 1
        next_a, next_e, next_i, next_o, next_u = 1, 1, 1, 1, 1
        for i in range(1, n + 1):
            next_a = cur_a
            next_e = cur_a + cur_e
            next_i = cur_a + cur_e + cur_i
            next_o = cur_a + cur_e + cur_i + cur_o
            next_u = cur_a + cur_e + cur_i + cur_o + cur_u

            cur_a, cur_e, cur_i, cur_o, cur_u = next_a, next_e, next_i, next_o, next_u
        return cur_a + cur_e + cur_i + cur_o + cur_u

