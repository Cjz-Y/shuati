class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def move(s):
            result = []
            index = s.find('0')

            l = list(s)

            if index < 3:
                l[index], l[index + 3] = l[index + 3], l[index]
                result.append(''.join(l))
                l[index], l[index + 3] = l[index + 3], l[index]
            else:
                l[index], l[index - 3] = l[index - 3], l[index]
                result.append(''.join(l))
                l[index], l[index - 3] = l[index - 3], l[index]

            if index == 0 or index == 3 or index == 4 or index == 1:
                l[index], l[index + 1] = l[index + 1], l[index]
                result.append(''.join(l))
                l[index], l[index + 1] = l[index + 1], l[index]
            if index == 2 or index == 5 or index == 1 or index == 4:
                l[index], l[index - 1] = l[index - 1], l[index]
                result.append(''.join(l))
                l[index], l[index - 1] = l[index - 1], l[index]
            return result


        use = set()
        start = ''
        # [[start + str(i) for i in range(len(board_item))] for board_item in board]
        for arr in board:
            for item in arr:
                start += item

        print(start)

        if start == '123450':
            return 0

        use.add(start)
        cur = [start]
        step = 1
        flag = False
        while cur:
            next = []
            for current in cur:
                for create_item in move(current):
                    if create_item not in use:
                        use.add(create_item)
                        next.append(create_item)
                        if create_item == '123450':
                            flag = True
                            break
                if flag:
                    break
            cur = next
            step += 1

        if flag:
            return step
        else:
            return -1



