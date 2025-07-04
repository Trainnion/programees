

def modulo():
    print("This program calculates the modulo of two decimal numbers.")
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    if number2 == 0:
        print("Cannot divide by zero.")
        return
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")

if __name__ == "__main__":
    modulo()
