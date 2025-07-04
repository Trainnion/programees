import os
print()


number_bases = [ "Binary", "Decimal", "Octal", "Hexadecimal"]
running = True

while(running):
    print("This Program takes a number be it Binary, Decimal, Octal & Hexadecimal \nand converts it unto the other three number bases \n1. Binary \n2. Decimal \n3. Octal \n4. Hexadecimal ")
    x = input("Choose a number base: ")
    unconverted_number= input(number_bases[int(x)  - 1] + " number: ")

    match x:
        case "1":
            original_unconverted_number = unconverted_number
            based_unconverted_number = "0b" + unconverted_number
            
            convertedTO_decimal = int(based_unconverted_number, 2)
            convertedTO_octal = oct(int(based_unconverted_number, 2))[2:]
            convertedTO_hexadecimal = hex(int(based_unconverted_number, 2))[2:].upper()
            
            print()
            print("Original: " + str(original_unconverted_number))
            print("Converted to Decimal: " + str(convertedTO_decimal))
            print("Converted to Octal: " + str(convertedTO_octal))
            print("Converted to Hexadecimal: " + str(convertedTO_hexadecimal))
            
        case "2":

            convertedTO_binary = bin(int(unconverted_number))[2:]
            convertedTO_octal = oct(int(unconverted_number))[2:]
            convertedTO_hexadecimal = hex(int(unconverted_number))[2:].upper()      
            print()
            print("Original: " + str(unconverted_number))
            print("Converted to Binary: " + str(convertedTO_binary))
            print("Converted to Octal: " + str(convertedTO_octal))
            print("Converted to Hexadecimal: " + str(convertedTO_hexadecimal))
            
            
        case "3":
            
            convertedTO_binary = bin(int(unconverted_number, 8))[2:]
            convertedTO_decimal = int(unconverted_number, 8)
            convertedTO_hexadecimal = hex(int(unconverted_number , 8))[2:].upper()      
            print()
            print("Original: " + str(unconverted_number))
            print("Converted to Binary: " + str(convertedTO_binary))
            print("Converted to Decimal: " + str(convertedTO_decimal))
            print("Converted to Hexadecimal: " + str(convertedTO_hexadecimal))
            
        case "4":
            
            print("hello")
            convertedTO_binary = bin(int(unconverted_number, 16))[2:]
            convertedTO_decimal = int(unconverted_number, 16)
            convertedTO_octal = oct(int(unconverted_number , 16))[2:]   
            print()
            print("Original: " + str(unconverted_number).upper())
            print("Converted to Binary: " + str(convertedTO_binary))
            print("Converted to Decimal: " + str(convertedTO_decimal))
            print("Converted to Octal: " + str(convertedTO_octal))
        
        
    print( "=" * 15)
    padayun = input("Start again? [y/n]: ")
    if(padayun == "n" ):
        running = False
        
    print()


