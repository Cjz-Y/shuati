while True:
    n = int(input())

    f = 1
    index = 1
    time = 1
    while True:
        f += index
        time += index
        if time >= n:
            print(f - (time - n))
            break
        f -= 1
        time += 1
        if time == n:
            print(f)
            break
        index += 1

    # print(f)

