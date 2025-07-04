import os
os.system("cls")

print("Searching Algorithms")
searching = [
    "Linear Search (unsorted)",
    "Binary Search (sorted)",
    "Interpolation Search (sorted)",
    "Ternary Search (sorted)",
]

def Linear_search():
    os.system("cls")
    numbers = input("Enter numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))
    found = False
    for idx, num in enumerate(numbers):
        print(f"Checking index {idx}: {num}")
        if num == target:
            print(f"Number {target} found at index {idx}.")
            found = True
            break
    if not found:
        print(f"Number {target} not found in the list.")

def Binary_search():
    os.system("cls")
    numbers = input("Enter sorted numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))
    
    left, right = 0, len(numbers) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Checking middle index {mid}: {numbers[mid]}")
        
        if numbers[mid] == target:
            print(f"Number {target} found at index {mid}.")
            found = True
            break
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if not found:
        print(f"Number {target} not found in the list.")
        
def Interpolation_search():
    os.system("cls")
    numbers = input("Enter sorted numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))

    low = 0
    high = len(numbers) - 1
    found = False

    while low <= high and target >= numbers[low] and target <= numbers[high]:
        if low == high:
            if numbers[low] == target:
                print(f"Number {target} found at index {low}.")
                found = True
            break

        # Interpolation formula
        pos = low + ((high - low) // (numbers[high] - numbers[low]) * (target - numbers[low]))

        if numbers[pos] == target:
            print(f"Number {target} found at index {pos}.")
            found = True
            break
        elif numbers[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    if not found:
        print(f"Number {target} not found in the list.")

def Ternary_search():
    os.system("cls")
    numbers = input("Enter sorted numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))
    left, right = 0, len(numbers) - 1
    found = False
    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third
        print(f"Checking indices {mid1}: {numbers[mid1]}, {mid2}: {numbers[mid2]}")
        if numbers[mid1] == target:
            print(f"Number {target} found at index {mid1}.")
            found = True
            break
        if numbers[mid2] == target:
            print(f"Number {target} found at index {mid2}.")
            found = True
            break
        if target < numbers[mid1]:
            right = mid1 - 1
        elif target > numbers[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    if not found:
        print(f"Number {target} not found in the list.")

def Interval_search():
    os.system("cls")
    numbers = input("Enter numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    start = int(input("Enter interval start: "))
    end = int(input("Enter interval end: "))
    found_indices = []
    for idx, num in enumerate(numbers):
        if start <= num <= end:
            found_indices.append(idx)
            print(f"Number {num} at index {idx} is within the interval [{start}, {end}].")
    if not found_indices:
        print(f"No numbers found in the interval [{start}, {end}].")

def Jump_search():
    import math
    os.system("cls")
    numbers = input("Enter sorted numbers (space separated): ")
    numbers = list(map(int, numbers.split()))
    target = int(input("Enter number to search for: "))
    n = len(numbers)
    step = int(math.sqrt(n))
    prev = 0
    found = False
    # Find the block where the target may be present
    while prev < n and numbers[min(step, n)-1] < target:
        print(f"Jumping to index {min(step, n)-1}: {numbers[min(step, n)-1]}")
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            break
    # Linear search in the found block
    for idx in range(prev, min(step, n)):
        print(f"Checking index {idx}: {numbers[idx]}")
        if numbers[idx] == target:
            print(f"Number {target} found at index {idx}.")
            found = True
            break
    if not found:
        print(f"Number {target} not found in the list.")

# Add Interval Search and Jump Search to the menu
searching.append("Interval Search (unsorted)")
searching.append("Jump Search (sorted)")
       
running = True 
while running:
    os.system("cls")
    print("Searching Algorithms")
    for i, algo in enumerate(searching, start=1):
        print(f"{i}. {algo}")

    choice = input("Choose an algorithm: ")

    match choice:
        case '1':
            Linear_search()
        case '2':
            Binary_search()
        case '3':
            Interpolation_search()
        case '4':
            Ternary_search()
        case '5':
            Interval_search()
        case '6':
            Jump_search()
            

    decision = input("\nDo you want to continue? (y/n): ")
    if decision.lower() == 'n':
       running = False
       os.system("cls")
       print("Exiting the program.")