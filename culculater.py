def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter first number: "))

for symbol in operation:
    print(symbol)

symbol_operation = input("Enter the operation: ")
num2 = int(input("Enter second number: "))

answer = operation[symbol_operation](num1, num2)
print(answer)

choice = input(f"The answer is {answer}. Continue? yes or no: ")

if choice == "yes":
    num1 = answer
    symbol_operation = input("Enter the operation: ")
    num2 = int(input("Enter second number: "))
