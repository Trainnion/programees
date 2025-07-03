import os
import time
import random

# region Helper Functions
# Helper function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Helper function to simulate a delay (in seconds)
def sleep(seconds):
    time.sleep(seconds)
# endregion

#region ciphers
class Ciphers:
    """Encrypts and decrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print(">> Cipher Station Activated!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\nChoose Mode:")
        modes = [("Encrypt", self.run_menu_encrypt), ("Decrypt", self.run_menu_decrypt)]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (number): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("Invalid choice, try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\nSelect a cipher to encrypt with:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_encrypt),
            ("Playfair Cipher", self.playfair_encrypt),
            ("Hill Cipher", self.hill_encrypt),
            ("Columnar Cipher", self.columnar_encrypt),
            ("Caesar Cipher", self.caesar_encrypt),
            ("Vernam Cipher", self.vernam_encrypt),
            ("Vigenère Cipher", self.vigenere_encrypt),
            ("One-Time Pad Cipher", self.one_time_pad_encrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("Invalid choice, try again.")

    def run_menu_decrypt(self):
        print("\nSelect a cipher to decrypt with:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_decrypt),
            ("Playfair Cipher", self.playfair_decrypt),
            ("Hill Cipher", self.hill_decrypt),
            ("Columnar Cipher", self.columnar_decrypt),
            ("Caesar Cipher", self.caesar_decrypt),
            ("Vernam Cipher", self.vernam_decrypt),
            ("Vigenère Cipher", self.vigenere_decrypt),
            ("One-Time Pad Cipher", self.one_time_pad_decrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("Invalid choice, try again.")

    # Caesar Encrypt and Decrypt
    def caesar_encrypt(self):
        text = input("Type your message: ")
        shift = int(input("Shift positions (1–25): "))
        encrypted = ""
        print("\n[Encrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} -> {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\nEncrypted → {encrypted}")

    def caesar_decrypt(self):
        text = input("Type encrypted message: ")
        shift = int(input("Shift positions used (1–25): "))
        decrypted = ""
        print("\n[Decrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} -> {shifted}")
                decrypted += shifted
            else:
                decrypted += char
        print(f"\nDecrypted → {decrypted}")

    # Vigenere Encrypt and Decrypt
    def vigenere_encrypt(self):
        text = input("Enter the text: ")
        key = input("Enter the keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[Encrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} + {key_char} -> {encrypted}")
                result += encrypted
            else:
                result += char
        print(f"\nEncrypted → {result}")

    def vigenere_decrypt(self):
        text = input("Enter encrypted text: ")
        key = input("Enter keyword used: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[Decrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                decrypted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} - {key_char} -> {decrypted}")
                result += decrypted
            else:
                result += char
        print(f"\nDecrypted → {result}")

    def playfair_encrypt(self):
        text = input("Message to encrypt: ")
        keyword = input("Keyword to construct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Pairs]")
        for i in range(0, len(prepared), 2):
            a, b = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, a, b)
            print(f"{a}{b} -> {cipher_pair}")
            encrypted += cipher_pair
        print(f"\nCiphertext → {encrypted}")

    def playfair_decrypt(self):
        text = input("Ciphertext to decrypt: ")
        keyword = input("Keyword to reconstruct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n[Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Pairs]")
        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, a, b)
            print(f"{a}{b} -> {plain_pair}")
            decrypted += plain_pair
        print(f"\nDecrypted Text → {decrypted}")


    def _find_position(self, matrix, ch):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == ch:
                    return i, j
        raise ValueError(f"Character {ch} not found in matrix")


    def _playfair_encrypt_pair(self, matrix, a, b):
        row1, col1 = self._find_position(matrix, a)
        row2, col2 = self._find_position(matrix, b)

        if row1 == row2:
            return (
                matrix[row1][(col1 + 1) % 5] +
                matrix[row2][(col2 + 1) % 5]
            )
        elif col1 == col2:
            return (
                matrix[(row1 + 1) % 5][col1] +
                matrix[(row2 + 1) % 5][col2]
            )
        else:
            return (
                matrix[row1][col2] +
                matrix[row2][col1]
            )


    def _playfair_decrypt_pair(self, matrix, a, b):
        row1, col1 = self._find_position(matrix, a)
        row2, col2 = self._find_position(matrix, b)

        if row1 == row2:
            return (
                matrix[row1][(col1 - 1) % 5] +
                matrix[row2][(col2 - 1) % 5]
            )
        elif col1 == col2:
            return (
                matrix[(row1 - 1) % 5][col1] +
                matrix[(row2 - 1) % 5][col2]
            )
        else:
            return (
                matrix[row1][col2] +
                matrix[row2][col1]
            )


    def _generate_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        seen = set()
        seq = []
        for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if ch.isalpha() and ch not in seen:
                seen.add(ch)
                seq.append(ch)
        return [seq[i:i+5] for i in range(0, 25, 5)]


    def _prepare_playfair_text(self, text):
        s = text.upper().replace("J", "I")
        s = "".join(ch for ch in s if ch.isalpha())
        out = ""
        i = 0
        while i < len(s):
            a = s[i]
            b = s[i + 1] if i + 1 < len(s) else "X"
            if a == b:
                out += a + "X"
                i += 1
            else:
                out += a + b
                i += 2
        if len(out) % 2 == 1:
            out += "X"
        return out



    # Vernam encrypt/decrypt (same operation)
    def vernam_encrypt(self):
        text = input("Input text: ")
        key = input("Key (same length as text): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nEncrypted: {result}")
        print(f"As hex: {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("Encrypted text: ")
        key = input("Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[Decrypting]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nDecrypted: {result}")
        print(f"As hex: {result.encode().hex()}")

    # One-Time Pad encrypt/decrypt (same operation)
    def one_time_pad_encrypt(self):
        text = input("Message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n[Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {ord(c) ^ k}")
        print(f"Generated key (hex): {key.hex()}")
        print(f"Encrypted output (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("Encrypted message (hex): ")
        key_hex = input("Key used (hex): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except Exception:
            print("Invalid hex input.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n[Decrypting]")
        for e, k in zip(encrypted, key):
            print(f"{e} ^ {k} = {e ^ k}")
        print(f"\nDecrypted message → {decrypted}")

    # Hill cipher encrypt/decrypt
    def hill_encrypt(self):
        text = input("Text to encode: ")
        key_input = input("3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("Expected 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("Invalid matrix input.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[Encrypting]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * Col {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\nMatrix used:")
        for row in matrix:
            print(row)
        print(f"Hill Cipher Encrypted → {result}")

    def hill_decrypt(self):
        text = input("Encrypted text: ")
        key_input = input("3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("Expected 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("Invalid matrix input.")
            return

        # Calculate modular inverse matrix mod 26
        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("Matrix not invertible mod 26. Can't decrypt.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[Decrypting]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(inv_matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * InvCol {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\nInverse matrix:")
        for row in inv_matrix:
            print(row)
        print(f"Hill Cipher Decrypted → {result}")

    def _hill_matrix_inverse(self, matrix):
        # Calculate determinant mod 26
        def det3(m):
            return (m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
                    - m[0][2]*m[1][1]*m[2][0] - m[0][1]*m[1][0]*m[2][2] - m[0][0]*m[1][2]*m[2][1]) % 26
        det = det3(matrix)
        # Find modular inverse of determinant mod 26
        det_inv = self._modular_inverse(det, 26)
        if det_inv is None:
            return None
        # Calculate matrix of cofactors
        cof = [[0]*3 for _ in range(3)]
        cof[0][0] = (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) % 26
        cof[0][1] = -(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) % 26
        cof[0][2] = (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]) % 26
        cof[1][0] = -(matrix[0][1]*matrix[2][2] - matrix[0][2]*matrix[2][1]) % 26
        cof[1][1] = (matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0]) % 26
        cof[1][2] = -(matrix[0][0]*matrix[2][1] - matrix[0][1]*matrix[2][0]) % 26
        cof[2][0] = (matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]) % 26
        cof[2][1] = -(matrix[0][0]*matrix[1][2] - matrix[0][2]*matrix[1][0]) % 26
        cof[2][2] = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
        # Transpose cofactor matrix to get adjugate
        adj = [[cof[j][i] % 26 for j in range(3)] for i in range(3)]
        # Multiply by determinant inverse mod 26
        inv = [[(adj[i][j] * det_inv) % 26 for j in range(3)] for i in range(3)]
        return inv

    def _modular_inverse(self, a, m):
        # Extended Euclidean Algorithm for modular inverse
        a = a % m
        if a == 0:
            return None
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Rail Fence encrypt/decrypt
    def rail_fence_encrypt(self):
        text = input("Message: ")
        if any(c.isdigit() for c in text):
            print("Digits not allowed.")
            return
        try:
            rails = int(input("Rails (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("Invalid rails.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n[Encrypting Zigzag]")
        for char in text:
            print(f"{char} -> Rail {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        encrypted = ''.join(fence)
        print(f"\nEncrypted → {encrypted}")

    def rail_fence_decrypt(self):
        ciphertext = input("Ciphertext: ")
        try:
            rails = int(input("Rails used (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("Invalid rails.")
            return

        n = len(ciphertext)
        fence = [['' for _ in range(n)] for _ in range(rails)]
        rail, direction = 0, 1
        for i in range(n):
            fence[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

        index = 0
        print("\n[Marking positions]")
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*' and index < n:
                    fence[r][c] = ciphertext[index]
                    print(f"Placing {ciphertext[index]} at rail {r}, pos {c}")
                    index += 1

        result = []
        rail, direction = 0, 1
        print("\n[Reading zigzag]")
        for i in range(n):
            result.append(fence[rail][i])
            print(f"Rail {rail}, pos {i} → {fence[rail][i]}")
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        decrypted = ''.join(result)
        print(f"\nDecrypted → {decrypted}")

    # Columnar encrypt/decrypt
    def columnar_encrypt(self):
        text = input("Plaintext: ").replace(" ", "")
        key = input("Keyword: ").lower()
        n = len(key)
        matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]
        while len(matrix[-1]) < n:
            matrix[-1].append('x')
        print("\n[Matrix]")
        for row in matrix:
            print("".join(row))

        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]
        print(f"Order of columns by key: {order}")

        result = ""
        for col_num in sorted(order):
            col_idx = order.index(col_num)
            col_text = "".join(matrix[row][col_idx] for row in range(len(matrix)))
            print(f"Column {col_idx} ({key[col_idx]}) -> {col_text}")
            result += col_text
        print(f"\nEncrypted → {result}")

    def columnar_decrypt(self):
        ciphertext = input("Ciphertext: ")
        key = input("Keyword: ").lower()
        n = len(key)
        num_rows = len(ciphertext) // n
        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]

        # Number of chars per column
        cols = {}
        start = 0
        for col_num in sorted(order):
            length = num_rows
            cols[col_num] = ciphertext[start:start+length]
            start += length
        print("\n[Columns extracted]")
        for k, v in cols.items():
            print(f"Col {k}: {v}")

        # Rebuild matrix by key order
        matrix = [[""]*n for _ in range(num_rows)]
        for col_idx, col_num in enumerate(order):
            col_text = cols[col_num]
            for row in range(num_rows):
                matrix[row][col_idx] = col_text[row]

        print("\n[Reconstructed matrix]")
        for row in matrix:
            print("".join(row))

        result = "".join(matrix[row][col] for row in range(num_rows) for col in range(n))
        print(f"\nDecrypted → {result}")
#endregion ciphers

# region GCD & LCM
class GCD_LCM:
    """Performs GCD and LCM calculations using classic number theory."""

    def __init__(self):
        clear_screen()
        print(">> Welcome to the GCD & LCM Utility!")
        sleep(1)
        self.start()

    def start(self):

        print("\nWhich operation do you need?")
        print(" 1. Find the GCD (Greatest Common Divisor)")
        print(" 2. Find the LCM (Least Common Multiple)")
        print(" 3. Exit")
        choice = input("Choose (1, 2 or 3): ").strip()
        if choice == '1':
            self.gcd()
        elif choice == '2':
            self.lcm()
        elif choice == '3':
            print("Goodbye!")
            return
        else:
            print("⚠️ That’s not a valid option. Try again.")

    def gcd(self):
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            x, y = a, b
            print(f"Finding GCD of {a} and {b}...\n")
            while y != 0:
                remainder = x % y
                print(f"{x} % {y} = {remainder}")
                x, y = y, remainder
            print(f"→ GCD({a}, {b}) = {x}")
        except ValueError:
            print("⚠️ Invalid input. Use integers only.")

    def lcm(self):
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            print(f"Calculating LCM of {a} and {b}...")
            x, y = a, b
            while y != 0:
                x, y = y, x % y
            gcd = x
            print(f"GCD = {gcd}")
            lcm = (a * b) // gcd
            print(f"→ LCM({a}, {b}) = {lcm}")
        except ValueError:
            print("⚠️ Please enter valid integers.")
# endregion

# region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print(">> Set Theory Function Activated!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("Welcome to the Set Theory Console!")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"Enter the elements of set {label} (space-separated): ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\nYou entered the following sets:")
        print(f"Set A → {self.set_a}")
        print(f"Set B → {self.set_b}")

    def compute_results(self):
        print("\nInitiating set operations...\n")
        sleep(1)

        operations = [
            ("Union", self._union),
            ("Intersection", self._intersection),
            ("Difference (A - B)", self._difference),
            ("Subset Check", self._subset_check),
            ("Equality Check", self._equality_check),
        ]
        random.shuffle(operations)  # Shuffle operation order

        for label, func in operations:
            print(f"--- {label} ---")
            func()
            print()

    def _union(self):
        result = self.set_a.copy()
        for item in self.set_b:
            if item not in result:
                print(f"Adding {item} to union set")
                result.add(item)
            else:
                print(f"{item} already present in union")
        print(f"→ Union Result: {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"{item} found in both sets")
                result.add(item)
            else:
                print(f"{item} is unique to A")
        print(f"→ Intersection Result: {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"Keeping {item} (not in B)")
                result.add(item)
            else:
                print(f"Discarding {item} (exists in B)")
        print(f"→ A - B Result: {result}")

    def _subset_check(self):
        print("Checking if A is a subset of B...")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"{item} is missing in B → Not a subset")
                print("→ Result: No")
                return
            else:
                print(f"{item} found in B")
        print("→ Result: Yes (A ⊆ B)")

    def _equality_check(self):
        print("Validating if sets A and B are equal...")
        all_items = self.set_a.union(self.set_b)
        same = True
        for item in all_items:
            in_a = item in self.set_a
            in_b = item in self.set_b
            symbol = "✓" if in_a and in_b else "✗"
            print(f"{symbol} {item}: A={in_a}, B={in_b}")
            if in_a != in_b:
                same = False
        print(f"→ Result: {'Yes' if same else 'No'} (A == B)")
# endregion set theory

#region sorting
class Sorting:
    """A simple class for sorting algorithms."""

    def __init__(self):
        clear_screen()
        print("⏳ Initializing Sorting Module...")
        sleep(1)
        self.start()

    def start(self):
        methods = [
            ("Quick Sort", self.quick_sort),
            ("Tree Sort", self.tree_sort),
            ("Insertion Sort", self.insertion_sort),
            ("Merge Sort", self.merge_sort),
            ("Bubble Sort", self.bubble_sort),
            ("Bucket Sort", self.bucket_sort),
            ("Comb Sort", self.comb_sort),
            ("Shell Sort", self.shell_sort),
            ("Radix Sort", self.radix_sort),
            ("Selection Sort", self.selection_sort),
        ]

        clear_screen()
        print("\n📊 Available Sorting Algorithms:")
        for idx, (name, _) in enumerate(methods, 1):
            print(f" {idx}. {name}")
        print(" 0. Back to Main Menu")

        try:
            choice = int(input("\n🔢 Select an option: "))
            if choice == 0:
                return
            _, func = methods[choice - 1]
            func()
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Please select a valid number.")
            sleep(1.5)

    def bubble_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔁 Performing Bubble Sort...")
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(f"Swapping {arr[j]} and {arr[j+1]} →", end=" ")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(arr)
                    sleep(0.01)
        print(f"✅ Sorted Result: {arr}")

    def selection_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔍 Performing Selection Sort...")
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"Step {i+1}: {arr}")
            sleep(0.01)
        print(f"✅ Sorted Result: {arr}")

    def insertion_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n📥 Performing Insertion Sort...")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"Step {i}: {arr}")
            sleep(0.01)
        print(f"✅ Sorted Result: {arr}")

    def merge_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔗 Performing Merge Sort...")
        self._merge_sort(arr)
        print(f"✅ Sorted Result: {arr}")

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            print(f"Split: {L} | {R}")
            self._merge_sort(L)
            self._merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
            print(f"Merged: {arr}")
            sleep(0.05)

    def quick_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n⚡ Performing Quick Sort...")
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"✅ Sorted Result: {arr}")

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        print(f"Pivot: {pivot}")
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(f"Swapped: {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        if not arr:
            print("⚠️ Empty list")
            return
        print("\n🪣 Performing Bucket Sort...")
        bucket_count = 10
        max_val, min_val = max(arr), min(arr)
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            idx = int((num - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[idx].append(num)
        for i, b in enumerate(buckets):
            b.sort()
            print(f"Bucket {i}: {b}")
        sorted_arr = [num for b in buckets for num in b]
        print(f"✅ Sorted Result: {sorted_arr}")

    def shell_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔩 Performing Shell Sort...")
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"Gap {gap}: {arr}")
            gap //= 2
        print(f"✅ Sorted Result: {arr}")

    def comb_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🧹 Performing Comb Sort...")
        gap = len(arr)
        shrink = 1.3
        sorted_flag = False
        while gap > 1 or not sorted_flag:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            sorted_flag = True
            for i in range(len(arr) - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_flag = False
                    print(f"Swapped: {arr}")
        print(f"✅ Sorted Result: {arr}")

    def radix_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔢 Performing Radix Sort...")
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort(arr, exp)
            print(f"Exp {exp}: {arr}")
            exp *= 10
        print(f"✅ Sorted Result: {arr}")

    def _counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in arr:
            index = (i // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in reversed(arr):
            index = (i // exp) % 10
            output[count[index] - 1] = i
            count[index] -= 1
        for i in range(n):
            arr[i] = output[i]

    def tree_sort(self):
        print("\n🌳 Tree Sort not yet implemented. (Placeholder)")
#endregion sorting

# region conversion
class Conversion:
    """A flexible number base converter with detailed, step-by-step tracing."""

    def __init__(self):
        clear_screen()
        print("🚀 Welcome to the Number Base Conversion Hub!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhat kind of number magic do you want to perform today?\n")

        options = [
            ("Decimal → Binary", self.decimal_to_binary),
            ("Binary → Decimal", self.binary_to_decimal),
            ("Decimal → Octal", self.decimal_to_octal),
            ("Decimal → Hexadecimal", self.decimal_to_hex),
            ("Octal → Decimal", self.octal_to_decimal),
            ("Hexadecimal → Decimal", self.hex_to_decimal),
            ("Binary → Octal", self.binary_to_octal),
            ("Binary → Hexadecimal", self.binary_to_hex),
            ("Octal → Binary", self.octal_to_binary),
            ("Octal → Hexadecimal", self.octal_to_hex),
            ("Hexadecimal → Binary", self.hex_to_binary),
            ("Hexadecimal → Octal", self.hex_to_octal),
        ]

        random.shuffle(options)

        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")

        try:
            choice = int(input("\nPick a number from above to get started: "))
            if 1 <= choice <= 12:
                print()
                options[choice - 1][1]()
            else:
                print("\n😅 Oops, that number’s not on the list. Try again!")
        except ValueError:
            print("\n😬 That doesn’t look like a number. Please enter digits only.")

    def decimal_to_binary(self):
        num = int(input("Type in a decimal number and watch it become binary: "))
        self._decimal_to_base(num, 2, "Binary")

    def binary_to_decimal(self):
        binary = input("Drop a binary number here (only 0s and 1s): ")
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("Let's break it down step-by-step:\n" + "\n".join(steps))
        print(f"→ That’s {int(binary, 2)} in decimal!")

    def decimal_to_octal(self):
        num = int(input("Enter a decimal number, and I'll convert it to octal: "))
        self._decimal_to_base(num, 8, "Octal")

    def decimal_to_hex(self):
        num = int(input("Pop in a decimal number, and let's make it hexadecimal: "))
        self._decimal_to_base(num, 16, "Hexadecimal")

    def octal_to_decimal(self):
        octal = input("Give me an octal number (digits 0–7): ")
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("Here's how that octal number adds up:\n" + "\n".join(steps))
        print(f"→ In decimal, that’s {int(octal, 8)}!")

    def hex_to_decimal(self):
        hex_str = input("Enter a hexadecimal number (0–9, A–F): ").upper()
        digits = "0123456789ABCDEF"
        steps = [f"{char} × 16^{i} = {digits.index(char)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("Let’s decode it together:\n" + "\n".join(steps))
        print(f"→ Converted to decimal: {int(hex_str, 16)}!")

    def binary_to_octal(self):
        binary = input("Type a binary number, and I'll turn it into octal: ")
        dec = int(binary, 2)
        print(f"First, let's see what that is in decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def binary_to_hex(self):
        binary = input("Pop a binary number here, and I’ll convert it to hex: ")
        dec = int(binary, 2)
        print(f"Step one, decimal version is: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def octal_to_binary(self):
        octal = input("Give me an octal number, I’ll flip it to binary: ")
        dec = int(octal, 8)
        print(f"Let's convert that to decimal first: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def octal_to_hex(self):
        octal = input("Enter an octal number, and I'll give you the hex: ")
        dec = int(octal, 8)
        print(f"Decimal form first: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def hex_to_binary(self):
        hex_str = input("Drop a hex number here, and I'll show you binary: ")
        dec = int(hex_str, 16)
        print(f"Decimal equivalent is: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def hex_to_octal(self):
        hex_str = input("Type a hex number, and I’ll convert it to octal: ")
        dec = int(hex_str, 16)
        print(f"Step one, decimal is: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def _decimal_to_base(self, decimal, base, label):
        digits = "0123456789ABCDEF"
        original = decimal
        steps = []
        if decimal == 0:
            print(f"Conversion Steps:\n{decimal} is zero, so {label} is 0.")
            print(f"→ {label}: 0")
            return
        while decimal > 0:
            r = decimal % base
            q = decimal // base
            step = f"{decimal} ÷ {base} = {q} remainder {r}"
            if base == 16:
                step += f" (which is '{digits[r]}')"
            steps.append(step)
            decimal = q
        print("Step-by-step breakdown:\n" + "\n".join(reversed(steps)))
        if base == 2:
            converted = bin(original)[2:]
        elif base == 8:
            converted = oct(original)[2:]
        else:
            converted = hex(original)[2:].upper()
        print(f"🎉 And here’s the final {label} value: {converted}")
# endregion conversion

# region Searching
class Searching:
    """A tool to demonstrate various search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("🔍 Welcome to the Interactive Search Tool!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\nWhich search adventure shall we take on today?")
        print(" 1. Interpolation Search")
        print(" 2. Linear Search")
        print(" 3. Binary Search")
        print(" 4. Ternary Search")
        print(" 5. Jump Search")
        print(" 6. Interval Search")

        try:
            choice = int(input("Pick a number (1–3) to dive in: "))
        except ValueError:
            print("⚠️ Oops! That’s not a number between 1 and 3. Try again.")
            return self.menu()

        if choice == 1:
            self.interpolation_search()
        elif choice == 2:
            self.linear_search()
        elif choice == 3:
            self.binary_search()
        elif choice == 4:
            self.ternary_search()
        elif choice == 5:
            self.jump_search()
        elif choice == 6:
            self.interval_search()
        else:
            print("⚠️ That choice isn’t on the menu. Give it another go!")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\nEnter your list of numbers (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"🔢 Here’s the sorted array we’ll work with: {values}")
            target = int(input("🔍 Now, what number are you searching for? "))
            return values, target
        except ValueError:
            print("⚠️ Hmmm, looks like some input wasn’t an integer. Try again please!")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔎 Starting linear search…\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"Checking index {idx} — value: {val}")
            if val == target:
                print(f"🎉 Got it! {target} found at index {idx}.")
                return
            print("→ Nope, not here. Moving on…")
        print(f"😞 Sorry, {target} isn’t in this list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting binary search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Step {step}: left = {left}, right = {right}, mid = {mid} (value: {arr[mid]})")
            step += 1

            if arr[mid] == target:
                print(f"🎉 Found {target} right here at index {mid}!")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} is less than {target}, searching the right half...")
                left = mid + 1
            else:
                print(f"{arr[mid]} is greater than {target}, searching the left half...")
                right = mid - 1

        print(f"😞 No luck! {target} isn’t in the array.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting interpolation search…\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎉 Found {target} at index {low}!")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"Step {step}: low = {low}, high = {high}, pos = {pos} (value: {arr[pos]})")
            step += 1

            if arr[pos] == target:
                print(f"🎯 Bullseye! {target} found at index {pos}.")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} is less than {target}, shifting right...")
                low = pos + 1
            else:
                print(f"{arr[pos]} is greater than {target}, shifting left...")
                high = pos - 1

        print(f"😔 {target} wasn’t found this time.")
    
    def ternary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔍 Launching Ternary Search...\n")
        sleep(0.5)
        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            print(f"Step {step}: mid1={mid1}({arr[mid1]}), mid2={mid2}({arr[mid2]})")
            step += 1
            if arr[mid1] == target:
                print(f"🎯 Found at index {mid1}")
                return
            if arr[mid2] == target:
                print(f"🎯 Found at index {mid2}")
                return
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        print(f"❌ {target} not discovered.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🏃 Executing Jump Search...\n")
        sleep(0.5)
        import math
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n) - 1] < target:
            print(f"Jumping from {prev} to {min(step, n) - 1}")
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                print("🚫 Overshot the list!")
                return
        for i in range(prev, min(step, n)):
            print(f"Scanning index {i}: {arr[i]}")
            if arr[i] == target:
                print(f"🎯 Found at index {i}")
                return
        print(f"❌ {target} not found after jumping.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📈 Interval (Exponential) Search Engaged...\n")
        sleep(0.5)
        if len(arr) == 0:
            print("📭 Empty array!")
            return
        if arr[0] == target:
            print("🎯 Found at index 0")
            return
        index = 1
        while index < len(arr) and arr[index] <= target:
            print(f"Interval check: index={index}, value={arr[index]}")
            index *= 2
        left = index // 2
        right = min(index, len(arr) - 1)
        print(f"🔎 Binary search between {left} and {right}")
        while left <= right:
            mid = (left + right) // 2
            print(f"Checking mid={mid}: {arr[mid]}")
            if arr[mid] == target:
                print(f"🎯 Found at index {mid}")
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"❌ {target} not located in exponential search window.")

