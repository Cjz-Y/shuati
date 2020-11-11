class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        def handleState(char, num, state):
            result = []
            for i in range(len(hand)):
                if hand[i] == char and (1 << i) & state == 0:
                    result.append(i)
                if len(result) == num:
                    break
            return result if len(result) == num else []

        def erease(s):
            start = 0
            num = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    num += 1
                else:
                    if num >= 3:
                        return erease(s[:start] + s[start + num:])
                    start = i
                    num = 1
            if num >= 3:
                return erease(s[:start] + s[start + num:])
            return s

        def one_count(num):
            result = 0
            while num != 0:
                num = num & (num - 1)
                result += 1
            return result

        max_value = 999999
        ans = max_value
        cur = [(board, 0)]

        use = set()
        use.add((board, 0))

        while cur:
            next = []

            for current_str, current_state in cur:
                if one_count(current_state) >= ans: continue
                # print("current_str: " + current_str)
                start = 0
                index = 0
                while index < len(current_str):
                    while index + 1 < len(current_str) and current_str[index] == current_str[index + 1]:
                        index += 1

                    if index - start + 1 == 2:
                        use_color = set()
                        for i in range(len(hand)):
                            if hand[i] != current_str[index] and hand[i] not in use_color and current_state & (
                                    1 << i) == 0:
                                new_str = current_str[:start + 1] + hand[i] + current_str[index:]
                                new_state = current_state | (1 << i)
                                # print(new_str, new_state)
                                use_color.add(hand[i])
                                if (new_str, new_state) not in use:
                                    use.add((new_str, new_state))
                                    next.append((new_str, new_state))

                    result = handleState(current_str[index], 3 - (index - start + 1), current_state)
                    if result:
                        new_str = erease(current_str[:start] + current_str[index + 1:])
                        new_state = current_state
                        for num in result:
                            new_state = new_state | (1 << num)
                        # print(new_str, new_state)
                        if new_str == "":
                            ans = min(ans, one_count(new_state))
                        else:
                            if (new_str, new_state) not in use:
                                use.add((new_str, new_state))
                                next.append((new_str, new_state))
                    index += 1
                    start = index
            cur = next
        return ans if ans != max_value else -1



