
# https://www.cnblogs.com/egust/p/4580299.html

def longestPalindrome(s):
    t = ['#']
    for ss in s:
        t.append(ss)
        t.append('#')

    center, right, size = 1, 2, len(t)
    p = [0, 1] + [None] * (size - 2)

    for i in range(2, size):
        mirror = center - (i - center)
        if i < right and i + p[mirror] < right:
            p[i] = p[mirror]
            continue

        count = min(size - i - 1, i)
        for length in range(1 if i > right else right - i + 1, count + 1):
            if t[i + length] != t[i - length]:
                count = length - 1
                break

        center = i
        r = i + count
        p[i] = count

    print(''.join(t))
    p = [str(i) for i in p]
    print(''.join(p))


s = 'abc'
longestPalindrome(s)
# print(3//2)