#Program-1.py

#Simple Calculator method
#Accepts two(a,b) double values and an type of operation string

#using class 

class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def calculate(self,operation):
        if operation == "addition":
            return self.a + self.b
        elif operation == "subtraction":
            return self.a - self.b
        elif operation == "multiplication":
            return self.a * self.b
        elif operation == "division":
            if self.b != 0:
                return self.a/self.b
            else:
                return "Error : b is a zero"
        else:
            return "Ivalid values"

if __name__ == "__main__":
    a = float(input("Enter the a value: "))
    b = float(input("Enter the b value: "))
    operation = input("Enter operation (addition, subtraction, multiplication, division): ").strip().lower()

    output = calculator(a,b)
    Answer = output.calculate(operation)
    print("Result: ",Answer)
