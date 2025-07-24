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
print("Welcome to Smart Calculator with Power Support")

num1 = float(input("Enter first number: "))
op1 = input("Enter first operator (+, -, *, /, **): ")
num2 = float(input("Enter second number: "))
op2 = input("Enter second operator (+, -, *, /, **): ")
num3 = float(input("Enter third number: "))

# === LOGIC ===
if precedence(op2) > precedence(op1):
    # Evaluate num2 op2 num3 first
    part = evaluate(num2, op2, num3)
    result = evaluate(num1, op1, part)
else:
    # Evaluate num1 op1 num2 first
    part = evaluate(num1, op1, num2)
    result = evaluate(part, op2, num3)

print("Result:", result)
