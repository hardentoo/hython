def f():
    if True:
        print("f()")
        return 0
        print("Shouldn't see this")

    print("Hello")

def g():
    print("Goodbye")

def h():
    a = f() + 1
    print("about to leave h()")
    return a

def i():
    pass

def j():
    a = 5
    while a != 0:
        print(a)
        if a == 2:
            return 42
        print("after")
        a = a - 1

def k():
    if True:
        return
    return 1

print(f())
print(g())
print(h())
print(i())
print(j())
print(k())