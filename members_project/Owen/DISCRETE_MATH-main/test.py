import os
from functools import reduce
import base64

# ========== NUMBER SYSTEM CALCULATOR ==========

def getch():
    try:
        import msvcrt
        msvcrt.getch()
    except ImportError:
        input("Press Enter to continue...")

def Caesar_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = int(input("Input key: "))
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    caesar_cipher_text = ""
    for char in plain_text:
        upper_char = char.upper()
        if upper_char in alphabet:
            index = alphabet.index(upper_char)
            shifted_index = (index + key) % 26
            caesar_cipher_text += alphabet[shifted_index]
        else:
            caesar_cipher_text += char  
            
    os.system("cls")
    print("Original text: ", plain_text)
    print("Cipher Text: ", caesar_cipher_text)
    getch()

def Rail_fence():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = int(input("Input key: "))
    
    rails = [''] * key  # Initialize rail levels
    row, direction = 0, 1

    for char in plain_text:
        rails[row] += char
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1  # Switch direction

    print("Original text:", plain_text)
    print("Cipher Text:", ''.join(rails))
    getch()
    

def Vigenere_cipher():
    os.system("cls")

    plain_text = input("Input Plain text: ")
    key = input("Input key (word): ").upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ""
    
    key_index = 0
    for char in plain_text:
        upper_char = char.upper()
        if upper_char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            index = (alphabet.index(upper_char) + shift) % 26
            cipher_text += alphabet[index]
            key_index += 1  # Move to the next letter in the key
        else:
            cipher_text += char

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    getch()
    
def Playfair_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ").upper().replace("J", "I")
    key = input("Input key (word): ").upper().replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_key = ""
    for char in key:
        if char in alphabet and char not in matrix_key:
            matrix_key += char
    for char in alphabet:
        if char not in matrix_key:
            matrix_key += char

    matrix = [list(matrix_key[i*5:(i+1)*5]) for i in range(5)]

    # Prepare plaintext digraphs
    prepared = ""
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        if a not in alphabet:
            i += 1
            continue
        if i + 1 < len(plain_text):
            b = plain_text[i+1]
            if b not in alphabet:
                prepared += a
                i += 1
                continue
            if a == b:
                prepared += a + "X"
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + "X"
            i += 1

    # Encrypt digraphs
    cipher_text = ""
    for i in range(0, len(prepared), 2):
        a = prepared[i]
        b = prepared[i+1]
        row1 = col1 = row2 = col2 = 0
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == a:
                    row1, col1 = row, col
                if matrix[row][col] == b:
                    row2, col2 = row, col
        if row1 == row2:
            cipher_text += matrix[row1][(col1+1)%5]
            cipher_text += matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher_text += matrix[(row1+1)%5][col1]
            cipher_text += matrix[(row2+1)%5][col2]
        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    getch()
    
    
def Vernam_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = input("Input key (same length as plain text): ")

    if len(plain_text) != len(key):
        print("Error: Key must be the same length as the plain text.")
        return

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_char = chr((ord(plain_text[i]) + ord(key[i])) % 256)
        cipher_text += cipher_char

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    getch()
    
def One_Time_Pad_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = input("Input key (same length as plain text): ")

    if len(plain_text) != len(key):
        print("Error: Key must be the same length as the plain text.")
        return

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_char = chr((ord(plain_text[i]) + ord(key[i])) % 256)
        cipher_text += cipher_char

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    getch()
    
def Hill_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ").upper().replace(" ", "")
    print("Enter 4 numbers for the 2x2 key matrix (row-wise, separated by spaces):")
    key_input = input("Key: ")
    key_nums = key_input.strip().split()
    if len(key_nums) != 4 or not all(num.isdigit() for num in key_nums):
        print("Invalid key. Enter 4 numbers separated by spaces.")
        return
    key_matrix = [ [int(key_nums[0]), int(key_nums[1])],
                   [int(key_nums[2]), int(key_nums[3])] ]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Pad plaintext if needed
    if len(plain_text) % 2 != 0:
        plain_text += "X"
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        pair = [alphabet.index(plain_text[i]), alphabet.index(plain_text[i+1])]
        c1 = (key_matrix[0][0]*pair[0] + key_matrix[0][1]*pair[1]) % 26
        c2 = (key_matrix[1][0]*pair[0] + key_matrix[1][1]*pair[1]) % 26
        cipher_text += alphabet[c1] + alphabet[c2]
    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    getch()
    
def Columnar_cipher():
    os.system("cls")
    plain_text = input("Input Plain text: ")
    key = input("Input key (word): ").upper()

    # Create a list of columns based on the key
    columns = [''] * len(key)
    for i, char in enumerate(plain_text):
        columns[i % len(key)] += char

    # Sort the key to determine the order of columns
    sorted_key = sorted((char, i) for i, char in enumerate(key))
    
    # Create cipher text by reading columns in sorted order
    cipher_text = ''.join(columns[i] for _, i in sorted_key)

    os.system("cls")
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    getch()
    
