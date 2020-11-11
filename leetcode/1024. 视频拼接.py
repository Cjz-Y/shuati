from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        def better(a, b):
            return a[0] > b[0] or (a[0] == b[0] and (a[1] >= b[1]))

        def qsort(head, tail, data):
            if head < tail:
                i, j = head, tail
                temp = data[head]
                while i < j:
                    while i < j and better(data[j], temp):  j -= 1
                    data[i] = data[j]
                    while i < j and better(temp, data[i]):  i += 1
                    data[j] = data[i]
                data[i] = temp

                qsort(head, i - 1, data)
                qsort(i + 1, tail, data)

        qsort(0, len(clips) - 1, clips)

        print(clips)
        stack = []

        for clip in clips:
            if not stack:
                stack.append(clip)
            else:
                if clip[0] > stack[-1][1]:
                    break
                elif clip[0] >= stack[-1][0] and clip[1] <= stack[-1][1]:
                    continue
                elif clip[0] == stack[-1][0] and clip[1] > stack[-1][1]:
                    stack.pop()
                    stack.append(clip)
                else:
                    while len(stack) >= 2 and stack[-2][1] >= clip[0] and clip[1] >= stack[-1][1]:
                        stack.pop()
                    stack.append(clip)

            if stack[-1][1] >= T:
                break



        if stack[0][0] == 0 and stack[-1][1] >= T:
            print(stack)
            return len(stack)
        else:
            return -1
