class Calculator:

    counter = 0

    def __init__(self, x=0, y=0):
        self.first_num = x
        self.y = y

        Calculator.counter += 1

print("counter = ", Calculator.counter)
calc1 = Calculator(1,1)
calc2 = Calculator(11,112)
calc3 = Calculator(12,11)
print("counter = ", Calculator.counter)
Calculator.counter = 100
print("counter = ", Calculator.counter)
