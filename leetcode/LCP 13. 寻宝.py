from typing import List


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        null = 99999
        temp_x = [0, 1, 0, -1]
        temp_y = [1, 0, -1, 0]
        ans = null

        def back(state, current_m, step):
            """
            递归回溯状态
            :param state: 当前的状态，用二进制表示
            :param current_m: 当前所在机关
            :param step: 当前所花费的脚步
            :return:
            """

            if state == (1 << len(m)) - 1:
                nonlocal ans
                ans = min(ans, step + m_dist[(m[current_m][0], m[current_m][1])][-1])
                return

            for i in range(1, len(m)):
                temp = 1 << i
                # 判断i位置是否走过，没走过可以走走
                if state & temp == 0:
                    if step + m_btw[current_m][i] < f[state + temp][i]:
                        f[state + temp][i] = step + m_btw[current_m][i]
                        back(state + temp, i, step + m_btw[current_m][i])

        def search(x, y):
            """
            搜索每个机关跟石头和起终点之间的最短路
            :param x:
            :param y:
            :return:
            """
            dist = [[null] * len(maze[0]) for i in range(len(maze))]

            dist[x][y] = 0
            cur = [(x, y)]

            while cur:
                next = []
                for cur_x, cur_y in cur:
                    for j in range(4):
                        next_x = cur_x + temp_x[j]
                        next_y = cur_y + temp_y[j]
                        if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] != '#' and \
                                dist[cur_x][cur_y] + 1 < dist[next_x][next_y]:
                            next.append((next_x, next_y))
                            dist[next_x][next_y] = dist[cur_x][cur_y] + 1

                cur = next

            f = [null for i in range(len(stone_pos))]
            for i in range(len(stone_pos)):
                f[i] = dist[stone_pos[i][0]][stone_pos[i][1]]
            # print(f)
            return f

        stone_pos = []
        start_pos = (-1, -1)
        end_pos = (-1, -1)

        # 记录石头的位置和起始位置
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'O':
                    stone_pos.append((i, j))
                if maze[i][j] == 'S':
                    start_pos = (i, j)
                if maze[i][j] == 'T':
                    end_pos = (i, j)

        # 终点是石头 -> 机关到石头是不需要经过石头的
        stone_pos.append(end_pos)
        # 起点是机关 -> 起点到机关是需要经过石头的
        m = [start_pos]
        m_dist = {}
        m_dist[start_pos] = search(start_pos[0], start_pos[1])

        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'M':
                    m.append((i, j))
                    m_dist[(i, j)] = search(i, j)

        # 计算两个机关之间的最短距离
        # print(m)
        m_btw = [[null] * len(m) for i in range(len(m))]
        for i in range(len(m)):
            for j in range(i + 1, len(m)):
                # print(i, j, ":")
                for k in range(len(stone_pos) - 1):
                    if m_dist[m[i]][k] + m_dist[m[j]][k] < m_btw[i][j]:
                        # print(m_dist[m[i]][k] + m_dist[m[j]][k])
                        m_btw[i][j] = m_dist[m[i]][k] + m_dist[m[j]][k]
                        m_btw[j][i] = m_dist[m[i]][k] + m_dist[m[j]][k]

        # print(m_btw)
        f = [[null] * len(m) for i in range(1 << len(m))]

        # 初始状态 1 代表第0个机关已经走了（起点是第一个机关）
        f[1][0] = 0

        # 枚举状态
        for state in range(1, 1 << len(m)):
            # 枚举当前的节点
            for fromm in range(0, len(m)):
                if state & (1 << fromm) != 0:
                    # 枚举到达的节点
                    for to in range(1, len(m)):
                        # print()
                        if state & (1 << to) == 0:
                            f[state | (1 << to)][to] = min(f[state][fromm] + m_btw[fromm][to], f[state | (1 << to)][to])
                            # print(state, to, state | (1 << to), f[state | (1 << to)][to])

        for i in range(0, len(m)):
            ans = min(ans, f[(1 << len(m)) - 1][i] + m_dist[(m[i][0], m[i][1])][-1])

        # back(1, 0, 0)

        return ans if ans != null else -1





