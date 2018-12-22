from Shapes.circle import Circle
from Shapes.calc import AddTwoNumbers,MultiplyTwoNumbers

circ = Circle(5)
print(circ.calculateArea())

a = 5
b = 10

print(f'addition of {a} and {b} is {AddTwoNumbers(a,b)}')
print(f'Multiplication of {a} and {b} is {MultiplyTwoNumbers(a,b)}')
