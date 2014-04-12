# L-15 MCS 507 Mon 30 Sep 2013 : oo model for 4-bar mechanism

"""
The main program to test the class prompts the user for n,
a number of angles, and then prints the coordinates for the
five joints that define the mechanism.
"""

from math import cos, sin, pi, sqrt

class FourBar(object):
    """
    A 4-bar mechanism is determined by five parameters:
    (1) a : the length of the horizontal bar,
    (2) L : the length of the crank,
    (3) R : the length of the bar attached to the crank,
    (4) r : the length of the bar to the right,
    (5) b : the length of the bar to the coupler.
    The mechanism is driven by a crank, with angle t,
    and we use c = cos(t) and s = sin(t).
    The value of t determines the state of the mechanism.
    """

    def __init__(self, a=100, L=50, R=125, r=125, b=125, t=pi/2):
        """
        Initializes a 4-bar mechanism with the 5 given lengths
        and sets the state of the 4-bar to the angle t.
        Default values are for the Chebyshev mechanism.
        """
        self.flat = a    # (0,a) is joint
        self.crank = L   # length of the crank
        self.top = R     # length of bar attached to crank
        self.right = r   # length of the right bar
        self.coupler = b # length of bar to the coupler
        self.angle = t   # state of the 4-bar

    def z1(self):
        """
        Returns the value of L^2+a^2-2*a*L*c.
        """
        a = self.flat
        L = self.crank
        c = cos(self.angle)
        v = L**2 + a**2 - 2.0*a*L*c
        return v

    def z2(self):
        """
        Returns the value of -L*R^2*s+L^3*s+L*s*r^2+a^2*L*s-2*L^2*s*c*a.
        """
        a = self.flat
        L = self.crank
        R = self.top
        r = self.right
        c = cos(self.angle)
        s = sin(self.angle)
        v = -L*R**2*s+L**3*s+L*s*r**2+a**2*L*s-2*L**2*s*c*a
        return v

    def z3(self):
        """
        Returns the value of the square root of the discriminant:
           sqrt(-2*L^2*R^2*s^2*a^2-2*L^2*R^2*s^2*r^2+2*a^4*R^2-a^2*r^4
             +L^6*s^2-L^2*R^4+2*L^4*R^2+2*L^4*r^2-L^2*r^4-7*L^4*a^2
             -7*L^2*a^4-L^6-a^6+6*L^4*s^2*a^2+4*L^3*R^2*s^2*c*a
             -4*L^5*s^2*c*a-2*L^2*s^2*r^2*a^2-2*L^4*R^2*s^2+L^2*s^2*r^4
             +5*a^4*L^2*s^2+2*L^2*r^2*R^2+6*L^5*a*c+4*L^2*a^2*R^2
             +4*L^2*r^2*a^2+20*L^3*c*a^3+2*a^2*r^2*R^2+4*L^3*s^2*r^2*c*a
             -12*a^3*L^3*s^2*c+4*L^4*s^2*c^2*a^2-8*L^3*a*R^2*c-8*L^3*a*r^2*c
             -8*a^3*R^2*L*c-8*a^3*r^2*L*c-a^2*R^4+2*a^4*r^2+6*a^5*L*c
             -8*a^2*L^4*c^2-8*a^4*L^2*c^2+2*a*L*c*R^4+2*a*L*c*r^4
             +8*a^2*L^2*c^2*R^2+8*a^2*L^2*c^2*r^2-2*L^4*s^2*r^2
             +L^2*R^4*s^2-4*a*L*c*r^2*R^2)
        If the argument of the sqrt is negative, zero is returned.
        """
        a = self.flat
        L = self.crank
        c = cos(self.angle)
        s = sin(self.angle)
        R = self.top
        r = self.right
        v = -2.0*L**2*R**2*s**2*a**2-2*L**2*R**2*s**2*r**2+2*a**4*R**2 \
            -a**2*r**4+L**6*s**2-L**2*R**4+2*L**4*R**2+2*L**4*r**2-L**2*r**4 \
            -7*L**4*a**2-7*L**2*a**4-L**6-a**6+6*L**4*s**2*a**2 \
            +4*L**3*R**2*s**2*c*a-4*L**5*s**2*c*a-2*L**2*s**2*r**2*a**2 \
            -2*L**4*R**2*s**2+L**2*s**2*r**4 +5*a**4*L**2*s**2 \
            +2*L**2*r**2*R**2+6*L**5*a*c+4*L**2*a**2*R**2 \
            +4*L**2*r**2*a**2+20*L**3*c*a**3+2*a**2*r**2*R**2 \
            +4*L**3*s**2*r**2*c*a-12*a**3*L**3*s**2*c+4*L**4*s**2*c**2*a**2 \
            -8*L**3*a*R**2*c-8*L**3*a*r**2*c-8*a**3*R**2*L*c-8*a**3*r**2*L*c \
            -a**2*R**4+2*a**4*r**2+6*a**5*L*c-8*a**2*L**4*c**2 \
            -8*a**4*L**2*c**2+2*a*L*c*R**4+2*a*L*c*r**4 \
            +8*a**2*L**2*c**2*R**2+8*a**2*L**2*c**2*r**2-2*L**4*s**2*r**2 \
            +L**2*R**4*s**2-4*a*L*c*r**2*R**2
        if v < 0:
            return 0
        else:
            return sqrt(v)

    def y1p(self):
        """
        Returns the value of (1/2)*(z2+z3)/z1.
        """
        v = (self.z2()+self.z3())/(2*self.z1())
        return v

    def y1m(self):
        """
        Returns the value of (1/2)*(z2-z3)/z1.
        """
        v = (self.z2()-self.z3())/(2*self.z1())
        return v

    def x(self, y):
        """
        Returns the value of (1/2)*(-a^2+r^2+L^2-R^2-2*y*L*s)/(-a+L*c).
        """
        a = self.flat
        L = self.crank
        c = cos(self.angle)
        s = sin(self.angle)
        R = self.top
        r = self.right
        x_den = 2*(-a+L*c)
        x_num = -a**2+r**2+L**2-R**2-2*y*L*s
        v = x_num/x_den
        return v

    def connector_point(self):
        """
        Returns coordinates of connector point.
        For complex values (0, 0) is returned.
        """
        try:
            y1pv = self.y1p()
            x1pv = self.x(y1pv)
            return (x1pv, y1pv)
        except:
            return (0, 0)

    def coupler_point(self):
        """
        Returns the coordinates of the coupler point.
        """
        t = self.angle
        L = self.crank
        ax = L*cos(t)
        ay = L*sin(t)
        p = self.connector_point()
        dx = p[0] - ax
        dy = p[1] - ay
        b = self.coupler
        if dx == 0:
            x = ax
            y = p[1] + b
        else:
            v = sqrt(dx*dx + dy*dy)
            x = p[0] + b*dx/v
            y = p[1] + b*dy/v
        return (x, y)

    def joints(self):
        """
        Returns the list of the coordinates of the
        five joints that define the mechanism.
        """
        L = [(0, 0), (self.flat, 0)]
        t = self.angle
        L.append((self.crank*cos(t), self.crank*sin(t)))
        L.append(self.connector_point())
        L.append(self.coupler_point())
        return L

    def print_joints(self):
        """
        Prints the coordinates for the joints.
        """
        L = self.joints()
        s = "%.2f " % self.angle
        for p in L:
            s = s + "(%5.1f, %5.1f)" % p
        print(s)

    def track_path(self):
        """
        Computes coordinates of points along a path
        tracked by the coupler point.
        """
        n = input('give number of samples = ')
        h = 2*pi/int(n)
        for i in range(0, n):
            self.print_joints()
            self.angle = self.angle + h
            if self.angle > 2*pi:
                self.angle = self.angle - 2*pi

def main():
    """
    Evaluates the formulas for the coupler of the 4-bar mechanism
    for values corresponding to the Chebyshev mechanism.
    """
    fbr = FourBar()
    fbr.track_path()

if __name__ == "__main__":
    main()