class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
# methods
    def get_sum(self):
        return self.a + self.b
    def get_minus(self):
        return self.a - self.b
    def get_multiple(self):
        return self.a * self.b
    def get_division(self):
        return self.a / self.b

if __name__ == "__main__":
    myCalc = calculator(a=3,b=2)
    print(myCalc.get_multiple())