# sum.py
# Allow     sum(n) to add [1, 2, 3, ... n]
#	or	sum(a, n) to add [a, a+1, ..., n]
def sum(*args):
    if len(args) == 1:
        start = 1
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]
    s = 0
    for x in range(start, stop+1):
        s += x
    return s

print(sum(10))
print(sum(3, 4))