class Pixel:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return '<Pixel r:%s g:%s b:%s>' % (self.r, self.g, self.b)