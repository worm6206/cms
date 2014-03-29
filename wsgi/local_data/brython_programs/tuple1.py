d = (11,12,13,'asdf',14,15.0)
# Note - tuples are immutable types
# Common operations: 
# length of a typle
print(len(d))
# indexation (in Python it starts from zero)
print(d[0], d[1])
# slicing
print(d[0:2]) # equals to (11, 12)
print(d[2:-1]) # equals to (13, 'asdf', 14)
print(d[:2]) # same as d[0:2], equals to (11, 12)
print(d[3:]) # equals to ('asdf', 14, 15.0)
# contains
print((15 in d, 100 in d)) # returns (True, False)