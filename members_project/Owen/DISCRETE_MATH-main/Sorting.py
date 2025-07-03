from TOOLS import TOOLS

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


class Sorting:
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Bucket Sort",
            "Shell Sort",
            "Comb Sort",
            "Radix Sort",
            # "Tree Sort",
        ]
        self.start()
        # self.selection_sort()  # For testing purposes, directly calling bubble_sort

    def start(self):
        TOOLS.print_type("pick your desired sorting method.")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        TOOLS.print_type("")
        choice = int(TOOLS.input_type("Enter the number of the method you want to use: ")) - 1
        TOOLS.print_type("")
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please run the program again.")
            exit()
        picked_method = self.methods[choice]
        TOOLS.print_type(f"You have selected: {picked_method}")
        match picked_method:
            case "Bubble Sort":
                self._bubble_sort()
            case "Selection Sort":
                self._selection_sort()
            case "Insertion Sort":
                self._insertion_sort()
            case "Merge Sort":
                self._merge_sort()
            case "Quick Sort":
                self._quick_sort()
            case "Bucket Sort":
                self._bucket_sort()
            case "Shell Sort":
                self._shell_sort()
            case "Comb Sort":
                self._comb_sort()
            case "Radix Sort":
                self._radix_sort()
            case "Tree Sort":
                self._tree_sort()
            case _:
                TOOLS.print_type("This method is not implemented yet.")

#region bubble sort
    def _bubble_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        unsorted = arr.copy()
        self.bubble_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Unsorted array:\t {unsorted}", "blue")
        TOOLS.print_type(f"Sorted array:\t {arr}", "yellow")

    def bubble_sort(self, arr):
        length = len(arr)
        for i in range(length):
            for j in range(0, length - i - 1):
                arrColor(arr, [j], [j + 1], label="Comparing:")
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                    arrColor(arr, [], [], [j, j + 1], label="Swapped:")
        return arr
#endregion bubble sort

#region selection sort
    def _selection_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.selection_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}", "yellow")

    def selection_sort(self, arr):
        length = len(arr)
        for i in range(length):
            min_idx = i
            for j in range(i + 1, length):
                arrColor(arr, [i], [j], [], [min_idx], label="Checking:")
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    arrColor(arr, [i], [j], [], [min_idx], label="New min found:")

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            arrColor(arr, [], [], [i, min_idx], label="Swapped:")
        return arr
#endregion selection sort

#region insertion sort
    def _insertion_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.insertion_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}", "yellow")

    def insertion_sort(self, arr, visualize=False):
        length = len(arr)
        for i in range(1, length):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                if visualize:
                    arrColor(arr, [j], [key])
                j -= 1
            arr[j + 1] = key

        return arr
#endregion insertion sort

#region merge sort
    def _merge_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.merge_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}", "yellow")

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Sorting.merge_sort(L)
            Sorting.merge_sort(R)

            Sorting.merge(arr, L, R)
        return arr

    @staticmethod
    def merge(arr, L, R):
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                arrColor(arr, [], [], [], [k], label="Placing from L:")
                i += 1
            else:
                arr[k] = R[j]
                arrColor(arr, [], [], [], [k], label="Placing from R:")
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            arrColor(arr, [], [], [], [k], label="Placing remaining from L:")
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            arrColor(arr, [], [], [], [k], label="Placing remaining from R:")
            j += 1
            k += 1

#endregion merge sort

#region quick sort
    def _quick_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ", "cyan").split()))

        # Color legend
        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mi\033[0m - Partition index (left of pivot)", None, delay=0.001)
        TOOLS.print_type("  \033[92mj\033[0m - Scanning element", None, delay=0.001)
        TOOLS.print_type("  \033[95mPivot\033[0m - Pivot element", None, delay=0.001)
        TOOLS.print_type("  \033[93mSwapped\033[0m - Elements that were swapped", None, delay=0.001)
        TOOLS.print_type("", None)

        self.quick_sort(arr, 0, len(arr) - 1)

        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}", "yellow")

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            arrColor(arr, [i], [j], [], [high], label="Comparing with pivot:")
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                arrColor(arr, [], [], [i, j], [], label="Swapped:           ")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        arrColor(arr, [], [], [i + 1, high], [], label="Pivot placed:       ")
        return i + 1
#endregion quick sort

