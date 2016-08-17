import random

class RandomPoint:
    """A random point that will lie within a square of side length 2*radius"""

    # Sets the radius of the circle that lies within the square. Then create
    # a randomely positioned point that lies within the square.
    def __init__(self, radius):
        assert (radius > 0)
        self.radius = radius
        self.x = random.randrange(-radius, radius)
        self.y = random.randrange(-radius, radius)

    # Determines if the point lies within the inner circle.
    def PointLiesInCircle(self):
        return (pow(self.x, 2) + pow(self.y, 2) <= pow(self.radius, 2))

    def DataPoints(self):
        return [self.x, self.y]