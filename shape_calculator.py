class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if type(self).__name__ == 'Square':
            str1 = '{}(side={})'.format(type(self).__name__, self.width, self.height)
        else:
            str1 = '{}(width={}, height={})'.format(type(self).__name__, self.width, self.height)
        return str1

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal_length = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal_length

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pic = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append("*")
            pic.append("".join(row))
        pic_str = "\n".join(pic) + "\n"
        return pic_str

    def get_amount_inside(self, shape):
        num_times = self.get_area() // shape.get_area()
        return num_times


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_diagonal())
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_perimeter())
print(sq.get_diagonal())
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

