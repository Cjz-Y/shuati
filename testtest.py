used = set()

a = set()
a.add(1)
a.add(2)
d = list(a)
d.sort()


used.add(a)

b = set()
b.add(2)
b.add(1)

print(b in used)