def AES_cipher():
    os.system("cls")
    print("AES Cipher")
    plain_text = input("Input Plain text: ")
    key = input("Input key (16 characters): ")
    if len(key) != 16:
        print("Key must be exactly 16 characters (128 bits) for AES-128.")
        return
    cipher_bytes = []
    for i, c in enumerate(plain_text):
        cipher_bytes.append(chr(ord(c) ^ ord(key[i % 16])))
    cipher_text = ''.join(cipher_bytes)
    print("Encrypted (not real AES):", base64.b64encode(cipher_text.encode('utf-8')).decode())
    decrypted = []
    for i, c in enumerate(cipher_text):
        decrypted.append(chr(ord(c) ^ ord(key[i % 16])))
    print("Decrypted:", ''.join(decrypted))
    getch()

def DES_cipher():
    os.system("cls")
    print("DES Cipher")
    plain_text = input("Input Plain text: ")
    key = input("Input key (8 characters): ")
    if len(key) != 8:
        print("Key must be exactly 8 characters (64 bits) for DES.")
        return
    cipher_bytes = []
    for i, c in enumerate(plain_text):
        cipher_bytes.append(chr(ord(c) ^ ord(key[i % 8])))
    cipher_text = ''.join(cipher_bytes)
    print("Encrypted (not real DES):", base64.b64encode(cipher_text.encode('utf-8')).decode())
    decrypted = []
    for i, c in enumerate(cipher_text):
        decrypted.append(chr(ord(c) ^ ord(key[i % 8])))
    print("Decrypted:", ''.join(decrypted))
    getch()

