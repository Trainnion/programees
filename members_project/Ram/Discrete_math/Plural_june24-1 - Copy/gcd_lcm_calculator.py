import os

def gcd(a, b):
    # Euclidean algorithm
    while b != 0:
        print(f"{a} = {b}({a // b}) + {a % b}")
        a, b = b, a % b
       
    return a

def lcm(a, b, gcd_value):
    # LCM using GCD
    return abs(a * b) // gcd_value
running = True

while(running):
    print()

    print("This program lets you input two integers and calculates its GCD and LCM")
    first_number = int(input("Input first number: "))
    second_number = int(input("Input Second number: "))

    GCD = gcd(first_number, second_number)
    LCM = lcm(first_number, second_number, GCD)
    print("GCD: ", GCD)
    print("LCM: ", LCM )
    
    
    run = input("\nStart again? [y/n]")
    if(run == "n" or run == "N"):
        running = False
        
os.system("cls")
print("Program Closed")