import os
import sys

# Get the absolute directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

menu = [
    ("Arithmetic Operations", os.path.join(BASE_DIR, "arithmetic_operations.py")),
    ("Bitwise/Binary Operations", os.path.join(BASE_DIR, "bitwise_binary.py")),
    ("Chinese Remainder Theorem", os.path.join(BASE_DIR, "chinese_remainder.py")),
    ("Conversions", os.path.join(BASE_DIR, "conversions.py")),
    ("Euler's Totient Function", os.path.join(BASE_DIR, "euler_Totient.py")),
    ("GCD/LCM Calculator", os.path.join(BASE_DIR, "gcd_lcm_calculator.py")),
    ("Greedy Algorithms", os.path.join(BASE_DIR, "greedy_Algorithm.py")),
    ("Logical Equivalence", os.path.join(BASE_DIR, "logical_equivalence.py")),
    ("Logic Tables", os.path.join(BASE_DIR, "logicTables.py")),
    ("Modulo Functions", os.path.join(BASE_DIR, "modulo_func.py")),
    ("NoLibraries Ciphers", os.path.join(BASE_DIR, "NoLibraries_ciphers.py")),
    ("Number Theory", os.path.join(BASE_DIR, "number_theory.py")),
    ("Ones/Twos Complement", os.path.join(BASE_DIR, "ones_twos_complement.py")),
    ("Propositional Logic", os.path.join(BASE_DIR, "propositional_Logic.py")),
    ("Searching Algorithms", os.path.join(BASE_DIR, "searching.py")),
    ("Set Theory", os.path.join(BASE_DIR, "set_theory.py")),
    ("Sorting Algorithms", os.path.join(BASE_DIR, "sorting.py")),
    ("Tree Factorization", os.path.join(BASE_DIR, "tree_factorization.py")),
    ("Latest Ciphers", os.path.join(BASE_DIR, "Latest_ciphers.py"))
]

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Main Menu\n")
        for i, (desc, _) in enumerate(menu, 1):
            print(f"{i}. {desc}")
        print("0. Exit")
        choice = input("\nChoose a module: ")
        if choice == "0":
            print("Exiting...")
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(menu):
                file_path = menu[idx][1]
                print(f"\n[Running: {file_path}]")
                # Use the specified Python executable and pass the full file path (directory) to os.system
                exit_code = os.system(f'C:/Users/UZZIAH/AppData/Local/Programs/Python/Python313/python.exe "{file_path}"')
                if exit_code != 0:
                    print(f"\n[Error] Failed to run: {file_path}\nExit code: {exit_code}")
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}")
        input("\nPress Enter to return to the main menu...")


main()


