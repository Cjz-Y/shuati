import sys
from collections import Counter


while (True):
    n = map(int, sys.stdin.readline().strip())

    temp = list(map(int, sys.stdin.readline().strip().split()))

    temp.sort(reverse=True)

    use = [False for i in range(len(temp))]

    total = 0
    flag = True

    for i in range(len(temp)):
        if temp[i] == 1:
            if use[i]:
                continue
            else:
                flag = False
        can = False
        for j in range(i + 1, len(temp)):
            for k in range(j + 1, len(temp)):
                # print(use[j], use[k], temp[j]+temp[k])
                if not use[j] and not use[k] and temp[j] + temp[k] == temp[i] - 1:
                    use[j] = True
                    use[k] = True
                    total += 1
                    can = True
                    break
        if not can:
            flag = False
            break
    # print(use)
    if flag:
        print("YES")
    else:
        print("NO")