#region bucket sort
    def _bucket_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ", "cyan").split()))
        
        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mBlue\033[0m - Current number being bucketed", None, delay=0.001)
        TOOLS.print_type("  \033[92mGreen\033[0m - Element currently sorted in a bucket", None, delay=0.001)
        TOOLS.print_type("  \033[93mYellow\033[0m - Final assembly of sorted array", None, delay=0.001)
        TOOLS.print_type("", None)

        sorted_arr = self.bucket_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {sorted_arr}", "yellow")

    def bucket_sort(self, arr):
        n = len(arr)
        bucket = [[] for _ in range(n)]

        # Bucket allocation with color
        for j in arr:
            index_b = min(int(10 * j), n - 1)
            bucket[index_b].append(j)
            arrColor(arr, [arr.index(j)], [], [], [], label=f"Placing {j} into bucket {index_b}")

        # Sort each bucket
        for i in range(n):
            if bucket[i]:
                TOOLS.print_type(f"\nSorting bucket {i}: {bucket[i]}", "blue", delay=0.001)
                self.insertion_sort(bucket[i], visualize=True)

        # Concatenate all sorted buckets
        sorted_arr = []
        for i in range(n):
            if bucket[i]:
                arrColor(bucket[i], [], [], [], [], label=f"Adding bucket {i} to final array:")
            sorted_arr += bucket[i]

        arrColor(sorted_arr, [], [], list(range(len(sorted_arr))), [], label="Final Sorted Array:")
        return sorted_arr

#endregion bucket sort

#region shell sort
    def _shell_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ", "cyan").split()))

        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mBlue\033[0m - Index currently being considered", None, delay=0.001)
        TOOLS.print_type("  \033[92mGreen\033[0m - Key being inserted", None, delay=0.001)
        TOOLS.print_type("  \033[93mYellow\033[0m - Subarray being merged back", None, delay=0.001)
        TOOLS.print_type("", None)

        self.shell_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}", "yellow")

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            TOOLS.print_type(f"\nGap: {gap}", "magenta", delay=0.001)
            for start in range(gap):
                subarray_indices = list(range(start, n, gap))
                subarray = [arr[i] for i in subarray_indices]

                TOOLS.print_type(f"Subarray from indices {subarray_indices}:", "blue", delay=0.001)
                arrColor(subarray, list(range(len(subarray))), [], [], [], label="Before sorting:")

                self.insertion_sort(subarray, visualize=True)

                TOOLS.print_type(f"Sorted subarray: {subarray}", "green", delay=0.001)

                for idx, val in zip(subarray_indices, subarray):
                    arr[idx] = val

                arrColor(arr, [], [], subarray_indices, [], label="Merged into main array:")

            gap //= 2

        return arr
#endregion shell sort

#region comb sort
    def _comb_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ", "cyan").split()))

        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mBlue\033[0m - Comparing pair", delay=0.001)
        TOOLS.print_type("  \033[93mYellow\033[0m - Swapping pair", delay=0.001)
        TOOLS.print_type("  \033[92mGreen\033[0m - Final sorted array", delay=0.001)
        TOOLS.print_type("", None)

        self.comb_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}", "green")

    def comb_sort(self, arr):
        n = len(arr)
        gap = n
        shrink = 1.3
        sorted_flag = False

        while gap > 1 or not sorted_flag:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1

            TOOLS.print_type(f"\nCurrent gap: {gap}", "magenta", delay=0.001)
            sorted_flag = True

            for i in range(n - gap):
                arrColor(arr, [i], [i + gap])
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_flag = False
                    arrColor(arr, [], [], [i, i + gap])
        return arr
#endregion comb sort

#region radix sort
    def _radix_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ", "cyan").split()))

        TOOLS.print_type("\nLegend:", "yellow", delay=0.001)
        TOOLS.print_type("  \033[94mBlue\033[0m - Current digit pass", delay=0.001)
        TOOLS.print_type("  \033[92mGreen\033[0m - Final sorted list (vertical)", delay=0.001)
        TOOLS.print_type("", None)

        self.radix_sort(arr)

        TOOLS.sleep(0.5)
        TOOLS.print_type("\nSorted array (vertical):", "green", delay=0.001)
        for i, val in enumerate(arr, 1):
            TOOLS.print_type(f"{i}. {val}", "green", delay=0.001)

    def radix_sort(self, arr):
        if not arr:
            return arr
        max_num = max(arr)
        exp = 1
        pass_num = 1
        while max_num // exp > 0:
            TOOLS.print_type(f"\nPass {pass_num} (sorting by digit at place {exp}):", "blue", delay=0.001)
            self.counting_sort(arr, exp)
            arrColor(arr, blue=list(range(len(arr))))
            TOOLS.sleep(0.4)
            exp *= 10
            pass_num += 1
        return arr

    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1

        for i in range(n):
            arr[i] = output[i]
        return arr

#endregion radix sort

#region tree sort
    def _tree_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        sorted_arr = self.tree_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {sorted_arr}")

    def tree_sort(self, arr):
        class Node:
            def __init__(self, key):
                self.left = None
                self.right = None
                self.val = key

        def insert(root, key):
            if root is None:
                return Node(key)
            else:
                if root.val < key:
                    root.right = insert(root.right, key)
                else:
                    root.left = insert(root.left, key)
            return root

        def inorder_traversal(root, sorted_arr):
            if root:
                inorder_traversal(root.left, sorted_arr)
                sorted_arr.append(root.val)
                inorder_traversal(root.right, sorted_arr)

        root = None
        for key in arr:
            root = insert(root, key)

        sorted_arr = []
        inorder_traversal(root, sorted_arr)
        return sorted_arr
#endregion tree sort

#region tournament sort
    def _tournament_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        sorted_arr = self.tournament_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {sorted_arr}")

    def tournament_sort(self, arr):
        n = len(arr)
        if n == 0:
            return arr
        if n == 1:
            return arr

        # Create a tournament tree
        tree = [None] * (2 * n - 1)

        # Build the tree
        for i in range(n):
            tree[n - 1 + i] = arr[i]

        for i in range(n - 2, -1, -1):
            tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])

        sorted_arr = []
        while len(sorted_arr) < n:
            # Find the minimum element
            min_index = 0
            for i in range(1, n):
                if tree[n - 1 + i] < tree[n - 1 + min_index]:
                    min_index = i

            sorted_arr.append(tree[n - 1 + min_index])
            # Remove the minimum element from the tree
            tree[n - 1 + min_index] = float('inf')

            # Update the tree
            for i in range((n - 2) // 2, -1, -1):
                tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])

        return sorted_arr
#endregion tournament sort