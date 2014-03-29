d = {1:1, 2.0:4.0, 3:9}
# other ways to define the dict:
d = dict(((1,1), (2,4.0), (3,9)))
d = dict([(1,1), (2,4.0), (3,9)])
d = dict((i, i ** 2) for i in (1,2,3)) # operation a ** b means a^b
print(d)
print((1 in d, 2 in d, 5 in d)) # returns (True, True, False)
print(d[1], d[3]) # returns (1, 9)
print(list(d.keys())) # returns 1, 2.0, 3
print(list(d.items())) # returns [(1, 1), (2, 4.0), (3, 9)]
d.update({4:16, 10:100}) # update a dict by another one
d[20] = 400 # set value 400 to key 20, add this key if it was absent
print(len(d)) # returns number of entries in the dict