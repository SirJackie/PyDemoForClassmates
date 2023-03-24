def f(x):
    return x


def g(x):
    return -x


def h(x, y):
    return y(x)


print(f(0.5))
print(h(0.5, f))
