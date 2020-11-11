class Solution:
    def isNumber(self, s: str) -> bool:
        state = [
            {' ': 0, 'sign': 1, 'digit': 2, '.': 4},  # 状态0，空状态
            {'digit': 2, '.': 4},  # 状态1，e之前的符号位
            {'digit': 2, '.': 3, 'e': 5, ' ': 8},  # 状态2，小数点之前的数字
            {'digit': 3, 'e': 5, ' ': 8},  # 状态3，小数点之后的数字
            {'digit': 3},  # 状态4，小数点前为空，直接从状态1和状态0转移过来的
            {'sign': 6, 'digit': 7},  # 状态5，自然数符号e
            {'digit': 7},  # 状态6，e之后的符号位
            {'digit': 7, ' ': 8},  # 状态7，符号之后的数字
            {' ': 8}  # 状态8，结尾状态
        ]
        current_state = 0

        for char in s:
            if '0' <= char <= '9':
                transfer = 'digit'
            elif char in ' .':
                transfer = char
            elif char in 'eE':
                transfer = 'e'
            elif char in '+-':
                transfer = 'sign'
            else:
                transfer = char
            # print(char, transfer, state[current_state].get(transfer, None))
            current_state = state[current_state].get(transfer, -1)
            if current_state == -1:
                return False

        return current_state in [2, 3, 7, 8]
