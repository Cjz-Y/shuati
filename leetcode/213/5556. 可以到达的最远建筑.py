from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        unuse_bricks = bricks
        heap = []
        ans = 0
        barried = False

        for i in range(1, len(heights)):
            print(str(i) + ":")
            print(unuse_bricks)
            print(heap)
            if heights[i] > heights[i - 1]:
                diff = heights[i] - heights[i - 1]
                print('diff' + str(diff))
                # 能用梯子就用梯子
                if len(heap) < ladders:
                    heapq.heappush(heap, diff)
                    continue

                # 不能用梯子，就跟堆顶元素比较，如果比堆顶元素还要小的话，就用砖头，否则就换出来
                if len(heap) > 0 and diff > heap[0]:
                    unuse_bricks -= heap[0]
                    if unuse_bricks < 0:
                        barried = True
                        ans = i - 1
                        break

                    heapq.heappop(heap)
                    heapq.heappush(heap, diff)
                else:
                    unuse_bricks -= diff
                    if unuse_bricks < 0:
                        barried = True
                        ans = i - 1
                        break
        return ans if barried else len(heights) - 1

