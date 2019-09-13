'''Example Square Root Functions'''

def newton_sqrt1(x):
    """Return the square root of x using Newton's Method."""
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

def lazy_sqrt(x):
    return x**0.5

def builtin_sqrt(x):
    from math import sqrt
    return sqrt(x)