def RSA_encryption():
    os.system("cls")
    print("RSA Encryption/Decryption)")
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    def modinv(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    d = modinv(e, phi)
    print(f"Public key: (e={e}, n={n})")
    print(f"Private key: (d={d}, n={n})")
    plain_text = input("Input Plain text (numbers only): ")
    encrypted = [pow(ord(c), e, n) for c in plain_text]
    print("Encrypted:", encrypted)
    decrypted = ''.join([chr(pow(c, d, n)) for c in encrypted])
    print("Decrypted:", decrypted)
    getch()
    
def SDES_cipher():
    os.system("cls")
    print("SDES Cipher")
    # SDES uses 10-bit key, 8-bit plaintext
    key = input("Enter 10-bit key (e.g., 1010000010): ")
    if len(key) != 10 or any(c not in '01' for c in key):
        print("Key must be 10 bits (0 or 1).")
        getch()
        return
    plaintext = input("Enter 8-bit plaintext (e.g., 11010111): ")
    if len(plaintext) != 8 or any(c not in '01' for c in plaintext):
        print("Plaintext must be 8 bits (0 or 1).")
        getch()
        return
    # Key generation (P10, LS-1, P8)
    def permute(bits, order):
        return ''.join(bits[i-1] for i in order)
    def left_shift(bits, n):
        return bits[n:] + bits[:n]
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    P4 = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    S0 = [
        [1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]
    ]
    S1 = [
        [0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]
    ]
    # Generate subkeys
    key_p10 = permute(key, P10)
    left, right = key_p10[:5], key_p10[5:]
    left1, right1 = left_shift(left, 1), left_shift(right, 1)
    K1 = permute(left1 + right1, P8)
    left2, right2 = left_shift(left1, 2), left_shift(right1, 2)
    K2 = permute(left2 + right2, P8)
    # Initial permutation
    bits = permute(plaintext, IP)
    def fk(bits, subkey):
        L, R = bits[:4], bits[4:]
        # Expand and permute
        R_exp = permute(R, EP)
        xor1 = ''.join(str(int(a)^int(b)) for a,b in zip(R_exp, subkey))
        # S-boxes
        def sbox(bits, box):
            row = int(bits[0]+bits[3], 2)
            col = int(bits[1]+bits[2], 2)
            return format(box[row][col], '02b')
        s0_out = sbox(xor1[:4], S0)
        s1_out = sbox(xor1[4:], S1)
        s_out = s0_out + s1_out
        s_out_p4 = permute(s_out, P4)
        L_out = ''.join(str(int(a)^int(b)) for a,b in zip(L, s_out_p4))
        return L_out + R
    # Round 1
    temp = fk(bits, K1)
    # Swap
    temp = temp[4:] + temp[:4]
    # Round 2
    temp = fk(temp, K2)
    # Inverse IP
    cipher = permute(temp, IP_inv)
    print(f"Ciphertext: {cipher}")
    # Decryption (reverse order of subkeys)
    bits = permute(cipher, IP)
    temp = fk(bits, K2)
    temp = temp[4:] + temp[:4]
    temp = fk(temp, K1)
    decrypted = permute(temp, IP_inv)
    print(f"Decrypted: {decrypted}")
    getch()

def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Bubble Sort Result:", arr)
    getch()
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
    print("Selection Sort Result:", arr)
    getch()
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Insertion Sort Result:", arr)
    getch()
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        print("Merge Sort Result:", arr.copy())
        getch()
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = merge(left, right)
    if len(arr) == len(left) + len(right):
        print("Merge Sort Result:", result)
        getch()
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

def quick_sort(arr):
    arr = arr.copy()
    if len(arr) <= 1:
        print("Quick Sort Result:", arr)
        getch()
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    result = quick_sort(less) + [pivot] + quick_sort(greater)
    if len(arr) == len(result):
        print("Quick Sort Result:", result)
        getch()
    return result

def heap_sort(arr):
    import heapq
    arr = arr.copy()
    heapq.heapify(arr)
    result = [heapq.heappop(arr) for _ in range(len(arr))]
    print("Heap Sort Result:", result)
    getch()
    return result

def bucket_sort(arr):
    if not arr:
        print("No numbers entered.")
        getch()
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
    sorted_numbers = [num for sublist in bucket for num in sublist]
    print("Bucket Sort Result:", sorted_numbers)
    getch()
    return sorted_numbers

def comb_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False
    while not sorted_flag:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        sorted_flag = True
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
                print("Comb Sort Current state:", arr)
    print("Comb Sort Result:", arr)
    getch()
    return arr

def radix_sort(arr):
    arr = arr.copy()
    if not arr:
        print("No numbers entered.")
        getch()
        return arr
    def counting_sort(arr, exp):
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
            print("Radix Sort Current state:", output)
        for i in range(n):
            arr[i] = output[i]
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    print("Radix Sort Result:", arr)
    getch()
    return arr

def tree_sort(arr):
    arr = arr.copy()
    if not arr:
        print("No numbers entered.")
        getch()
        return arr
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        def insert(self, value):
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        def inorder(self, result):
            if self.left:
                self.left.inorder(result)
            result.append(self.value)
            if self.right:
                self.right.inorder(result)
    root = Node(arr[0])
    for num in arr[1:]:
        root.insert(num)
    sorted_numbers = []
    root.inorder(sorted_numbers)
    print("Tree Sort Result:", sorted_numbers)
    getch()
    return sorted_numbers

    
    


# searching_functions.py
# Contains searching algorithm implementations for import into test.py

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def jump_search(arr, target):
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if pos < 0 or pos >= len(arr):
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1



def addition(number1, number2, number_base):
    try:
        if number_base == "1":
            result = bin(int(number1, 2) + int(number2, 2))[2:]
        elif number_base == "2":
            result = oct(int(number1, 8) + int(number2, 8))[2:]
        elif number_base == "3":
            result = hex(int(number1, 16) + int(number2, 16))[2:]
        else:
            return "Invalid base"
        print(f"Addition Result: {result}")
        getch()
        return result
    except:
        print("Error")
        getch()
        return "Error"

def subtraction(number1, number2, number_base):
    try:
        if number_base == "1":
            result = bin(int(number1, 2) - int(number2, 2))[2:]
        elif number_base == "2":
            result = oct(int(number1, 8) - int(number2, 8))[2:]
        elif number_base == "3":
            result = hex(int(number1, 16) - int(number2, 16))[2:]
        else:
            return "Invalid base"
        print(f"Subtraction Result: {result}")
        getch()
        return result
    except:
        print("Error")
        getch()
        return "Error"

def multiplication(number1, number2, number_base):
    try:
        if number_base == "1":
            result = bin(int(number1, 2) * int(number2, 2))[2:]
        elif number_base == "2":
            result = oct(int(number1, 8) * int(number2, 8))[2:]
        elif number_base == "3":
            result = hex(int(number1, 16) * int(number2, 16))[2:]
        else:
            return "Invalid base"
        print(f"Multiplication Result: {result}")
        getch()
        return result
    except:
        print("Error")
        getch()
        return "Error"

def division(number1, number2, number_base):
    try:
        if number1 == "0" or number2 == "0":
            return "Cannot divide 0"
        if number_base == "1":
            result = bin(int(number1, 2) // int(number2, 2))[2:]
        elif number_base == "2":
            result = oct(int(number1, 8) // int(number2, 8))[2:]
        elif number_base == "3":
            result = hex(int(number1, 16) // int(number2, 16))[2:]
        else:
            return "Invalid base"
        print(f"Division Result: {result}")
        getch()
        return result
    except:
        print("Error")
        getch()
        return "Error"

def BITWISE(x, y, operation):
    x_str, y_str = x, y
    result = eval(f"0b{x} {operation} 0b{y}")
    max_len = max(len(x_str), len(y_str))
    print(f"{operation}")
    print(x_str.rjust(max_len))
    print(y_str.rjust(max_len))
    print("_" * max_len)
    print(bin(result)[2:].rjust(max_len))
    print()

def BITWISE_OPERATIONS(x, y):
    for op in ["|", "&", "^"]:
        BITWISE(x, y, op)

def chinese_remainder_theorem(n, a):
    total = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        inv = pow(p, -1, n_i)
        total += a_i * inv * p
    return total % prod

# ========== UI SUBMENUS ==========

def arithmetic_ui():
    numeric_base = ["Binary", "Octal", "Hexadecimal"]
    print("1. Binary\n2. Octal\n3. Hexadecimal")
    base = input("Choose numeric base: ")
    if base not in ["1", "2", "3"]:
        print("Invalid base.")
        return
    os.system("cls")
    print(f"Choose operation in {numeric_base[int(base) - 1]}")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    operation = input("Operation: ")
    os.system("cls")
    n1 = input(f"Enter first {numeric_base[int(base) - 1]} number: ")
    n2 = input(f"Enter second {numeric_base[int(base) - 1]} number: ")
    result = {
        "1": addition,
        "2": subtraction,
        "3": multiplication,
        "4": division
    }.get(operation, lambda *args: "Invalid operation")(n1, n2, base)
    print(f"Result: {result}")
    getch()
    input("\nPress Enter to return to menu...")

def bitwise_ui():
    os.system("cls")
    print("Bitwise Operations (Binary only)")
    x = input("Enter first binary: ")
    y = input("Enter second binary: ")
    print()
    BITWISE_OPERATIONS(x, y)
    input("Press Enter to return to menu...")

def chinese_remainder_ui():
    os.system("cls")
    print("Chinese Remainder Theorem Solver")
    k = int(input("Enter number of congruences: "))
    n, a = [], []
    for i in range(k):
        n.append(int(input(f"Enter modulus n[{i+1}]: ")))
        a.append(int(input(f"Enter remainder a[{i+1}]: ")))
    x = chinese_remainder_theorem(n, a)
    print(f"\nThe solution x ≡ {x} mod {reduce(lambda a, b: a*b, n)}")
    for i in range(k):
        print(f"x ≡ {a[i]} mod {n[i]}")
    input("\nPress Enter to return to menu...")

def euler_totient(n):
    result = n
    p = 2
    coprimes = []
    original_n = n
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    # Find coprimes
    from math import gcd
    for k in range(1, original_n + 1):
        if gcd(k, original_n) == 1:
            coprimes.append(k)
    return result, coprimes

def euler_totient_ui():
    os.system("cls")
    print("Euler's Totient Function Calculator")
    n = int(input("Enter a positive integer: "))
    phi, coprimes = euler_totient(n)
    print(f"\nEuler's Totient Function φ({n}) = {phi}")
    print(f"Numbers coprime to {n}: {coprimes}")
    print(f"Total coprime numbers: {len(coprimes)}")
    input("\nPress Enter to return to menu...")

def gcd(a, b):
    # Euclidean algorithm
    while b != 0:
        print(f"{a} = {b}({a // b}) + {a % b}")
        a, b = b, a % b
    return a

def lcm(a, b, gcd_value):
    # LCM using GCD
    return abs(a * b) // gcd_value

def gcd_lcm_ui():
    os.system("cls")
    print("This program lets you input two integers and calculates its GCD and LCM")
    first_number = int(input("Input first number: "))
    second_number = int(input("Input Second number: "))
    GCD = gcd(first_number, second_number)
    LCM = lcm(first_number, second_number, GCD)
    print("GCD: ", GCD)
    print("LCM: ", LCM)
    input("\nPress Enter to return to menu...")

def logical_equivalence():
    os.system("cls")
    print("Logical Equivalence Checker")
    print("Enter two logical expressions using variables (e.g., p, q, r) and operators (~ for NOT, & for AND, | for OR, -> for IMPLIES, <-> for IFF):")
    expr1 = input("Enter first expression: ")
    expr2 = input("Enter second expression: ")
    variables = sorted(set([c for c in expr1 + expr2 if c.isalpha()]))
    if not variables:
        print("No variables found in expressions.")
        return
    print(f"Variables detected: {', '.join(variables)}")
    from itertools import product
    def eval_expr(expr, vals):
        for var, val in zip(variables, vals):
            expr = expr.replace(var, str(val))
        expr = expr.replace("~", " not ")
        expr = expr.replace("&", " and ")
        expr = expr.replace("|", " or ")
        expr = expr.replace("->", " <= ")
        expr = expr.replace("<->", " == ")
        try:
            return eval(expr)
        except Exception as e:
            print(f"Error evaluating: {expr}\n{e}")
            return None
    equivalent = True
    print("\nTruth Table:")
    print(" | ".join(variables) + " | Expr1 | Expr2")
    for vals in product([False, True], repeat=len(variables)):
        res1 = eval_expr(expr1, vals)
        res2 = eval_expr(expr2, vals)
        print(" | ".join(str(int(v)) for v in vals) + f" |   {int(res1)}   |   {int(res2)}")
        if res1 != res2:
            equivalent = False
    if equivalent:
        print("\nThe expressions are logically equivalent.")
    else:
        print("\nThe expressions are NOT logically equivalent.")
    input("\nPress Enter to return to menu...")

def greedy_knapsack():
    os.system('cls')
    print("Fractional Knapsack Problem")
    from math import floor
    class Item:
        def __init__(self, value, weight):
            self.value = value
            self.weight = weight
            self.index = 0
            self.ratio = value / weight if weight != 0 else 0
    n = int(input("Enter number of items: "))
    items = []
    for i in range(n):
        v = int(input(f"Enter value of item {i+1}: "))
        w = int(input(f"Enter weight of item {i+1}: "))
        item = Item(v, w)
        item.index = i
        items.append(item)
    capacity = int(input("Enter capacity of knapsack: "))
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    fractions = [0] * n
    for item in items:
        if capacity <= 0:
            break
        if item.weight <= capacity:
            fractions[item.index] = 1
            total_value += item.value
            capacity -= item.weight
        else:
            fractions[item.index] = capacity / item.weight
            total_value += item.value * fractions[item.index]
            capacity = 0
    print("Item fractions:", [floor(f * 100) for f in fractions])
    print("Total value:", total_value)
    input("\nPress Enter to return to menu...")

def greedy_egyptian_fraction():
    print("Greedy Algorithm: Egyptian Fraction Representation")
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    if numerator == 0 or denominator == 0:
        print("Numerator and denominator must be non-zero.")
        getch()
        return
    result = []
    print(f"\nEgyptian Fraction representation of {numerator}/{denominator}:")
    while numerator != 0:
        x = -(-denominator // numerator)  # Ceiling division
        result.append(x)
        print(f"1/{x}")
        numerator = numerator * x - denominator
        denominator = denominator * x
    print("\nResult as sum:", end=" ")
    print(" + ".join([f"1/{d}" for d in result]))
    getch()

def diffie_hellman_demo():
    print("Diffie-Hellman Key Exchange Demo (Educational)")
    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root modulo p (g): "))
    print("\n-- Alice and Bob choose private keys --")
    a = int(input("Alice's private key (a, secret): "))
    b = int(input("Bob's private key (b, secret): "))
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"\nAlice computes public key: A = g^a mod p = {g}^{a} mod {p} = {A}")
    print(f"Bob computes public key: B = g^b mod p = {g}^{b} mod {p} = {B}")
    print("\n-- Exchange public keys --")
    print(f"Alice sends A = {A} to Bob")
    print(f"Bob sends B = {B} to Alice")
    alice_secret = pow(B, a, p)
    bob_secret = pow(A, b, p)
    print(f"\nAlice computes shared secret: s = B^a mod p = {B}^{a} mod {p} = {alice_secret}")
    print(f"Bob computes shared secret: s = A^b mod p = {A}^{b} mod {p} = {bob_secret}")
    if alice_secret == bob_secret:
        print(f"\nShared secret established! s = {alice_secret}")
    else:
        print("\nError: Shared secrets do not match!")
    getch()

def job_sequencing_ui():
    os.system('cls')
    print("Job Sequencing with Deadlines (Greedy)")
    n = int(input("Enter number of jobs: "))
    jobs = []
    for i in range(n):
        job_id = input(f"Job {i+1} ID: ")
        deadline = int(input(f"Job {i+1} Deadline: "))
        profit = int(input(f"Job {i+1} Profit: "))
        jobs.append((job_id, deadline, profit))
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline
    total_profit = 0
    for job in jobs:
        for d in range(min(max_deadline, job[1]) - 1, -1, -1):
            if slots[d] is None:
                slots[d] = job[0]
                total_profit += job[2]
                break
    print("\nJob sequence:", [j for j in slots if j is not None])
    print("Total profit:", total_profit)
    input("\nPress Enter to return to menu...")

def activity_selection_ui():
    os.system('cls')
    print("Activity Selection Problem (Greedy)")
    n = int(input("Enter number of activities: "))
    activities = []
    for i in range(n):
        start = int(input(f"Activity {i+1} Start time: "))
        finish = int(input(f"Activity {i+1} Finish time: "))
        activities.append((start, finish))
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    for i in range(1, n):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    print("\nSelected activities (start, finish):", selected)
    print("Total activities selected:", len(selected))
    input("\nPress Enter to return to menu...")

def greedy_algorithms_ui():
    while True:
        os.system('cls')
        print("Greedy Algorithms")
        print("1. Fractional Knapsack Problem")
        print("2. Egyptian Fraction Representation")
        print("3. Diffie-Hellman Key Exchange Demo")
        print("4. Job Sequencing with Deadlines")
        print("5. Activity Selection Problem")
        print("6. Back to Main Menu")
        choice = input("Choose an algorithm: ")
        if choice == "1":
            greedy_knapsack()
        elif choice == "2":
            greedy_egyptian_fraction()
        elif choice == "3":
            diffie_hellman_demo()
        elif choice == "4":
            job_sequencing_ui()
        elif choice == "5":
            activity_selection_ui()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")
        input("\nPress Enter to continue...")

def cipher_menu():
    ciphers = [
        "Caesar Cipher", "Vigenère Cipher", "Playfair Cipher", "Vernam Cipher",
        "One Time Pad Cipher", "Hill Cipher", "Rail Fence Cipher", "Columnar Cipher",
        "AES Cipher", "DES Cipher", "SDES Cipher", "RSA Encryption"
    ]
    while True:
        os.system("cls")
        print("=== Cipher Algorithms ===")
        for idx, name in enumerate(ciphers, 1):
            print(f"{idx}. {name}")
        print("13. Back to Main Menu")
        choice = input("Choose Cipher: ")
        match choice:
            case "1": Caesar_cipher()
            case "2": Vigenere_cipher()
            case "3": Playfair_cipher()
            case "4": Vernam_cipher()
            case "5": One_Time_Pad_cipher()
            case "6": Hill_cipher()
            case "7": Rail_fence()
            case "8": Columnar_cipher()
            case "9": AES_cipher()
            case "10": DES_cipher()
            case "11": SDES_cipher()
            case "12": RSA_encryption()
            case "13": break
            case _: input("Invalid choice. Press Enter to try again...")

def number_base_converter():
    os.system('cls')
    number_bases = [ "Binary", "Decimal", "Octal", "Hexadecimal"]
    running = True

    while(running):
        print("This Program takes a number (Binary, Decimal, Octal, or Hexadecimal) \nand converts it to the other three number bases\n1. Binary\n2. Decimal\n3. Octal\n4. Hexadecimal")
        x = input("Choose a number base: ")
        if x not in ["1", "2", "3", "4"]:
            os.system('cls')
            print("Invalid choice.\n")
            continue

        unconverted_number = input(number_bases[int(x) - 1] + " number: ")

        match x:
            case "1":
                based_unconverted_number = "0b" + unconverted_number
                convertedTO_decimal = int(based_unconverted_number, 2)
                convertedTO_octal = oct(convertedTO_decimal)[2:]
                convertedTO_hexadecimal = hex(convertedTO_decimal)[2:].upper()

                os.system('cls')
                print("Original: " + unconverted_number)
                print("Converted to Decimal:", convertedTO_decimal)
                print("Converted to Octal:", convertedTO_octal)
                print("Converted to Hexadecimal:", convertedTO_hexadecimal)

            case "2":
                dec = int(unconverted_number)
                convertedTO_binary = bin(dec)[2:]
                convertedTO_octal = oct(dec)[2:]
                convertedTO_hexadecimal = hex(dec)[2:].upper()

                os.system('cls')
                print("Original:", unconverted_number)
                print("Converted to Binary:", convertedTO_binary)
                print("Converted to Octal:", convertedTO_octal)
                print("Converted to Hexadecimal:", convertedTO_hexadecimal)

            case "3":
                dec = int(unconverted_number, 8)
                convertedTO_binary = bin(dec)[2:]
                convertedTO_decimal = dec
                convertedTO_hexadecimal = hex(dec)[2:].upper()

                os.system('cls')
                print("Original:", unconverted_number)
                print("Converted to Binary:", convertedTO_binary)
                print("Converted to Decimal:", convertedTO_decimal)
                print("Converted to Hexadecimal:", convertedTO_hexadecimal)

            case "4":
                dec = int(unconverted_number, 16)
                convertedTO_binary = bin(dec)[2:]
                convertedTO_decimal = dec
                convertedTO_octal = oct(dec)[2:]

                os.system('cls')
                print("Original:", unconverted_number.upper())
                print("Converted to Binary:", convertedTO_binary)
                print("Converted to Decimal:", convertedTO_decimal)
                print("Converted to Octal:", convertedTO_octal)

        print("=" * 30)
        again = input("Start again? [y/n]: ").lower()
        if again != 'y':
            running = False
            os.system('cls')

def modulo():
    os.system('cls')
    print("This program calculates the modulo of two decimal numbers.")
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    if number2 == 0:
        print("Cannot divide by zero.")
        getch()
        return
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")
    getch()

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def fermats_little_theorem(a, p):
    if p <= 1:
        print(f"p = {p} is not a valid prime.")
        return False
    print(f"Checking Fermat's Little Theorem for a = {a}, p = {p}:")
    print(f"Computing {a}^{p} mod {p} ...")
    result = pow(a, p, p)
    print(f"{a}^{p} mod {p} = {result}")
    print(f"Should be congruent to a = {a} (mod {p})")
    if result == a % p:
        print(f"Result: {result} ≡ {a % p} (mod {p}) — Theorem holds!")
        return True
    else:
        print(f"Result: {result} ≠ {a % p} (mod {p}) — Theorem does NOT hold.")
        return False

def primitive_roots(n):
    if n == 2:
        return [1]
    def is_primitive_root(g, n, phi, factors):
        for factor in factors:
            if pow(g, phi // factor, n) == 1:
                return False
        return True
    phi = n - 1
    factors = list(set(prime_factors(phi)))
    roots = []
    for g in range(2, n):
        if gcd(g, n) == 1 and is_primitive_root(g, n, phi, factors):
            roots.append(g)
    return roots

def trial_division(n):
    divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def number_theory_ui():
    while True:
        os.system('cls')
        print("Number Theory Functions")
        print("1. Prime Factors")
        print("2. Sieve of Eratosthenes")
        print("3. Fermat's Little Theorem")
        print("4. Primitive Roots")
        print("5. Trial Division (find all divisors)")
        print("6. Back to Main Menu")
        choice = input("Choose function: ")
        if choice == "1":
            n = int(input("Enter number to factor: "))
            print("Prime factors:", prime_factors(n))
            getch()
        elif choice == "2":
            n = int(input("Find all primes up to: "))
            print("Primes:", sieve_of_eratosthenes(n))
            getch()
        elif choice == "3":
            a = int(input("Enter a: "))
            p = int(input("Enter p (prime): "))
            result = fermats_little_theorem(a, p)
            print(f"Fermat's Little Theorem holds: {result}")
            getch()
        elif choice == "4":
            n = int(input("Find primitive roots modulo: "))
            print("Primitive roots:", primitive_roots(n))
            getch()
        elif choice == "5":
            n = int(input("Enter number to find divisors: "))
            print("Divisors (excluding 1 and n):", trial_division(n))
            getch()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            getch()
        input("\nPress Enter to continue...")

# ========== ONES' AND TWOS' COMPLEMENT ========== 
def ones_twos_complement_ui():
    os.system('cls')
    print("Ones' and Twos' Complement Calculator")
    while True:
        print("1. Ones' Complement")
        print("2. Twos' Complement")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            binary = input("Enter a binary number: ")
            ones = ''.join('1' if b == '0' else '0' for b in binary)
            print(f"Ones' complement: {ones}")
        elif choice == "2":
            binary = input("Enter a binary number: ")
            ones = ''.join('1' if b == '0' else '0' for b in binary)
            twos = bin(int(ones, 2) + 1)[2:]
            # Pad with zeros if needed
            twos = twos.zfill(len(binary))
            print(f"Twos' complement: {twos}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
        input("\nPress Enter to continue...")

# ========== SET THEORY ========== 
def set_theory_ui():
    os.system('cls')
    print("Set Theory Operations")
    while True:
        print("1. Union")
        print("2. Intersection")
        print("3. Difference (A - B)")
        print("4. Symmetric Difference")
        print("5. Subset Check")
        print("6. Superset Check")
        print("7. Back to Main Menu")
        choice = input("Choose an operation: ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            A = set(input("Enter elements of set A (comma separated): ").split(','))
            B = set(input("Enter elements of set B (comma separated): ").split(','))
            if choice == "1":
                print("A ∪ B =", A | B)
            elif choice == "2":
                print("A ∩ B =", A & B)
            elif choice == "3":
                print("A - B =", A - B)
            elif choice == "4":
                print("A Δ B =", A ^ B)
            elif choice == "5":
                print("A ⊆ B:", A <= B)
            elif choice == "6":
                print("A ⊇ B:", A >= B)
            getch()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")
            getch()
        input("\nPress Enter to continue...")

def tree_factorization_ui():
    os.system('cls')
    print("Tree Factorization (Prime Factor Tree)")
    n = int(input("Enter a positive integer to factor: "))
    def factor_tree(n, indent=""):
        if n <= 1:
            print(indent + str(n))
            return
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"{indent}{n}")
                factor_tree(i, indent + "  ")
                factor_tree(n // i, indent + "  ")
                return
        print(f"{indent}{n}")
    factor_tree(n)
    input("\nPress Enter to return to menu...")

# ========== MAIN MENU ==========
def main():
    running = True
    while running:
        os.system("cls")
        print("MAIN MENU")
        print("1. Arithmetic Operations (Binary/Octal/Hex)")
        print("2. Bitwise Operations")
        print("3. Chinese Remainder Theorem")
        print("4. Cipher Algorithms")
        print("5. Number Base Converter")
        print("6. Euler's Totient Function")
        print("7. GCD and LCM Calculator")
        print("8. Greedy Algorithms")
        print("9. Logical Equivalence")
        print("10. Modulo Calculator")
        print("11. Number Theory Functions")
        print("12. Ones' and Twos' Complement Calculator")
        print("13. Set Theory Operations")
        print("14. Tree Factorization")
        print("15. Sorting Algorithms")
        print("16. Searching Algorithms")
        print("17. Exit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                arithmetic_ui()
            case "2":
                x = input("Input first binary: ")
                y = input("Input second binary: ")
                BITWISE_OPERATIONS(x, y)
                input("Press Enter to continue...")
            case "3":
                k = int(input("Enter number of congruences: "))
                n, a = [], []
                for i in range(k):
                    n_i = int(input(f"Enter modulus n[{i+1}]: "))
                    a_i = int(input(f"Enter remainder a[{i+1}]: "))
                    n.append(n_i)
                    a.append(a_i)
                x = chinese_remainder_theorem(n, a)
                print(f"\nThe solution x ≡ {x} mod {reduce(lambda a, b: a*b, n)}")
                for i in range(k):
                    print(f"x ≡ {a[i]} mod {n[i]}")
                input("\nPress Enter to continue...")
            case "4":
                cipher_menu()
            case "5":
                number_base_converter()
            case "6":
                euler_totient_ui()
            case "7":
                gcd_lcm_ui()
            case "8":
                greedy_algorithms_ui()
            case "9":
                logical_equivalence()
            case "10":
                modulo()
            case "11":
                number_theory_ui()
            case "12":
                ones_twos_complement_ui()
            case "13":
                set_theory_ui()
            case "14":
                tree_factorization_ui()
            case "15":
                sorting_ui()
            case "16":
                searching_ui()
            case "17":
                running = False
            case _:
                print("Invalid option")
                input("Press Enter to continue...")

def sorting_ui():
    os.system('cls')
    print("Sorting Algorithms")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Bucket Sort")
    print("8. Comb Sort")
    print("9. Radix Sort")
    print("10. Tree Sort")
    print("11. Back to Main Menu")
    while True:
        choice = input("Choose a sorting algorithm: ")
        if choice == "11":
            break
        arr = input("Enter numbers separated by spaces: ")
        arr = [int(x) for x in arr.split()]
        if choice == "1":
            bubble_sort(arr)
        elif choice == "2":
            selection_sort(arr)
        elif choice == "3":
            insertion_sort(arr)
        elif choice == "4":
            merge_sort(arr)
        elif choice == "5":
            quick_sort(arr)
        elif choice == "6":
            heap_sort(arr)
        elif choice == "7":
            bucket_sort(arr)
        elif choice == "8":
            comb_sort(arr)
        elif choice == "9":
            radix_sort(arr)
        elif choice == "10":
            tree_sort(arr)
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")
        os.system('cls')
        print("Sorting Algorithms")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        print("7. Bucket Sort")
        print("8. Comb Sort")
        print("9. Radix Sort")
        print("10. Tree Sort")
        print("11. Back to Main Menu")

def searching_ui():
    os.system('cls')
    print("Searching Algorithms")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Jump Search")
    print("4. Interpolation Search")
    print("5. Back to Main Menu")
    while True:
        choice = input("Choose a searching algorithm: ")
        if choice == "5":
            break
        arr = input("Enter sorted numbers separated by spaces: ")
        arr = [int(x) for x in arr.split()]
        target = int(input("Enter the target value: "))
        if choice == "1":
            linear_search(arr, target)
        elif choice == "2":
            binary_search(arr, target)
        elif choice == "3":
            jump_search(arr, target)
        elif choice == "4":
            interpolation_search(arr, target)
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")
        os.system('cls')
        print("Searching Algorithms")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Jump Search")
        print("4. Interpolation Search")
        print("5. Back to Main Menu")

def getch():
    try:
        import msvcrt
        msvcrt.getch()
    except ImportError:
        input("Press Enter to continue...")

# if __name__ == "__test__":
#     main()
main()