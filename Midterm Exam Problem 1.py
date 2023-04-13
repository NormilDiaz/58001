class Circle:
    def __init__(self, num):
        self.num = float(input("Enter the desired radius: "))

    def area(self):
        return 3.141592653589793 * self.num * self.num

    def perimeter(self):
        return 2 * 3.141592653589793 * self.num

    def Display(self):
        print('The Area of the Circle is', self.area(), 'and the Perimeter of the Circle is', + self.perimeter())


shape = Circle('num')
shape.Display()