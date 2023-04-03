class DistanceConversion:
    def __init__(self, num):
        self.num = float(input("Enter the desired meter: "))

    def MeterToCentimeter(self):
        return self.num * 100

    def MeterToKilometer(self):
        return self.num / 1000

    def MeterToInches(self):
        return self.num * 39.7

    def display(self):
        print('The Conversion of meter to centimeter is:', self.MeterToCentimeter(), 'and The Conversion of meter to klometer is:', + self.MeterToKilometer(), 'and The Conversion of meter to inches is:', + self.MeterToInches())


conv = DistanceConversion('num')
conv.display()