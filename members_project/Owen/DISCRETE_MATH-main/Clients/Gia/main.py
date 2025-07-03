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

# region ciphers
class Ciphers:
    """Encrypts and decrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print("🛡️ Cipher Station Activated!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\n🔐 Choose Mode:")
        modes = [("Encrypt 🔒", self.run_menu_encrypt), ("Decrypt 🔓", self.run_menu_decrypt)]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (enter number): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice — please try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\n🧩 Select a cipher to Encrypt with:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_encrypt),
            ("Playfair Cipher", self.playfair_encrypt),
            ("Hill Cipher", self.hill_encrypt),
            ("Columnar Cipher", self.columnar_encrypt),
            ("Caesar Cipher", self.caesar_encrypt),
            ("Vernam Cipher", self.vernam_encrypt),
            ("Vigenère Cipher", self.vigenere_encrypt),
            ("One-Time Pad Cipher", self.one_time_pad_encrypt),
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Enter number for your cipher: "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ That wasn't a valid option. Try again.")

    def run_menu_decrypt(self):
        print("\n🧩 Select a cipher to Decrypt with:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_decrypt),
            ("Playfair Cipher", self.playfair_decrypt),
            ("Hill Cipher", self.hill_decrypt),
            ("Columnar Cipher", self.columnar_decrypt),
            ("Caesar Cipher", self.caesar_decrypt),
            ("Vernam Cipher", self.vernam_decrypt),
            ("Vigenère Cipher", self.vigenere_decrypt),
            ("One-Time Pad Cipher", self.one_time_pad_decrypt),
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Enter number for decryption: "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ That wasn't valid. Please try again.")

    # Caesar Encrypt and Decrypt
    def caesar_encrypt(self):
        text = input("Enter your message to encrypt: ")
        shift = int(input("Shift amount (1–25): "))
        encrypted = ""
        print("\n[🔒 Encrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} → {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\nEncrypted Result → {encrypted}")

    def caesar_decrypt(self):
        text = input("Enter the encrypted text: ")
        shift = int(input("Shift amount used (1–25): "))
        decrypted = ""
        print("\n[🔓 Decrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} → {shifted}")
                decrypted += shifted
            else:
                decrypted += char
        print(f"\nDecrypted Result → {decrypted}")

    # Vigenère Encrypt and Decrypt
    def vigenere_encrypt(self):
        text = input("Message to encrypt: ")
        key = input("Keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[🔒 Encrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} + {key_char} → {encrypted}")
                result += encrypted
            else:
                result += char
        print(f"\nEncrypted Result → {result}")

    def vigenere_decrypt(self):
        text = input("Encrypted text to decrypt: ")
        key = input("Keyword used: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[🔓 Decrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                decrypted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} - {key_char} → {decrypted}")
                result += decrypted
            else:
                result += char
        print(f"\nDecrypted Result → {result}")

    # Playfair Encrypt and Decrypt
    def playfair_encrypt(self):
        text = input("Enter message to encrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Encrypting Pairs]")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {cipher_pair}")
            encrypted += cipher_pair
        print(f"\nEncrypted Text → {encrypted}")

    def playfair_decrypt(self):
        text = input("Enter ciphertext to decrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Decrypting Pairs]")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {plain_pair}")
            decrypted += plain_pair
        print(f"\nDecrypted Text → {decrypted}")

    # Vernam encrypt/decrypt
    def vernam_encrypt(self):
        text = input("Plaintext input: ")
        key = input("Key (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[🔒 Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nEncrypted → {result}")
        print(f"(Hex) → {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("Ciphertext input: ")
        key = input("Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[🔓 Decrypting]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nDecrypted → {result}")
        print(f"(Hex) → {result.encode().hex()}")

    # One-Time Pad encrypt/decrypt (same operation)
    def one_time_pad_encrypt(self):
        text = input("Enter your message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n[🔒 Encrypting via One-Time Pad]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {ord(c) ^ k}")
        print(f"🔑 Generated key (hex): {key.hex()}")
        print(f"🔐 Encrypted output (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("Paste encrypted message (hex): ")
        key_hex = input("Paste key used (hex): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except Exception:
            print("⚠️ Invalid hex input—please try again.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n[🔓 Decrypting via One-Time Pad]")
        for e, k in zip(encrypted, key):
            print(f"{e} ⊕ {k} = {e ^ k}")
        print(f"\n📨 Decrypted message → {decrypted}")

    # Hill cipher encrypt/decrypt
    def hill_encrypt(self):
        text = input("Enter text to encrypt: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space-separated): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("⚠️ Invalid matrix input—please enter 9 integers.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[🔒 Encrypting with Hill Cipher]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block {block} → Col {j} = {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Key matrix used:")
        for row in matrix:
            print(row)
        print(f"\n🔐 Hill Cipher Encrypted result → {result}")

    def hill_decrypt(self):
        text = input("Enter encrypted text: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space-separated): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("⚠️ Invalid matrix input—please enter 9 integers.")
            return

        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("⚠️ Matrix not invertible mod 26—cannot decrypt.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[🔓 Decrypting with Hill Cipher]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(inv_matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block {block} → InvCol {j} = {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Inverse matrix used:")
        for row in inv_matrix:
            print(row)
        print(f"\n📨 Hill Cipher Decrypted result → {result}")

    def _hill_matrix_inverse(self, matrix):
        # Calculate determinant mod 26
        def det3(m):
            return (m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
                    - m[0][2]*m[1][1]*m[2][0] - m[0][1]*m[1][0]*m[2][2] - m[0][0]*m[1][2]*m[2][1]) % 26
        det = det3(matrix)
        det_inv = self._modular_inverse(det, 26)
        if det_inv is None:
            return None
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
        adj = [[cof[j][i] % 26 for j in range(3)] for i in range(3)]
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
        text = input("🚂 Plaintext message: ")
        if any(c.isdigit() for c in text):
            print("⚠️ Digits are not allowed in this cipher.")
            return
        try:
            rails = int(input("Specify number of rails (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid rails—please enter 2 to 10.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n[🔒 Encrypting Zigzag]")
        for char in text:
            print(f"{char} → rail {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        encrypted = ''.join(fence)
        print(f"\n🔐 Encrypted text → {encrypted}")

    def rail_fence_decrypt(self):
        ciphertext = input("🚂 Ciphertext: ")
        try:
            rails = int(input("Rails used (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid rails—please enter 2 to 10.")
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
        print("\n[🗺️ Marking positions]")
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*' and index < n:
                    fence[r][c] = ciphertext[index]
                    print(f"Placing {ciphertext[index]} at rail {r}, pos {c}")
                    index += 1

        result = []
        rail, direction = 0, 1
        print("\n[🔓 Reading zigzag]")
        for i in range(n):
            result.append(fence[rail][i])
            print(f"rail {rail}, pos {i} → {fence[rail][i]}")
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        decrypted = ''.join(result)
        print(f"\n📨 Decrypted text → {decrypted}")

    # Columnar encrypt/decrypt
    def columnar_encrypt(self):
        text = input("📋 Plaintext (spaces removed automatically): ").replace(" ", "")
        key = input("🔑 Keyword: ").lower()
        n = len(key)
        matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]
        while len(matrix[-1]) < n:
            matrix[-1].append('x')
        print("\n[🧩 Matrix layout]")
        for row in matrix:
            print("".join(row))

        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]
        print(f"Column order based on key: {order}")

        result = ""
        for col_num in sorted(order):
            col_idx = order.index(col_num)
            col_text = "".join(matrix[row][col_idx] for row in range(len(matrix)))
            print(f"Column {col_idx} ('{key[col_idx]}') → {col_text}")
            result += col_text
        print(f"\n✅ Encrypted → {result}")

    def columnar_decrypt(self):
        ciphertext = input("🔐 Ciphertext: ")
        key = input("🔑 Keyword used: ").lower()
        n = len(key)
        num_rows = len(ciphertext) // n
        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]

        cols = {}
        start = 0
        print("\n[📦 Extracting columns]")
        for col_num in sorted(order):
            length = num_rows
            cols[col_num] = ciphertext[start:start+length]
            print(f"Column {col_num} → {cols[col_num]}")
            start += length

        matrix = [[""]*n for _ in range(num_rows)]
        for col_idx, col_num in enumerate(order):
            col_text = cols[col_num]
            for row in range(num_rows):
                matrix[row][col_idx] = col_text[row]

        print("\n[🧱 Reconstructed matrix]")
        for row in matrix:
            print("".join(row))

        result = "".join(matrix[row][col] for row in range(num_rows) for col in range(n))
        print(f"\n📨 Decrypted → {result}")
#endregion cipher

# region GCD & LCM
class GCD_LCM:
    """Performs GCD and LCM calculations using classic number theory."""

    def __init__(self):
        clear_screen()
        print("🔧 Welcome to the GCD & LCM Toolkit!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhat would you like to compute?")
        print(" 1. 🔢 Greatest Common Divisor (GCD)")
        print(" 2. ♾️ Least Common Multiple (LCM)")
        print(" 3. 🚪 Exit")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == '1':
            self.gcd()
        elif choice == '2':
            self.lcm()
        elif choice == '3':
            print("👋 Goodbye! Come back anytime.")
            return
        else:
            print("⚠️ Invalid selection—please choose 1, 2, or 3.")

    def gcd(self):
        try:
            a = int(input("First number: "))
            b = int(input("Second number: "))
            x, y = a, b
            print(f"\n🔍 Computing GCD of {a} and {b}:\n")
            while y != 0:
                remainder = x % y
                print(f"{x} % {y} = {remainder}")
                x, y = y, remainder
            print(f"→ ✅ GCD({a}, {b}) = {x}")
        except ValueError:
            print("⚠️ Please enter valid integers.")

    def lcm(self):
        try:
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print(f"\n🔍 Computing LCM of {a} and {b}:\n")
            x, y = a, b
            while y != 0:
                x, y = y, x % y
            gcd = x
            print(f"GCD found: {gcd}")
            lcm = (a * b) // gcd
            print(f"→ ✅ LCM({a}, {b}) = {lcm}")
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
        print("✨ Set Theory Mode Activated!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("👋 Hello! Let’s explore some sets together.")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"Enter the elements for set {label} (separated by spaces): ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\n📁 You’ve entered these sets:")
        print(f"Set A = {self.set_a}")
        print(f"Set B = {self.set_b}")

    def compute_results(self):
        print("\n⚙️ Computing set operations...\n")
        sleep(1)

        operations = [
            ("Union", self._union),
            ("Intersection", self._intersection),
            ("Difference (A − B)", self._difference),
            ("Subset Check", self._subset_check),
            ("Equality Check", self._equality_check),
        ]
        random.shuffle(operations)

        for label, func in operations:
            print(f"--- 🔹 {label} ---")
            func()
            print()

    def _union(self):
        result = self.set_a.copy()
        for item in self.set_b:
            if item not in result:
                print(f"➕ Adding {item} to the union")
                result.add(item)
            else:
                print(f"✅ {item} is already in the union")
        print(f"→ Union = {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"🔗 {item} is in both sets")
                result.add(item)
            else:
                print(f"❗ {item} is only in A")
        print(f"→ Intersection = {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"👀 Keeping {item} (not in B)")
                result.add(item)
            else:
                print(f"🚫 Removing {item} (found in B)")
        print(f"→ A − B = {result}")

    def _subset_check(self):
        print("🔍 Checking if A is a subset of B...")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"✖️ {item} is missing in B — so not a subset")
                print("→ Result: No")
                return
            else:
                print(f"✔️ {item} found in B")
        print("→ Result: Yes (A ⊆ B)")

    def _equality_check(self):
        print("⚖️ Checking if A and B are equal...")
        all_items = self.set_a.union(self.set_b)
        same = True
        for item in all_items:
            in_a = item in self.set_a
            in_b = item in self.set_b
            symbol = "✅" if in_a and in_b else "❌"
            print(f"{symbol} {item}: A={in_a}, B={in_b}")
            if in_a != in_b:
                same = False
        print(f"→ Result: {'Yes' if same else 'No'} (A == B)")
# endregion set theory


# region sorting
class Sorting:
    """A simple class for sorting algorithms."""

    def __init__(self):
        clear_screen()
        print("✨ Launching the Sorting Module...")
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
        print("\n📊 Pick a sorting algorithm to explore:")
        for idx, (name, _) in enumerate(methods, 1):
            print(f" {idx}. {name}")
        print(" 0. 🔙 Return to Main Menu")

        try:
            choice = int(input("\n🔢 Your selection: "))
            if choice == 0:
                return
            _, func = methods[choice - 1]
            func()
        except (ValueError, IndexError):
            print("⚠️ That input wasn’t valid. Please pick a correct number.")
            sleep(1.5)

    def bubble_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n🔁 Running Bubble Sort...")
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(f"Swapping {arr[j]} ↔ {arr[j+1]} →", end=" ")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(arr)
                    sleep(0.01)
        print(f"✅ Sorted result: {arr}")

    def selection_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n🧐 Running Selection Sort...")
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"Step {i+1}: {arr}")
            sleep(0.01)
        print(f"✅ Sorted result: {arr}")

    def insertion_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n📥 Running Insertion Sort...")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"Step {i}: {arr}")
            sleep(0.01)
        print(f"✅ Sorted result: {arr}")

    def merge_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n🔗 Running Merge Sort...")
        self._merge_sort(arr)
        print(f"✅ Sorted result: {arr}")

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
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n⚡ Running Quick Sort...")
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"✅ Sorted result: {arr}")

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        print(f"Pivot chosen: {pivot}")
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(f"Swapped: {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        if not arr:
            print("⚠️ No numbers provided!")
            return
        print("\n🪣 Running Bucket Sort...")
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
        print(f"✅ Sorted result: {sorted_arr}")

    def shell_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n🔩 Running Shell Sort...")
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"After gap={gap}: {arr}")
            gap //= 2
        print(f"✅ Sorted result: {arr}")

    def comb_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n🧹 Running Comb Sort...")
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
        print(f"✅ Sorted result: {arr}")

    def radix_sort(self):
        arr = list(map(int, input("Enter numbers to sort (space‑separated): ").split()))
        print("\n🔢 Running Radix Sort...")
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort(arr, exp)
            print(f"After exp={exp}: {arr}")
            exp *= 10
        print(f"✅ Sorted result: {arr}")

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
        print("\n🌳 Tree Sort is a placeholder—stay tuned!")
# endregion sorting


# region conversion
class Conversion:
    """A flexible number base converter with detailed, step-by-step tracing."""

    def __init__(self):
        clear_screen()
        print("⚙️ Welcome to the Base Conversion Playground!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhich conversion adventure shall we take on today?\n")

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
            choice = int(input("\nChoose a task by entering its number: "))
            if 1 <= choice <= 12:
                print()
                options[choice - 1][1]()
            else:
                print("\n😅 That number’s not listed. Give it another shot!")
        except ValueError:
            print("\n😬 That doesn’t look like a number. Use digits only.")

    def decimal_to_binary(self):
        num = int(input("Enter a decimal number to convert to binary: "))
        self._decimal_to_base(num, 2, "Binary")

    def binary_to_decimal(self):
        binary = input("Paste a binary number (0s and 1s only): ")
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("Here’s the step-by-step breakdown:\n" + "\n".join(steps))
        print(f"→ That equals {int(binary, 2)} in decimal!")

    def decimal_to_octal(self):
        num = int(input("Enter a decimal number to convert to octal: "))
        self._decimal_to_base(num, 8, "Octal")

    def decimal_to_hex(self):
        num = int(input("Enter a decimal number to convert to hexadecimal: "))
        self._decimal_to_base(num, 16, "Hexadecimal")

    def octal_to_decimal(self):
        octal = input("Paste an octal number (digits 0–7): ")
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("Check out how it adds up:\n" + "\n".join(steps))
        print(f"→ That’s {int(octal, 8)} in decimal!")

    def hex_to_decimal(self):
        hex_str = input("Enter a hexadecimal number (0–9, A–F): ").upper()
        digits = "0123456789ABCDEF"
        steps = [f"{char} × 16^{i} = {digits.index(char)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("Decoding step-by-step:\n" + "\n".join(steps))
        print(f"→ That’s {int(hex_str, 16)} in decimal!")

    def binary_to_octal(self):
        binary = input("Enter a binary number to convert to octal: ")
        dec = int(binary, 2)
        print(f"First, that’s {dec} in decimal.")
        self._decimal_to_base(dec, 8, "Octal")

    def binary_to_hex(self):
        binary = input("Enter a binary number to convert to hex: ")
        dec = int(binary, 2)
        print(f"First, that’s {dec} in decimal.")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def octal_to_binary(self):
        octal = input("Enter an octal number to convert to binary: ")
        dec = int(octal, 8)
        print(f"Decimal equivalent is: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def octal_to_hex(self):
        octal = input("Enter an octal number to convert to hex: ")
        dec = int(octal, 8)
        print(f"Decimal equivalent is: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def hex_to_binary(self):
        hex_str = input("Enter a hex number to convert to binary: ")
        dec = int(hex_str, 16)
        print(f"Decimal equivalent is: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def hex_to_octal(self):
        hex_str = input("Enter a hex number to convert to octal: ")
        dec = int(hex_str, 16)
        print(f"Decimal equivalent is: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def _decimal_to_base(self, decimal, base, label):
        digits = "0123456789ABCDEF"
        original = decimal
        steps = []
        if decimal == 0:
            print(f"Conversion steps:\nZero converts directly to 0 in {label}.")
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
        print("Step-by-step insight:\n" + "\n".join(reversed(steps)))
        if base == 2:
            converted = bin(original)[2:]
        elif base == 8:
            converted = oct(original)[2:]
        else:
            converted = hex(original)[2:].upper()
        print(f"🎉 Final {label} result: {converted}")
# endregion conversion


# region Searching
class Searching:
    """A tool to explore different search algorithms interactively."""

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
            choice = int(input("Pick a number (1–6) to dive in: "))
        except ValueError:
            print("⚠️ Oops! That’s not a number between 1 and 6. Try again.")
            return self.menu()

        {
            1: self.interpolation_search,
            2: self.linear_search,
            3: self.binary_search,
            4: self.ternary_search,
            5: self.jump_search,
            6: self.interval_search,
        }.get(choice, lambda: (print("⚠️ That choice isn’t on the menu. Give it another go!"), self.menu()))()

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
        print("\n🔎 Starting ternary search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            print(f"Step {step}: left={left}, mid1={mid1}, mid2={mid2}, right={right} "
                  f"(values: {arr[mid1]}, {arr[mid2]})")
            step += 1

            if arr[mid1] == target:
                print(f"🎉 Found {target} at index {mid1}!")
                return
            if arr[mid2] == target:
                print(f"🎉 Found {target} at index {mid2}!")
                return

            if target < arr[mid1]:
                print(f"{target} < {arr[mid1]}: searching left third…")
                right = mid1 - 1
            elif target > arr[mid2]:
                print(f"{target} > {arr[mid2]}: searching right third…")
                left = mid2 + 1
            else:
                print(f"{target} is between {arr[mid1]} and {arr[mid2]}: searching middle third…")
                left = mid1 + 1
                right = mid2 - 1

        print(f"😞 No luck! {target} wasn’t found.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting jump search…\n")
        sleep(0.5)

        import math
        n = len(arr)
        step_size = int(math.sqrt(n))
        prev = 0
        step = 1

        # Jump through blocks
        while prev < n and arr[min(prev + step_size, n) - 1] < target:
            print(f"Step {step}: jumping to block ending at index {min(prev+step_size, n)-1} "
                  f"(value: {arr[min(prev+step_size, n)-1]})")
            prev += step_size
            step += 1

        # Linear search in the block
        print(f"🔎 Performing linear search in block starting at index {prev}…")
        for idx in range(prev, min(prev + step_size, n)):
            print(f"Checking index {idx} — value: {arr[idx]}")
            if arr[idx] == target:
                print(f"🎉 Found {target} at index {idx}!")
                return

        print(f"😞 Sorry, {target} isn’t in the list.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=False)
        print("\n🔎 Starting interval search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            print(f"Step {step}: checking interval from {left} to {right}")
            # find min and max in interval
            mini = min(arr[left:right+1])
            maxi = max(arr[left:right+1])
            print(f"Interval min={mini}, max={maxi}")
            if target < mini or target > maxi:
                print(f"{target} is outside this interval → narrowing...")
                left += 1
                right -= 1
            else:
                # fallback to linear in that interval
                for idx in range(left, right+1):
                    print(f"Checking index {idx} — value: {arr[idx]}")
                    if arr[idx] == target:
                        print(f"🎉 Found {target} at index {idx}!")
                        return
                break
            step += 1

        print(f"😞 No luck! {target} isn’t in this list.")
# endregion


# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("🌟 Welcome to the Prime Number Playground!")
        sleep(1)
        self.start()

    def start(self):
        print("\nChoose your prime adventure:")
        print(" 1. 🧐 Check if a number is prime")
        print(" 2. 🔍 Generate primes via Sieve")
        print(" 3. 🧩 Factorize a number")
        print(" 4. 📏 Fermat’s Little Theorem demo")
        print(" 5. 🌱 Find primitive roots")
        try:
            choice = int(input("Enter your choice (1–5): "))
        except ValueError:
            print("⚠️ Whoops! That wasn’t a valid number.")
            return

        match choice:
            case 1: self.check_prime()
            case 2: self.sieve()
            case 3: self.prime_factors()
            case 4: self.fermats()
            case 5: self.primitive_roots()
            case _: print("⚠️ That option isn’t available. Please choose 1–5.")

    def check_prime(self):
        try:
            n = int(input("\nType a number to check: "))
        except ValueError:
            print("⚠️ Enter a valid integer, please.")
            return

        if n < 2:
            print(f"❌ {n} isn’t prime—primes start from 2!")
            return

        for i in range(2, int(n ** 0.5) + 1):
            print(f"🔎 Testing {n} ÷ {i} → remainder = {n % i}")
            if n % i == 0:
                print(f"⛔ {n} is divisible by {i}, so it’s not prime.")
                return

        print(f"✅ Congratulations! {n} is indeed prime.")

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
            print("⚠️ That input isn’t a number.")
            return

        original = n
        factors = []

        print(f"\n🔧 Starting factorization of {original}:")

        while n % 2 == 0:
            print(f"{n} is even → capturing factor 2.")
            factors.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"{n} divisible by {i} → capturing {i}")
                factors.append(i)
                n //= i
            i += 2

        if n > 2:
            print(f"🎯 Prime leftover: {n}")
            factors.append(n)

        print(f"\n✅ Prime factors of {original}: {factors}")

    def sieve(self):
        print("\n🔬 Sieve of Eratosthenes – prime generation mode.")
        try:
            start = int(input("Starting number (inclusive): "))
            end = int(input("Ending number (exclusive): "))
        except ValueError:
            print("⚠️ Please enter valid numbers.")
            return

        if end <= start:
            print("⚠️ End must be larger than start.")
            return

        print(f"\n⏳ Calculating primes from {start} to {end}…")
        primes = [i for i in range(start, end) if self._check_prime(i)]

        print(f"\n✅ Primes between {start} and {end}:")
        print(primes)

    def fermats(self):
        print("\n📏 Demonstrating Fermat’s Little Theorem.")
        try:
            a = int(input("Value of a: "))
            k = int(input("Exponent k: "))
            p = int(input("Prime p: "))
        except ValueError:
            print("⚠️ Only numeric values allowed.")
            return

        if not self._check_prime(p):
            print("⚠️ That p isn’t prime—Fermat requires a prime modulus!")
            return

        result = pow(a, k, p)
        print(f"\n✨ Computation result: {a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\n🌱 Primitive Root Checker for prime p.")
        try:
            p = int(input("Prime p: "))
            a = int(input("Candidate a: "))
        except ValueError:
            print("⚠️ Please use valid positive integers.")
            return

        if p <= 0 or a <= 0:
            print("⚠️ Only positive integers accepted.")
            return

        if not self._check_prime(p):
            print("⚠️ p must be a prime number for this to work.")
            return

        required = set(range(1, p))
        actual = set(pow(a, k, p) for k in range(1, p))

        if actual == required:
            print(f"🎉 Yes! {a} is a primitive root modulo {p}.")
        else:
            print(f"🚫 Nope, {a} is not a primitive root for {p}.")

        print(f"\n🔍 Scanning all primitive roots modulo {p}…")
        roots = []
        for g in range(2, p):
            if set(pow(g, k, p) for k in range(1, p)) == required:
                roots.append(g)

        print(f"\n📋 All primitive roots of {p}:")
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
        print("🤖 Gia Balasabas’s Algorithm Hub: Activating Logic Matrix… 🤖\n")
        print(random.choice([
            "Which brain-teaser shall we crack today?",
            "Pick a puzzle and let’s get computing:",
            "Step into the algorithm playground below:",
            "Which problem shall we solve next?",
        ]))

        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. 🔷 {module.__name__}")
        print(" 0. 🛑 Quit Session")

        try:
            choice = int(input("\n📮 Your pick (0 to exit): "))
        except ValueError:
            print(random.choice([
                "\nOops, that’s not a number. Give it another go!",
                "\nOnly digits accepted! Try once more.",
                "\nInvalid input — please select by number.",
            ]))
            sleep(1.5)
            continue

        if choice == 0:
            print(random.choice([
                "\n👋 Thanks for the brain workout! Farewell!",
                "\n🎮 Session closed. See you for the next challenge!",
                "\n🌈 You crushed it! Come back soon.",
            ]))
            break

        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            while True:
                clear_screen()
                print(f"⚙️ Entering {selected_module.__name__} Module…\n")
                selected_module()

                again = input(random.choice([
                    "\n↩️ Want another round of this module? (y/N): ",
                    "\n🔁 One more go at this challenge? (y/N): ",
                    "\n🏁 Try it again? (y/N): ",
                ])).strip().lower()

                if again != 'y':
                    break
        else:
            print(random.choice([
                "\n❗ That option isn’t listed—try again.",
                "\n❗ Not valid. Choose from the list!",
                "\n❗ That’s not an available module number.",
            ]))
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion
##
