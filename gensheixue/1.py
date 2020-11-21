import sys
import heapq

m, n = map(int, sys.stdin.readline().strip().split())
mission = list(map(int, sys.stdin.readline().strip().split()))

mission.sort(reverse=True)

machine = [0 for i in range(m)]
ans = -1

for mission_time in mission:
    # print(machine)
    a = heapq.heappop(machine)
    a += mission_time
    ans = max(ans, a)
    heapq.heappush(machine, a)

# print(machine)

print(ans)

