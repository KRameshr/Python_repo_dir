class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}, Age: {self.age}"

emp1 = Employee("Ramesh", 50000, 30)
print(emp1)

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def execute_command(self, command, num1, num2):
        if command == 'add':
            return self.add(num1, num2)
        elif command == 'sub':
            return self.sub(num1, num2)
        elif command == 'mul':
            return self.mul(num1, num2)
        elif command == 'div':
            return self.div(num1, num2)
        else:
            return "Invalid Command"


calc = Calculator()
print(calc.execute_command('add', 10, 5)) 
print(calc.execute_command('mul', 4, 3))   
print(calc.execute_command('div', 10, 0))