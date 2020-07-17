class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, size):
        self.width = size

    def set_height(self, size):
        self.height = size

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        chart = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(0, self.height):
            for j in range(0, self.width):
                chart += '*'
            chart += '\n'
        return chart

    def get_amount_inside(self, shape):
        in_width = self.width / shape.width
        in_height = self.height / shape.height

        return int(in_width * in_height)

    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'


class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length

    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self, length):
        self.width = length
        self.height = length

    def set_height(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        return 'Square(side='+str(self.width)+')'
