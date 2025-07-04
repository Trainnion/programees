import os


def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            print(f"Iteration {i+1}.{j+1}: {arr}")
        if not swapped:
            break
    print("Bubble Sort Result:", arr)

    return arr

def selection_sort(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Iteration {i+1}: {arr}")
    print("Selection Sort Result:", arr)

    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Iteration {i}.{i-j}: {arr}")
        arr[j + 1] = key
        print(f"After inserting element {i}: {arr}")
    print("Insertion Sort Result:", arr)

    return arr

def merge_sort(arr, _depth=0):
    # Add _depth for pretty printing
    if len(arr) <= 1:
        print("  " * _depth + f"Returning: {arr.copy()}")
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], _depth+1)
    right = merge_sort(arr[mid:], _depth+1)
    result = merge(left, right)
    print("  " * _depth + f"Merging: {left} + {right} => {result}")
    if _depth == 0:
        print("Merge Sort Result:", result)
    
    return result

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, _depth=0):
    arr = arr.copy()
    if len(arr) <= 1:
        print("  " * _depth + f"Returning: {arr}")
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    print("  " * _depth + f"Pivot: {pivot} | less: {less} | greater: {greater}")
    result = quick_sort(less, _depth+1) + [pivot] + quick_sort(greater, _depth+1)
    print("  " * _depth + f"Combined: {result}")
    if _depth == 0:
        print("Quick Sort Result:", result)
    
    return result

def heap_sort(arr):
    import heapq
    arr = arr.copy()
    heapq.heapify(arr)
    print(f"Heapified: {arr}")
    result = []
    for i in range(len(arr)):
        smallest = heapq.heappop(arr)
        result.append(smallest)
        print(f"Iteration {i+1}: {result} (heap: {arr})")
    print("Heap Sort Result:", result)

    return result

def bucket_sort(arr):
    if not arr:
        print("No numbers entered.")
    
        return arr
    max_value = max(arr)
    bucket = [[] for _ in range(max_value // 10 + 1)]
    for idx, num in enumerate(arr):
        bucket[num // 10].append(num)
        # Print buckets after each insertion
        print(f"Iteration {idx+1}: ", end="")
        for b_idx, b in enumerate(bucket):
            print(f"Bucket {b_idx}: {b}  ", end="")
        print()
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])
        print(f"After sorting bucket {i}: {bucket[i]}")
    sorted_numbers = [num for sublist in bucket for num in sublist]
    print("Bucket Sort Result:", sorted_numbers)

    return sorted_numbers

def comb_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False
    iteration = 1
    while not sorted_flag:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        sorted_flag = True
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
                print(f"Iteration {iteration}: {arr}")
            iteration += 1
    print("Comb Sort Result:", arr)

    return arr

def radix_sort(arr):
    arr = arr.copy()
    if not arr:
        print("No numbers entered.")
    
        return arr
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        print(f"Count after exp={exp}: {count}")
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
        print(f"Output after exp={exp}: {output}")
        for i in range(n):
            arr[i] = output[i]
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        print(f"Sorting by digit at exp={exp}")
        counting_sort(arr, exp)
        print(f"Array after exp={exp}: {arr}")
        exp *= 10
    print("Radix Sort Result:", arr)

    return arr

def tree_sort(arr):
    os.system("cls")
    unsorted = input("Enter numbers to sort (space separated): ")
    arr = list(map(int, unsorted.split()))
    if not arr:
        print("No numbers entered.")
        return
    n = len(arr)
    heap_type = input("Choose heap type (min/max): ").strip().lower()

    def heapify_max(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            print("Current state:", arr)
            heapify_max(arr, n, largest)

    def heapify_min(arr, n, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            print("Current state:", arr)
            heapify_min(arr, n, smallest)

    if heap_type == "min":
        # Build a minheap
        for i in range(n // 2 - 1, -1, -1):
            heapify_min(arr, n, i)
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            print("Current state:", arr)
            heapify_min(arr, i, 0)
        arr.reverse()  # To get ascending order
        print("Sorted numbers (Min Heap):", arr)
    else:
        # Default to maxheap
        for i in range(n // 2 - 1, -1, -1):
            heapify_max(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            print("Current state:", arr)
            heapify_max(arr, i, 0)
        print("Sorted numbers (Max Heap):", arr)

def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2
    iteration = 1
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                print(f"Iteration {iteration}: {arr}")
                iteration += 1
            arr[j] = temp
            print(f"After inserting element at index {i}: {arr}")
        gap //= 2
    print("Shell Sort Result:", arr)
    return arr

sorting = [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Bucket Sort",
            "Shell Sort",
            "Comb Sort",
            "Radix Sort",
            "Tree Sort",
            "Heap Sort" 
         ]
running = True
while(running):
    os.system("cls")
    print("Sorting Algorithms")
    i = 1
    for sorter in sorting:
        print(f"{i}.", sorter)
        i = i + 1

    sorter = input("Choose Sorting Algorithm: ")
    match sorter:
        case "1":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            bubble_sort(arr)
        case "2":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            selection_sort(arr)
        case "3":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            insertion_sort(arr)
        case "4":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            merge_sort(arr)
        case "5":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            quick_sort(arr)
        case "6":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            bucket_sort(arr)
        case "7":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            shell_sort(arr)
        case "8":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            comb_sort(arr)
        case "9":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            radix_sort(arr)
        case "10":
            tree_sort([])  # tree_sort will prompt for input itself
        case "11":
            arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
            heap_sort(arr)
        case _:
            print("Invalid choice.")
        
    restart = input("\nStart again? [y/n]: ")
    if restart.lower() == "n":
        running = False
        running = False

