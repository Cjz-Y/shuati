n = int(input())
m = int(input())
if n == 0:
    print(0)
elif m == 0:
    print(0)
else:
    # print('yes')
    global ans
    ans = 0


    def search(index, temp_sum, temp_num):
        # print('a')
        global ans
        if temp_sum == n:
            # print(result)
            ans += 1
            return
        if temp_num >= m:
            return

        for i in range(index, n + 1):
            if i + temp_sum <= n:
                # result.append(i)
                search(i, temp_sum + i, temp_num + 1)
                # result.pop()
            else:
                break


    search(1, 0, 0)
    print(ans)




