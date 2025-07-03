from TOOLS import TOOLS
from Prime import Prime

class GCD_LCM():
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "(GCD) Euclidean algorithm",
            "(LCM) Using GCD",
            # "Prime factorization",
            # "Binary GCD algorithm",
        ]
        self.start()

    def start(self):
        TOOLS.print_type("Pick a method to calculate GCD:")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please try again.")
            return
        method_name = self.methods[choice]
        TOOLS.print_type("")
        TOOLS.print_type(f"You chose: {method_name}")

        match method_name:
            case "(GCD) Euclidean algorithm":
                a = int(TOOLS.input_type("Enter first number (a): "))
                b = int(TOOLS.input_type("Enter second number (b): "))
                result = self.eucledian(a, b)
                TOOLS.sleep(0.5)
                print()
                TOOLS.print_type(f"GCD({a}, {b}) = {result}")
            case "(LCM) Using GCD":
                a = int(TOOLS.input_type("Enter first number (a): "))
                b = int(TOOLS.input_type("Enter second number (b): "))
                gcd = self.eucledian(a, b)
                TOOLS.sleep(0.5)
                print()
                TOOLS.print_type(f"GCD({a}, {b}) = {gcd}")
                TOOLS.print_type(f"LCM({a}, {b}) = (a * b) // GCD(a, b)")
                TOOLS.print_type(f"LCM({a}, {b}) = ({a} * {b}) // {gcd}")
                lcm = (a * b) // gcd
                TOOLS.print_type(f"LCM({a}, {b}) = {lcm}")


    def eucledian(self, a, b):
        """Calculate GCD using the Euclidean algorithm."""
        print()
        while b: #runs when b is not zero
            TOOLS.print_type(f"{a} = {b}({a // b}) + {a % b}")
            a, b = b, a % b #swap
        return a

    # def