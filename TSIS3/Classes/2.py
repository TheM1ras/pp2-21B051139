class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length ** 2

Asqr = Square(int(input()))
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area
