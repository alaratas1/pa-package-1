from .point import Point

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2) ** 0.5

    def perpendicular_distance(self, point):
        x0 = point.x
        y0 = point.y

        x1 = self.p1.x
        y1 = self.p1.y

        x2 = self.p2.x
        y2 = self.p2.y

        numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)

        denominator = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5

        return numerator / denominator
    
    def __str__(self):
        return f"Line({self.p1}, {self.p2})"
