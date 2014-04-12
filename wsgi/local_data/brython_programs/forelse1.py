from random import randrange
n = 5
foo = [randrange(10) for i in range(n)]

for i in foo:
    if i == 0:
        print('found 1')
else:
    print('did not find 1')