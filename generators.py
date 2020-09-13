a = (x for x in range(1, 1000))

print(a)
for _ in range(10):
    print(next(a))