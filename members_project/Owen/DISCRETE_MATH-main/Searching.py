from TOOLS import TOOLS
from Sorting import Sorting

def arrColor(arr, blue=None, green=None, yellow=None, magenta=None, label="", delay=0.001):
    blue = blue or []
    green = green or []
    yellow = yellow or []
    magenta = magenta or []

    color_codes = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'magenta': '\033[95m'
    }

    display_arr = "["
    for i, val in enumerate(arr):
        color = None
        if i in magenta:
            color = color_codes['magenta']
        elif i in yellow:
            color = color_codes['yellow']
        elif i in blue:
            color = color_codes['blue']
        elif i in green:
            color = color_codes['green']

        if color:
            display_arr += f"{color}{val}\033[0m, "
        else:
            display_arr += f"{val}, "

    display_arr = display_arr.rstrip(", ") + "]"
    if label:
        display_arr = f"{label}\t{display_arr}"

    TOOLS.print_type(display_arr, None, delay)


class Searching:
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "Linear Search", #sequential
            "Binary Search", #interval
            "Interpolation Search"
            # "Jump Search",
            # "Exponential Search",
            # "Interpolation Search"
        ]
        self.start()

    def start(self):
        TOOLS.print_type("Pick a method to perform searching:")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please try again.")
            return
        method_name = self.methods[choice]

        match method_name:
            case "Linear Search":
                TOOLS.print_type("You chose Linear Search.", "blue")
                self._linear_search()
            case "Binary Search":
                TOOLS.print_type("You chose Binary Search.", "blue")
                self._binary_search()
            case "Interpolation Search":
                TOOLS.print_type("you chose Interpolation Search.", "blue")
                self._interpolation_search()
    
    def _linear_search(self): 
        TOOLS.print_type("Performing Linear Search...", "cyan", delay=0.001)

        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mBlue\033[0m   - Currently checking", delay=0.001)
        TOOLS.print_type("  \033[93mYellow\033[0m - Match found", delay=0.001)
        TOOLS.print_type("", None)

        arr = list(map(int, TOOLS.input_type("Enter the elements of the array (space separated): ", "cyan").split()))
        target = int(TOOLS.input_type("Enter the number to search for: ", "cyan"))
        
        index = self.linear_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"\nFound {target} at index {index}.", "yellow", delay=0.001)
        else:
            TOOLS.print_type(f"\n{target} not found in the array.", "red", delay=0.001)

    def linear_search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                arrColor(arr, yellow=[i])
                return i
            arrColor(arr, blue=[i])
            TOOLS.sleep(0.1)
        return -1

    
    def _binary_search(self):
        print()
        TOOLS.print_type("Performing Binary Search...", "cyan", delay=0.001)

        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mBlue\033[0m    - Current left/right bounds", delay=0.001)
        TOOLS.print_type("  \033[95mMagenta\033[0m - Middle element", delay=0.001)
        TOOLS.print_type("  \033[93mYellow\033[0m  - Match found", delay=0.001)
        TOOLS.print_type("")

        arr = list(map(int, TOOLS.input_type("Enter the elements of the array (space separated): ", "cyan").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}", "green", delay=0.001)

        target = int(TOOLS.input_type("Enter the number to search for: ", "cyan"))
        index = self.binary_search(arr, target)

        if index != -1:
            TOOLS.print_type(f"\nFound {target} at index {index}.", "yellow", delay=0.001)
        else:
            TOOLS.print_type(f"\n{target} not found in the array.", "red", delay=0.001)

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                arrColor(arr, yellow=[mid])
                return mid
            else:
                arrColor(arr, blue=[left, right], magenta=[mid])
                TOOLS.sleep(0.5)

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    
    #region interpolation search
    def _interpolation_search(self):
        """Perform interpolation search on a sorted list."""
        print()
        TOOLS.print_type("Performing Interpolation Search...")
        # Example implementation
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}", "green")
        target = int(TOOLS.input_type("Enter the number to search for: "))
        index = self.interpolation_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"Found {target} at index {index}.", "yellow")
        else:
            TOOLS.print_type(f"{target} not found in the array.", "red")

    def interpolation_search(self, arr, target):
        key = target
        low = 0
        high = len(arr) - 1

        print()
        TOOLS.print_type("low", "blue")
        TOOLS.print_type("high", "green")
        TOOLS.print_type("pos", "yellow")
        print()

        while low <= high and arr[low] <= key <= arr[high]:


            if arr[high] == arr[low]:
                if arr[low] == key:
                    return low
                else:
                    break

            pos = low + int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))
            print(f"pos: {pos}; low: {low}; high: {high}; arr[low]:{arr[low]}; arr[high]: {arr[high]}")
            
            #text
            displayed_arr = ""
            for i in range(len(arr)):
                # if i = 0:
                #     displayed_arr += f"{arr[i]}"
                #     continue
                if i == pos:
                    displayed_arr += f", \033[93m{arr[pos]}\033[0m"
                elif i == low:
                    displayed_arr += f", \033[94m{arr[low]}\033[0m"
                elif i == high:
                    displayed_arr += f", \033[92m{arr[high]}\033[0m"
                
                else:
                    displayed_arr += f", {arr[i]}"
            displayed_arr = f"[{displayed_arr[2:]}]"
            
            TOOLS.print_type(displayed_arr)
            if pos < low or pos > high:
                break
            if arr[pos] < key:
                low = pos + 1
            elif arr[pos] > key:
                high = pos - 1
            else:
                return pos
        return -1
    #endregion interpolation search

    #region ternary search
    def _ternary_search(self):
        """Perform ternary search on a sorted list."""
        print()
        TOOLS.print_type("Performing Ternary Search...")
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}", "blue")
        target = int(TOOLS.input_type("Enter the number to search for: "))
        index = self.ternary_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"Found {target} at index {index}.", "yellow")
        else:
            TOOLS.print_type(f"{target} not found in the array.", "red")

    def ternary_search(self, arr, target):
        """Perform ternary search on a sorted list."""
        left, right = 0, len(arr) - 1
        while left <= right:
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        return -1
    #endregion ternary search