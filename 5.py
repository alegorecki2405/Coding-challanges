# Good morning! Here's your coding interview problem for today.
# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair)
# returns the first and last element of that pair. For example,
# car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns
# 4.
def cons(a, b):

    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
            return b
    return f(right)


print(car(cons(1,2)))
print(cdr(cons(1,2)))