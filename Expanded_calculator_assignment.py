# This code implements a simple calculator that can handle addition, subtraction, multiplication, division, and exponentiation (power) operations. 
# It evaluates expressions based on operator precedence (to model the BODMAS Rules).

# This function evaluates a simple expression with two numbers and an operator.
def evaluate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '**':
        return a ** b
    else:
        return None

# This function determines the precedence of operators.(To implement BODMAS rules)
def precedence(op):
    if op == '**':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    else:
        return 0

# === INPUT ===
# This section takes user input for the calculator operations.
print("Welcome to Smart Calculator with Power Support")

num1 = float(input("Enter first number: "))
op1 = input("Enter first operator (+, -, *, /, **): ")
num2 = float(input("Enter second number: "))
op2 = input("Enter second operator (+, -, *, /, **): ")
num3 = float(input("Enter third number: "))

# === LOGIC ===
# This section calculates the expression based on operator precedence.
if precedence(op2) > precedence(op1):
    # Evaluate num2 op2 num3 first
    part = evaluate(num2, op2, num3)
    result = evaluate(num1, op1, part)
else:
    # Evaluate num1 op1 num2 first
    part = evaluate(num1, op1, num2)
    result = evaluate(part, op2, num3)

print("Result:", result)
