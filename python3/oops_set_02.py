class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")
    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number**.5}")
    def cube(self):
        print(f"The value of {self.number} cube {self.number**3}")

obj = Calculator(3)
obj.square()
obj.squareRoot()
obj.cube()