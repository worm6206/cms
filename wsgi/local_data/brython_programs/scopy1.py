'''
# scope0.py
def f(n):
    x = 3
    return x**n

print(f(4))
print("還有")
print(x)

# scope1.py
x = 3
def f(n):
    return x**n

print(f(4))
print(x)
'''
'''
# scope2.py
# UnboundLocalError: local variable 'x' referenced before assignment
x = 3
def f(n):
    x += 1
    return x**n

print(f(4))
print(x)
'''

# scope3.py
x = 3
def f(n):
    global x
    x += 1
    return x**n

print(f(4))
print(x)