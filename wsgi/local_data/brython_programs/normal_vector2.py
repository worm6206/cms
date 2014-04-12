import math

# normal vector of a plane

def mag(V):
  return math.sqrt(sum([x*x for x in V]))
def n(V):
  v_m = mag(V)
  return [ vi/v_m for vi in V]
  
N = [5, 2, 3]
print(mag(N))
print(n(N))