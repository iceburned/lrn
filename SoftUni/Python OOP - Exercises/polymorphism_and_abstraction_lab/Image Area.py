class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.get_area()

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __le__(self, other):
        return self.area <= other.area

    def __lt__(self, other):
        return self.area < other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area