# endregion

# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("🔢 Welcome to the Prime Numbers Module!")
        sleep(1)
        self.start()

    def start(self):
        print("\nPick something to explore:")
        print(" 1. Is it prime?")
        print(" 2. Generate primes (Sieve of Eratosthenes)")
        print(" 3. Find prime factors")
        print(" 4. Use Fermat's Little Theorem")
        print(" 5. Discover primitive roots")
        try:
            choice = int(input("Your choice (1–5): "))
        except ValueError:
            print("⚠️ That didn’t look like a number. Try again!")
            return

        match choice:
            case 1: self.check_prime()
            case 2: self.sieve()
            case 3: self.prime_factors()
            case 4: self.fermats()
            case 5: self.primitive_roots()
            case _: print("⚠️ That's not on the list. Try again.")

    def check_prime(self):
        try:
            n = int(input("\nEnter a number to check: "))
        except ValueError:
            print("⚠️ Please enter a valid integer.")
            return

        if n < 2:
            print(f"❌ Nope! {n} is not a prime number.")
            return

        for i in range(2, int(n ** 0.5) + 1):
            print(f"Testing: {n} ÷ {i} → remainder: {n % i}")
            if n % i == 0:
                print(f"⛔ Divisible by {i}. That means {n} is not prime.")
                return

        print(f"✅ Yes! {n} is a prime number.")

    @staticmethod
    def _check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors(self):
        try:
            n = int(input("\nEnter a number to factor: "))
        except ValueError:
            print("⚠️ That wasn’t a number.")
            return

        original = n
        factors = []

        print(f"\n🧩 Starting factorization of {original}:")

        while n % 2 == 0:
            print(f"{n} is even → adding 2 to the list.")
            factors.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"{n} is divisible by {i} → adding {i}")
                factors.append(i)
                n //= i
            i += 2

        if n > 2:
            print(f"🔹 Leftover prime: {n}")
            factors.append(n)

        print(f"\n✔️ Prime factors of {original}: {factors}")

    def sieve(self):
        print("\n🔬 Sieve of Eratosthenes — find all primes in a range.")
        try:
            start = int(input("Start from (inclusive): "))
            end = int(input("End at (exclusive): "))
        except ValueError:
            print("⚠️ Numbers only, please.")
            return

        if end <= start:
            print("⚠️ Make sure the end is greater than the start.")
            return

        print(f"\nCrunching primes from {start} to {end}...")
        primes = [i for i in range(start, end) if self._check_prime(i)]

        print(f"\n✅ Found these primes in range {start} to {end}:")
        print(primes)

    def fermats(self):
        print("\n📐 Fermat’s Little Theorem: a^(p−1) ≡ 1 mod p, for prime p.")
        try:
            a = int(input("Enter value for a: "))
            k = int(input("Enter exponent k: "))
            p = int(input("Enter a prime number p: "))
        except ValueError:
            print("⚠️ Only numeric inputs are allowed.")
            return

        if not self._check_prime(p):
            print("⚠️ That p isn’t prime. The theorem needs a prime!")
            return

        result = pow(a, k, p)
        print(f"\n✨ Result: {a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\n📊 Primitive Roots — testing and listing all for prime p.")
        try:
            p = int(input("Enter a prime number p: "))
            a = int(input("Enter a number to test as a primitive root: "))
        except ValueError:
            print("⚠️ Numbers only!")
            return

        if p <= 0 or a <= 0:
            print("⚠️ Positive integers only.")
            return

        if not self._check_prime(p):
            print("⚠️ You must use a prime number for p.")
            return

        required = set(range(1, p))
        actual = set(pow(a, k, p) for k in range(1, p))

        if actual == required:
            print(f"🎉 Yes! {a} is a primitive root modulo {p}.")
        else:
            print(f"🚫 Nope, {a} is not a primitive root modulo {p}.")

        print("\n🧮 Gathering all primitive roots of", p)
        roots = []
        for g in range(2, p):
            if set(pow(g, k, p) for k in range(1, p)) == required:
                roots.append(g)

        print(f"\n📋 Primitive roots of {p}:")
        print(roots)
