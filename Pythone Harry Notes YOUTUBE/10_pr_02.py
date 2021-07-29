class Calculator:
    def __init__(self, num):
        self.num = num
    def square(self):
        print(f"The value of {self.num} suqare is {self.num **2}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num **3}")
    def squareRoot(self):
        print(f"The value of {self.num} square root is {self.num **0.5 }")
    @staticmethod
    def greet():
        print("Hello")
a = Calculator(9)
a.square()
a.cube()
a.squareRoot()
a.greet()