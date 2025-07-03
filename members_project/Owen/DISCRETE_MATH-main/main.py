from ST import ST
from Ciphers import Ciphers
from Sorting import Sorting
from Conversion import Conversion
from Prime import Prime, password
from GCD_LCM import GCD_LCM
from Searching import Searching

#region main
from basic_math import bMath
from TOOLS import TOOLS
# TOOLS.clear_screen()    
# passkey = input("input password: ")
# if passkey != password:
#     print("you are not the owner of this code.")
#     quit()

TOOLS.clear_screen()

picked:int = -2

classes = [
    ST,
    Ciphers,
    Sorting,
    Conversion,
    Prime,
    GCD_LCM,
    Searching
]

while picked != -1: #-1 is used to exit the loop
    TOOLS.clear_screen()
    # print(TOOLS.clear_screen())
    TOOLS.print_type("pick a class to open")
    for i, cls in enumerate(classes):
        TOOLS.print_type(f"{i + 1}. {cls.__name__}")
    picked = int(TOOLS.input_type("Enter the number of the class you want to open: ")) - 1

    #picks the class based on user input
    if picked < 0 or picked >= len(classes):
        TOOLS.print_type("Invalid choice. Please run the program again.")
        exit()

    picked_class = classes[picked]
    picked_class()
    while True:
        print()
        decision = input("would you like to restart the class? (y/N): ")
        if decision.lower() == 'y':
            picked_class()
        else:
            break
#endregion

#region test
# myarr = [1,3,5,7,9,2,4,6,8,0]

# coloredArr = arrColor(myarr, [0], [8], [5,6])
# print(coloredArr)
# print(TOOLS.is_prime(29))  # True
# print(TOOLS.is_prime(15))  # False
# print(TOOLS.is_prime(2))   # True
#endregion test