# endregion

# region Main Program Loop
def main():
    modules = [
        Ciphers,
        GCD_LCM,
        SetTheory,
        Sorting,
        Conversion,
        Searching,
        Prime,
    ]

    while True:
        clear_screen()
        random.shuffle(modules)
        print("🧠 Jason Hangalay’s Algorithm Nexus: System Calibration Complete… 🧠\n")
        print(random.choice([
            "What logic stream shall we decode today?",
            "Choose your next problem-solving quest:",
            "Dive into one of the modules below:",
            "Where shall our algorithms take us next?",
        ]))

        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. ⚙️ {module.__name__}")
        print(" 0. 🛑 Close Program")

        try:
            choice = int(input("\n📊 Make your selection (0 to exit): "))
        except ValueError:
            print(random.choice([
                "\n🚫 That wasn’t a number. Let's fix that.",
                "\n❌ Digits only. Try again.",
                "\n⚠️ Invalid input detected. Use numbers only.",
            ]))
            sleep(1.5)
            continue

        if choice == 0:
            print(random.choice([
                "\n👋 Farewell! See you on the next logic loop!",
                "\n🔚 Shutting down. Keep thinking critically!",
                "\n🌟 You’ve unlocked knowledge. Come back soon!",
            ]))
            break

        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            while True:
                clear_screen()
                print(f"🔬 Now running: {selected_module.__name__} Module...\n")
                selected_module()

                again = input(random.choice([
                    "\n🔁 Run this module again? (y/N): ",
                    "\n♻️ Want to give it another shot? (y/N): ",
                    "\n🔄 Replay this module? (y/N): ",
                ])).strip().lower()

                if again != 'y':
                    break
        else:
            print(random.choice([
                "\n⚠️ That number isn't linked to a module.",
                "\n🚫 Not a valid option. Try again.",
                "\n❗ Please pick from the available options.",
            ]))
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion

