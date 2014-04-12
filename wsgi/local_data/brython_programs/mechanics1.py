from math import sqrt, pow

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def Length(self):
        L = sqrt(pow(self.p1.x - self.p2.x,2) + \
                 pow(self.p1.y - self.p2.y,2))
        return L


    def dc(self):
        L = self.Length()
        prj = self.p2 - self.p1
        return prj / L


def main():
    p1 = Point(0.0, 0.0)
    p2 = Point(3.0, 4.0)
    L1 = Line(p1, p2)
    print("Length of line =", L1.Length())

if __name__ == '__main__':
    main()