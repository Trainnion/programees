from TOOLS import TOOLS
class Conversion: #class for conversion
    def __init__(self):
        print("what the fuck bro")
        TOOLS.clear_screen()
        self.methods = [
            "binary to octal",
            "binary to decimal",
            "binary to hex",

            "decimal to binary",
            "decimal to octal",
            "decimal to hex",

            "octal to binary",
            "octal to decimal",
            "octal to hex",

            "hex to binary",
            "hex to octal",
            "hex to decimal",
        ]
        self.start()
        # raise NotImplementedError("This class cannot be instantiated directly.")

    def start(self):
        print("Pick a conversion method:")
        for i, method in enumerate(self.methods):
            print(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.methods):
            print("Invalid choice. Please try again.")
            return
        method_name = self.methods[choice]
        print()
        print(f"You chose: {method_name}")
        match method_name:
            case "binary to octal":
                binary = TOOLS.input_type("Enter binary number: ")
                result = self.btoo(binary)
                TOOLS.print_type(f"Octal: {result}")
            case "binary to decimal":
                binary = TOOLS.input_type("Enter binary number: ")
                result = self.btod(binary)
                TOOLS.print_type(f"Decimal: {result}")
            case "binary to hex":
                binary = TOOLS.input_type("Enter binary number: ")
                result = self.btoh(binary)
                TOOLS.print_type(f"Hex: {result}")
            case "decimal to binary":
                decimal = int(TOOLS.input_type("Enter decimal number: "))
                result = self.dtob(decimal)
                TOOLS.print_type(f"Binary: {result}")
            case "decimal to octal":
                decimal = int(TOOLS.input_type("Enter decimal number: "))
                result = self.dtoo(decimal)
                TOOLS.print_type(f"Octal: {result}")
            case "decimal to hex":
                decimal = int(TOOLS.input_type("Enter decimal number: "))
                result = self.dtoh(decimal)
                TOOLS.print_type(f"Hex: {result}")
            case "octal to binary":
                octal = TOOLS.input_type("Enter octal number: ")
                result = self.otob(octal)
                TOOLS.print_type(f"Binary: {result}")
            case "octal to decimal":
                octal = TOOLS.input_type("Enter octal number: ")
                result = self.otod(octal)
                TOOLS.print_type(f"Decimal: {result}")
            case "octal to hex":
                octal = TOOLS.input_type("Enter octal number: ")
                result = self.otoh(octal)
                TOOLS.print_type(f"Hex: {result}")
            case "hex to binary":
                hex_num = TOOLS.input_type("Enter hex number: ")
                result = self.htob(hex_num)
                TOOLS.print_type(f"Binary: {result}")
            case "hex to octal":
                hex_num = TOOLS.input_type("Enter hex number: ")
                result = self.htoo(hex_num)
                TOOLS.print_type(f"Octal: {result}")
            case "hex to decimal":
                hex_num = TOOLS.input_type("Enter hex number: ")
                result = self.htod(hex_num)
                TOOLS.print_type(f"Decimal: {result}")
    
    #decimal to binary
    # @staticmethod
    def dtob(self, decimal: int) -> str:
        if decimal == 0:
            TOOLS.print_type("0", "yellow")
            return "0"

        binary = ""
        base = 2

        TOOLS.print_type(f"Converting {decimal} to binary:", "cyan", delay=0.001)

        while decimal > 0:
            remainder = decimal % base
            TOOLS.print_type(f"{decimal} ÷ {base} = {decimal // base} remainder {remainder}", "blue", delay=0.001)
            binary = str(remainder) + binary
            decimal //= base
            TOOLS.sleep(0.3)

        TOOLS.print_type(f"Binary: {binary}", "yellow", delay=0.001)
        return binary

    
    #decimal to octal
    # @staticmethod
    def dtoo(self, decimal: int):
        output = ""
        sub = 8
        TOOLS.print_type(f"Converting {decimal} to Octal...", "cyan", delay=0.001)

        while True:
            r = decimal % sub  # remainder
            TOOLS.print_type(f"{decimal} % {sub} = {r} → prepend to result", "yellow", delay=0.001)
            decimal //= sub
            output = str(r) + output
            TOOLS.print_type(f"New decimal value: {decimal}", "blue", delay=0.001)
            if decimal == 0: break

        TOOLS.print_type(f"Final Octal: {output}", "green", delay=0.001)
        return output


    #decimal to hex
    # @staticmethod
    def dtoh(self, decimal: int):
        output = ""
        sub = 16
        TOOLS.print_type(f"Converting {decimal} to Hexadecimal...", "cyan", delay=0.001)

        while True:
            r = decimal % sub  # remainder
            TOOLS.print_type(f"{decimal} % {sub} = {r}", "yellow", delay=0.001)

            match r:
                case 10:
                    r = "A"
                case 11:
                    r = "B"
                case 12:
                    r = "C"
                case 13:
                    r = "D"
                case 14:
                    r = "E"
                case 15:
                    r = "F"

            decimal //= sub
            TOOLS.print_type(f"New decimal value: {decimal}", "blue", delay=0.001)
            output = str(r) + output
            TOOLS.print_type(f"Current Hex: {output}", "magenta", delay=0.001)

            if decimal == 0: break

        TOOLS.print_type(f"Final Hexadecimal: {output}", "green", delay=0.001)
        return output

    
    #binary to decimal
    # @staticmethod
    def btod(self, binary: str):
        binary = str(binary)
        r_binary = ""
        output = 0
        sub = 2

        TOOLS.print_type(f"Converting binary '{binary}' to decimal...", "cyan", delay=0.001)

        for char in binary:
            r_binary = char + r_binary  # reverse the binary string
        TOOLS.print_type(f"Reversed binary: {r_binary}", "yellow", delay=0.001)

        for i in range(0, len(r_binary)):
            value = int(r_binary[i]) * sub ** i
            TOOLS.print_type(f"{r_binary[i]} * {sub}^{i} = {value}", "blue", delay=0.001)
            output += value

        TOOLS.print_type(f"Final Decimal: {output}", "green", delay=0.001)
        return output


    #octal to decimal
    # @staticmethod
    def otod(self, octal: str):
        octal = str(octal)
        r_octal = ""
        output = 0
        sub = 8

        TOOLS.print_type(f"Converting octal '{octal}' to decimal...", "cyan", delay=0.001)

        for char in octal:
            r_octal = char + r_octal
        TOOLS.print_type(f"Reversed octal: {r_octal}", "yellow", delay=0.001)

        for i in range(0, len(r_octal)):
            value = int(r_octal[i]) * sub ** i
            TOOLS.print_type(f"{r_octal[i]} * {sub}^{i} = {value}", "blue", delay=0.001)
            output += value

        TOOLS.print_type(f"Final Decimal: {output}", "green", delay=0.001)
        return output


    #hex to decimal
    # @staticmethod
    #hex to decimal
    # @staticmethod
    def htod(self, hex:str):
        """converts hex to decimal"""
        hex = str(hex).upper()
        r_hex = ""
        output = 0
        sub = 16

        TOOLS.print_type("Converting hexadecimal to decimal...", "cyan", delay=0.001)

        for char in hex:
            r_hex = char + r_hex

        TOOLS.print_type(f"Reversed hex: {r_hex}", "yellow", delay=0.001)

        for i in range(0,len(r_hex)):
            to_out = 0
            match r_hex[i]:
                case "A": to_out = 10
                case "B": to_out = 11
                case "C": to_out = 12
                case "D": to_out = 13
                case "E": to_out = 14
                case "F": to_out = 15
                case _: to_out = int(r_hex[i])
            
            term = to_out * sub ** i
            TOOLS.print_type(f"{r_hex[i]} → {to_out} × {sub}^{i} = {term}", "blue", delay=0.001)
            output += term
        
        TOOLS.print_type(f"Final Decimal Value: {output}", "green", delay=0.001)
        return output


    #binary to octal
    def btoo(self, binary:str):
        binary = str(binary)
        TOOLS.print_type("Converting binary to octal...", "cyan", delay=0.001)
        decimal = self.btod(binary)
        TOOLS.print_type(f"Binary to Decimal: {decimal}", "yellow", delay=0.001)
        octal = self.dtoo(decimal)
        TOOLS.print_type(f"Decimal to Octal: {octal}", "green", delay=0.001)
        return octal

    #binary to hex
    def btoh(self, binary:str):
        binary = str(binary)
        TOOLS.print_type("Converting binary to hexadecimal...", "cyan", delay=0.001)
        decimal = self.btod(binary)
        TOOLS.print_type(f"Binary to Decimal: {decimal}", "yellow", delay=0.001)
        hexa = self.dtoh(decimal)
        TOOLS.print_type(f"Decimal to Hex: {hexa}", "green", delay=0.001)
        return hexa
    
    #octal to binary
    def otob(self, octal:str):
        octal = str(octal)
        TOOLS.print_type("Converting octal to binary...", "cyan", delay=0.001)
        decimal = self.otod(octal)
        TOOLS.print_type(f"Octal to Decimal: {decimal}", "yellow", delay=0.001)
        binary = self.dtob(decimal)
        TOOLS.print_type(f"Decimal to Binary: {binary}", "green", delay=0.001)
        return binary

    #octal to hex
    def otoh(self, octal:str):
        octal = str(octal)
        TOOLS.print_type("Converting octal to hexadecimal...", "cyan", delay=0.001)
        decimal = self.otod(octal)
        TOOLS.print_type(f"Octal to Decimal: {decimal}", "yellow", delay=0.001)
        hexa = self.dtoh(decimal)
        TOOLS.print_type(f"Decimal to Hex: {hexa}", "green", delay=0.001)
        return hexa

    #hex to binary
    def htob(self, hex:str):
        hex = str(hex)
        TOOLS.print_type("Converting hexadecimal to binary...", "cyan", delay=0.001)
        decimal = self.htod(hex)
        TOOLS.print_type(f"Hex to Decimal: {decimal}", "yellow", delay=0.001)
        binary = self.dtob(decimal)
        TOOLS.print_type(f"Decimal to Binary: {binary}", "green", delay=0.001)
        return binary

    #hex to octal
    def htoo(self, hex:str):
        hex = str(hex)
        TOOLS.print_type("Converting hexadecimal to octal...", "cyan", delay=0.001)
        decimal = self.htod(hex)
        TOOLS.print_type(f"Hex to Decimal: {decimal}", "yellow", delay=0.001)
        octal = self.dtoo(decimal)
        TOOLS.print_type(f"Decimal to Octal: {octal}", "green", delay=0.001)
        return octal

    

