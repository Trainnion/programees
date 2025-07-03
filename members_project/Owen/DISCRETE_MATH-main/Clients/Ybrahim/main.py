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
    """🛡️ Stylish encryption & decryption using vintage ciphers."""

    def __init__(self):
        clear_screen()
        print("🧠 Cipher Control Panel Online!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\n🎛️ What would you like to do?")
        modes = [
            ("🗝️ Encrypt a message", self.run_menu_encrypt),
            ("📖 Decrypt a message", self.run_menu_decrypt)
        ]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("🔢 Choose a number: "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("🚫 That’s not a valid option. Let’s try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\n🛡️ Pick your encryption method:")
        options = [
            ("🚄 Rail Fence Cipher", self.rail_fence_encrypt),
            ("🔲 Playfair Cipher", self.playfair_encrypt),
            ("📏 Hill Cipher", self.hill_encrypt),
            ("🏛️ Columnar Cipher", self.columnar_encrypt),
            ("🎖️ Caesar Cipher", self.caesar_encrypt),
            ("🎩 Vernam Cipher", self.vernam_encrypt),
            ("📚 Vigenère Cipher", self.vigenere_encrypt),
            ("🎰 One-Time Pad Cipher", self.one_time_pad_encrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("👉 Select (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Whoops! That wasn’t valid.")

    def run_menu_decrypt(self):
        print("\n🔓 Pick your decryption method:")
        options = [
            ("🚄 Rail Fence Cipher", self.rail_fence_decrypt),
            ("🔲 Playfair Cipher", self.playfair_decrypt),
            ("📏 Hill Cipher", self.hill_decrypt),
            ("🏛️ Columnar Cipher", self.columnar_decrypt),
            ("🎖️ Caesar Cipher", self.caesar_decrypt),
            ("🎩 Vernam Cipher", self.vernam_decrypt),
            ("📚 Vigenère Cipher", self.vigenere_decrypt),
            ("🎰 One-Time Pad Cipher", self.one_time_pad_decrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("👉 Select (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ That didn’t work. Try a valid option.")

    # Caesar Encrypt and Decrypt
    def caesar_encrypt(self):
        text = input("✍️ Enter your message: ")
        shift = int(input("🎚️ Shift amount (1–25): "))
        encrypted = ""
        print("\n🔄 Encrypting with Caesar Cipher...")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} 🔁 {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\n📦 Encrypted message: {encrypted}")

    def caesar_decrypt(self):
        text = input("📩 Paste encrypted message: ")
        shift = int(input("🎚️ Shift amount used (1–25): "))
        decrypted = ""
        print("\n🔎 Decrypting Caesar Cipher...")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} ⬅️ {shifted}")
                decrypted += shifted
            else:
                decrypted += char
        print(f"\n📝 Decrypted message: {decrypted}")

    def vigenere_encrypt(self):
        text = input("📝 Enter plain text: ")
        key = input("🔐 Provide a keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n🔄 Encrypting with Vigenère...")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} ➕ {key_char} ➡️ {encrypted}")
                result += encrypted
            else:
                result += char
        print(f"\n🔏 Result: {result}")

    def vigenere_decrypt(self):
        text = input("📥 Enter encrypted text: ")
        key = input("🔐 Keyword used during encryption: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n🔍 Decrypting Vigenère...")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                decrypted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} ➖ {key_char} ➡️ {decrypted}")
                result += decrypted
            else:
                result += char
        print(f"\n📖 Decrypted result: {result}")

    def playfair_encrypt(self):
        text = input("📝 What do you want to encrypt? ")
        keyword = input("🔐 Keyword for matrix generation: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n📊 Cipher Matrix:")
        for row in matrix:
            print(" ".join(row))
        print("\n🔗 Digraphs:")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} 🔁 {cipher_pair}")
            encrypted += cipher_pair
        print(f"\n🔐 Encrypted Output: {encrypted}")

    def playfair_decrypt(self):
        text = input("📥 Input ciphertext: ")
        keyword = input("🔐 Keyword for matrix reconstruction: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n📊 Cipher Matrix:")
        for row in matrix:
            print(" ".join(row))
        print("\n🔓 Decryption Pairs:")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} ⬅️ {plain_pair}")
            decrypted += plain_pair
        print(f"\n🧾 Final Decryption: {decrypted}")

    def _playfair_decrypt_pair(self, matrix, a, b):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == a:
                    row1, col1 = i, j
                if matrix[i][j] == b:
                    row2, col2 = i, j
        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]

    def vernam_encrypt(self):
        text = input("💬 Enter message: ")
        key = input("🔐 Key (same length as message): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n🔄 Encrypting with Vernam Cipher...")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n🔏 Encrypted result: {result}")
        print(f"📦 Hex representation: {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("📥 Paste your encrypted message: ")
        key = input("🔐 Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n🧪 Decrypting using Vernam Cipher...")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n📜 Decrypted text: {result}")
        print(f"📦 Hex form: {result.encode().hex()}")

    def one_time_pad_encrypt(self):
        text = input("💬 Enter message to encrypt: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n🔒 One-Time Pad encryption in progress...")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {ord(c) ^ k}")
        print(f"🧾 Key (hex): {key.hex()}")
        print(f"📦 Encrypted output (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("📥 Encrypted message (hex format): ")
        key_hex = input("🔐 Key used (hex format): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except Exception:
            print("🚫 Invalid hex input provided.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n🔓 Decrypting using One-Time Pad...")
        for e, k in zip(encrypted, key):
            print(f"{e} ⊕ {k} = {e ^ k}")
        print(f"\n📜 Decrypted message: {decrypted}")

    def hill_encrypt(self):
        text = input("📨 Enter the message to encrypt: ")
        key_input = input("🔢 Provide 3x3 matrix (9 space-separated numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ You must enter exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("🚫 Invalid input for matrix.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n🔐 Encrypting using Hill Cipher...")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} × Column {j} = {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Key Matrix Used:")
        for row in matrix:
            print(row)
        print(f"📦 Encrypted Output: {result}")

    def hill_decrypt(self):
        text = input("🧩 Encrypted message: ")
        key_input = input("🔢 Enter 3x3 key matrix (9 space-separated values): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ You must enter exactly 9 values.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("🚫 Matrix input was invalid.")
            return

        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("🚫 Matrix not invertible under mod 26.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n🔓 Hill Cipher decryption underway...")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(inv_matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} × InvCol {j} = {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🔁 Inverse Key Matrix:")
        for row in inv_matrix:
            print(row)
        print(f"📜 Final Decryption: {result}")

    def rail_fence_encrypt(self):
        text = input("📝 Enter your message: ")
        if any(c.isdigit() for c in text):
            print("🚫 Digits aren’t allowed for this cipher.")
            return
        try:
            rails = int(input("🚆 Number of rails (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ That rail count isn’t valid.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n🌊 Writing in zigzag pattern...")
        for char in text:
            print(f"{char} 🠒 Row {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        encrypted = ''.join(fence)
        print(f"\n🔐 Final Encrypted Text: {encrypted}")

    def rail_fence_decrypt(self):
        ciphertext = input("📥 Encrypted message: ")
        try:
            rails = int(input("🚆 Number of rails used (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid rail count.")
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
        print("\n🧷 Filling pattern positions...")
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*' and index < n:
                    fence[r][c] = ciphertext[index]
                    print(f"Placing {ciphertext[index]} ➜ Rail {r}, Pos {c}")
                    index += 1

        result = []
        rail, direction = 0, 1
        print("\n🔁 Reading zigzag sequence...")
        for i in range(n):
            result.append(fence[rail][i])
            print(f"From Rail {rail}, Pos {i} 🡒 {fence[rail][i]}")
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        decrypted = ''.join(result)
        print(f"\n📜 Decrypted Message: {decrypted}")

    def columnar_encrypt(self):
        text = input("📝 Enter plaintext message: ").replace(" ", "")
        key = input("🔐 Enter keyword: ").lower()
        n = len(key)
        matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]
        while len(matrix[-1]) < n:
            matrix[-1].append('x')
        print("\n📊 Creating matrix:")
        for row in matrix:
            print("".join(row))

        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]
        print(f"🔢 Column order based on keyword: {order}")

        result = ""
        for col_num in sorted(order):
            col_idx = order.index(col_num)
            col_text = "".join(matrix[row][col_idx] for row in range(len(matrix)))
            print(f"🔽 Column {col_idx} ({key[col_idx]}) → {col_text}")
            result += col_text
        print(f"\n🔒 Encrypted Message: {result}")

    def columnar_decrypt(self):
        ciphertext = input("📥 Enter ciphertext: ")
        key = input("🔐 Keyword used: ").lower()
        n = len(key)
        num_rows = len(ciphertext) // n
        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]

        cols = {}
        start = 0
        for col_num in sorted(order):
            length = num_rows
            cols[col_num] = ciphertext[start:start+length]
            start += length
        print("\n📤 Extracted Columns:")
        for k, v in cols.items():
            print(f"Col {k}: {v}")

        matrix = [[""]*n for _ in range(num_rows)]
        for col_idx, col_num in enumerate(order):
            col_text = cols[col_num]
            for row in range(num_rows):
                matrix[row][col_idx] = col_text[row]

        print("\n🧩 Reconstructed Matrix:")
        for row in matrix:
            print("".join(row))

        result = "".join(matrix[row][col] for row in range(num_rows) for col in range(n))
        print(f"\n📜 Decrypted Message: {result}")
#endregion ciphers
# 1 by 1 paste please

# region Searching
class Searching: 
    """An interactive explorer of popular search algorithms."""

    def __init__(self):
        clear_screen()
        print("🌸 Welcome to the Sakura Search Pavilion!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\n🌺 Which blossom of search would you like to explore?")
        print(" 1. 🎯 Interpolation Search")
        print(" 2. 🧭 Linear Search")
        print(" 3. 🪷 Binary Search")
        print(" 4. 🌼 Ternary Search")
        print(" 5. 🪜 Jump Search")
        print(" 6. 🌊 Interval Search")
        
        try:
            choice = int(input("🌟 Choose a number (1–3): "))
        except ValueError:
            print("⚠️ Only valid numbers are allowed. Please try again.")
            return self.menu()

        if choice == 2:
            self.linear_search()
        elif choice == 3:
            self.binary_search()
        elif choice == 1:
            self.interpolation_search()
        else:
            print("🚫 That option isn’t blooming yet. Pick another.")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\n🌸 Enter a list of numbers (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"🧺 Sorted garden: {values}")
            target = int(input("🔍 Which number are we looking for?: "))
            return values, target
        except ValueError:
            print("⚠️ Please type only valid numbers.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🚶 Starting linear search...\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"🔎 Checking index {idx}: value = {val}")
            if val == target:
                print(f"🎉 Found it! {target} is at position {idx}.")
                return
            print("🌿 Not here... moving along.")
        print(f"🍂 {target} wasn’t spotted in the field.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🧭 Navigating binary search...\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"🔎 Step {step}: left = {left}, right = {right}, mid = {mid}, value = {arr[mid]}")
            step += 1

            if arr[mid] == target:
                print(f"🌟 Success! {target} is at index {mid}.")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} < {target} → Searching right side")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {target} → Searching left side")
                right = mid - 1

        print(f"🍁 No match for {target} in the sorted array.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🌈 Starting interpolation search...\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎯 Target found at index {low}.")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"🔍 Step {step}: low = {low}, high = {high}, pos = {pos}, value = {arr[pos]}")
            step += 1

            if arr[pos] == target:
                print(f"🏵️ Wonderful! {target} blooms at index {pos}.")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} < {target} → Shift right")
                low = pos + 1
            else:
                print(f"{arr[pos]} > {target} → Shift left")
                high = pos - 1

        print(f"🌫️ Alas, {target} isn’t in the collection.")

    def ternary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🌻 Sprouting Ternary Search...\n")
        sleep(0.5)
        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            print(f"📘 Step {step}: mid1={mid1}({arr[mid1]}), mid2={mid2}({arr[mid2]})")
            step += 1
            if arr[mid1] == target:
                print(f"🌼 Located at index {mid1}")
                return
            if arr[mid2] == target:
                print(f"🌼 Located at index {mid2}")
                return
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        print(f"🍃 Couldn’t find {target} in the garden path.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🏞️ Jumping into the search...\n")
        sleep(0.5)
        import math
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n) - 1] < target:
            print(f"🪜 Leaping from {prev} to {min(step, n) - 1}")
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                print("🚧 We've gone too far!")
                return
        for i in range(prev, min(step, n)):
            print(f"🔍 Peeking at index {i}: {arr[i]}")
            if arr[i] == target:
                print(f"🌟 Found your number at index {i}")
                return
        print(f"🍂 {target} was not among the jumped steps.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📶 Blossoming Interval Search...\n")
        sleep(0.5)
        if len(arr) == 0:
            print("🌾 The list is empty!")
            return
        if arr[0] == target:
            print("🎯 Found at index 0")
            return
        index = 1
        while index < len(arr) and arr[index] <= target:
            print(f"⏩ Growth phase: index={index}, value={arr[index]}")
            index *= 2
        left = index // 2
        right = min(index, len(arr) - 1)
        print(f"🔎 Binary blossom between {left} and {right}")
        while left <= right:
            mid = (left + right) // 2
            print(f"🧪 Evaluating mid={mid}: {arr[mid]}")
            if arr[mid] == target:
                print(f"🌟 Found your bloom at index {mid}")
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"🌧️ {target} didn’t grow within this interval.")
# endregion

# region Prime
class Prime:
    """NeoSynth Prime Toolkit: prime checks, factorization, modular power, and root discovery."""

    def __init__(self):
        clear_screen()
        print("🔬 [PrimeLab] Launching Prime Intelligence Module...")
        sleep(1)
        self.start()

    def start(self):
        print("\n📊 Select a prime function to initiate:")
        print(" 1. 🔍 Prime Check")
        print(" 2. 📈 Primes in Range (Sieve)")
        print(" 3. 🧱 Prime Factorization")
        print(" 4. 🧮 Fermat’s Modular Power")
        print(" 5. 🔑 Primitive Root Finder")

        try:
            choice = int(input("\n🎯 Choose an option (1–5): "))
        except ValueError:
            print("⚠️ Invalid input. Use a number between 1 and 5.")
            return

        match choice:
            case 1: self.check_prime()
            case 2: self.sieve()
            case 3: self.prime_factors()
            case 4: self.fermats()
            case 5: self.primitive_roots()
            case _: print("🚫 Invalid option. Try again.")

    def check_prime(self):
        try:
            n = int(input("\n🔢 Enter a number to test: "))
        except ValueError:
            print("🚫 Invalid input. Use whole numbers only.")
            return

        if n < 2:
            print(f"❌ {n} is not prime (minimum is 2).")
            return

        for i in range(2, int(n ** 0.5) + 1):
            print(f"🔎 Step: {n} % {i} = {n % i}")
            if n % i == 0:
                print(f"✖️ Composite! Divisible by {i}.")
                return

        print(f"✅ {n} is a prime number!")

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
            n = int(input("\n🧩 Enter a number to factor: "))
        except ValueError:
            print("⚠️ Please enter a valid integer.")
            return

        original = n
        factors = []
        print(f"\n🔧 Decomposing {original} into primes...")

        while n % 2 == 0:
            print(f"➕ Factor 2 (even division)")
            factors.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"➕ Factor {i}")
                factors.append(i)
                n //= i
            i += 2

        if n > 2:
            print(f"🧿 Final prime: {n}")
            factors.append(n)

        print(f"\n📦 Prime factor list: {factors}")

    def sieve(self):
        print("\n🧪 Prime Discovery (Sieve of Eratosthenes)")
        try:
            start = int(input("🔹 Start of range: "))
            end = int(input("🔸 End of range: "))
        except ValueError:
            print("⚠️ Please input valid integers.")
            return

        if end <= start:
            print("⚠️ End must be greater than start.")
            return

        print(f"\n🚦 Scanning primes in [{start}, {end})...")
        primes = [i for i in range(start, end) if self._check_prime(i)]
        print(f"\n📋 Primes found: {primes}")

    def fermats(self):
        print("\n📐 Modular Exponentiation using Fermat's Little Theorem")
        try:
            a = int(input("🔸 Base (a): "))
            k = int(input("🔺 Exponent (k): "))
            p = int(input("🔻 Prime Modulus (p): "))
        except ValueError:
            print("🚫 Integers only, please.")
            return

        if not self._check_prime(p):
            print("❌ Modulus must be a prime number.")
            return

        result = pow(a, k, p)
        print(f"\n📈 Computation: {a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\n🔐 Primitive Root Validator")
        try:
            p = int(input("🔹 Enter prime modulus (p): "))
            a = int(input("🔸 Enter candidate root (a): "))
        except ValueError:
            print("⚠️ Inputs must be integers.")
            return

        if p <= 0 or a <= 0:
            print("🚫 Numbers must be greater than 0.")
            return

        if not self._check_prime(p):
            print("❌ p must be a prime number.")
            return

        required = set(range(1, p))
        actual = set(pow(a, k, p) for k in range(1, p))

        if actual == required:
            print(f"✅ {a} is a primitive root modulo {p}.")
        else:
            print(f"❌ {a} is not a primitive root modulo {p}.")

        print(f"\n🔎 Scanning all primitive roots of {p}...")
        roots = []
        for g in range(2, p):
            if set(pow(g, k, p) for k in range(1, p)) == required:
                roots.append(g)

        print(f"🌟 Valid primitive roots of {p}: {roots}")
# endregion

# region GCD & LCM
class GCD_LCM:
    """A precision toolkit for computing GCD and LCM using number theory logic."""

    def __init__(self):
        clear_screen()
        print("🔧 [NumberCore] Initiating GCD & LCM Engine...")
        sleep(1)
        self.start()

    def start(self):
        print("\n🔍 Select a calculation module:")
        print(" 1. 📐 GCD (Greatest Common Divisor)")
        print(" 2. 📏 LCM (Least Common Multiple)")
        print(" 3. 🔙 Return to Main Console")

        choice = input("\n📌 Your selection (1–3): ").strip()

        if choice == '1':
            self.gcd()
        elif choice == '2':
            self.lcm()
        elif choice == '3':
            print("↩️ Returning to hub...")
            sleep(1)
        else:
            print("⚠️ Invalid input. Restarting module...")
            sleep(1.5)
            self.start()

    def gcd(self):
        try:
            a = int(input("\n🔢 Input first integer: "))
            b = int(input("🔢 Input second integer: "))
        except ValueError:
            print("🚫 Error: Whole numbers only.")
            return

        print(f"\n📘 Euclidean Algorithm: GCD({a}, {b})")
        step = 1
        while b != 0:
            print(f"🌀 Step {step}: {a} mod {b} = {a % b}")
            a, b = b, a % b
            step += 1

        print(f"\n✅ Result: GCD is {a}")

    def lcm(self):
        try:
            a = int(input("\n🔢 Input first integer: "))
            b = int(input("🔢 Input second integer: "))
        except ValueError:
            print("🚫 Error: Whole numbers only.")
            return

        original_a, original_b = a, b
        print(f"\n🧮 Calculating LCM of {a} and {b}...")

        # Compute GCD
        x, y = a, b
        while y != 0:
            x, y = y, x % y
        gcd = x

        # Compute LCM
        lcm = abs(original_a * original_b) // gcd
        print(f"\n📘 Step 1: GCD({original_a}, {original_b}) = {gcd}")
        print(f"📘 Step 2: LCM = |{original_a} × {original_b}| ÷ {gcd} = {lcm}")
        print(f"\n🎯 Result: LCM is {lcm}")
# endregion

# region conversion
class Conversion:
    """A futuristic number base converter with precision-guided feedback."""

    def __init__(self):
        clear_screen()
        print("🧠 [BaseCore Unit] Activating Conversion Interface...")
        sleep(1)
        self.start()

    def start(self):
        print("\n🔧 Select a base conversion protocol:\n")

        options = [
            ("🔢 Decimal → Binary", self.decimal_to_binary),
            ("💡 Binary → Decimal", self.binary_to_decimal),
            ("🔢 Decimal → Octal", self.decimal_to_octal),
            ("🔢 Decimal → Hexadecimal", self.decimal_to_hex),
            ("📘 Octal → Decimal", self.octal_to_decimal),
            ("📘 Hexadecimal → Decimal", self.hex_to_decimal),
            ("💡 Binary → Octal", self.binary_to_octal),
            ("💡 Binary → Hexadecimal", self.binary_to_hex),
            ("📘 Octal → Binary", self.octal_to_binary),
            ("📘 Octal → Hexadecimal", self.octal_to_hex),
            ("📘 Hexadecimal → Binary", self.hex_to_binary),
            ("📘 Hexadecimal → Octal", self.hex_to_octal),
        ]

        random.shuffle(options)

        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")

        try:
            choice = int(input("\n🧮 Enter your choice (1–12): "))
            if 1 <= choice <= 12:
                options[choice - 1][1]()
            else:
                print("⚠️ Selection out of range. Try again.")
        except ValueError:
            print("⚠️ Invalid input — numeric choices only.")

    def decimal_to_binary(self):
        num = int(input("🔢 Input decimal value: "))
        self._decimal_to_base(num, 2, "Binary")

    def binary_to_decimal(self):
        binary = input("💡 Input binary value: ")
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("📘 Breakdown:\n" + "\n".join(steps))
        print(f"✅ Decimal Result: {int(binary, 2)}")

    def decimal_to_octal(self):
        num = int(input("🔢 Input decimal value: "))
        self._decimal_to_base(num, 8, "Octal")

    def decimal_to_hex(self):
        num = int(input("🔢 Input decimal value: "))
        self._decimal_to_base(num, 16, "Hexadecimal")

    def octal_to_decimal(self):
        octal = input("📘 Enter octal number (0–7): ")
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("📘 Breakdown:\n" + "\n".join(steps))
        print(f"✅ Decimal Result: {int(octal, 8)}")

    def hex_to_decimal(self):
        hex_str = input("📘 Enter hexadecimal (0–9, A–F): ").upper()
        digits = "0123456789ABCDEF"
        steps = [f"{char} × 16^{i} = {digits.index(char)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("📘 Breakdown:\n" + "\n".join(steps))
        print(f"✅ Decimal Result: {int(hex_str, 16)}")

    def binary_to_octal(self):
        binary = input("💡 Input binary value: ")
        dec = int(binary, 2)
        print(f"🔄 Converted to Decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def binary_to_hex(self):
        binary = input("💡 Input binary value: ")
        dec = int(binary, 2)
        print(f"🔄 Converted to Decimal: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def octal_to_binary(self):
        octal = input("📘 Input octal value: ")
        dec = int(octal, 8)
        print(f"🔄 Converted to Decimal: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def octal_to_hex(self):
        octal = input("📘 Input octal value: ")
        dec = int(octal, 8)
        print(f"🔄 Converted to Decimal: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def hex_to_binary(self):
        hex_str = input("📘 Input hexadecimal: ")
        dec = int(hex_str, 16)
        print(f"🔄 Converted to Decimal: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def hex_to_octal(self):
        hex_str = input("📘 Input hexadecimal: ")
        dec = int(hex_str, 16)
        print(f"🔄 Converted to Decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def _decimal_to_base(self, decimal, base, label):
        digits = "0123456789ABCDEF"
        original = decimal
        steps = []
        while decimal > 0:
            r = decimal % base
            q = decimal // base
            step = f"{decimal} ÷ {base} = {q} R {r}"
            if base == 16:
                step += f" ({digits[r]})"
            steps.append(step)
            decimal = q
        if not steps:
            steps.append("0")
        print("\n📘 Conversion Process:\n" + "\n".join(reversed(steps)))
        if base == 2:
            converted = bin(original)[2:]
        elif base == 8:
            converted = oct(original)[2:]
        else:
            converted = hex(original)[2:].upper()
        print(f"\n✅ {label} Result: {converted}")
# endregion conversion

#region sorting
class Sorting:
    """An interactive console for sorting algorithms with style."""

    def __init__(self):
        clear_screen()
        print("🧩 [SortCore AI] Initializing Sorting Engine...")
        sleep(1)
        self.start()

    def start(self):
        methods = [
            ("⚡ Quick Sort", self.quick_sort),
            ("🌲 Tree Sort", self.tree_sort),
            ("📥 Insertion Sort", self.insertion_sort),
            ("🔗 Merge Sort", self.merge_sort),
            ("🫧 Bubble Sort", self.bubble_sort),
            ("🪣 Bucket Sort", self.bucket_sort),
            ("🧹 Comb Sort", self.comb_sort),
            ("⚙️ Shell Sort", self.shell_sort),
            ("📊 Radix Sort", self.radix_sort),
            ("🎯 Selection Sort", self.selection_sort),
        ]

        while True:
            clear_screen()
            print("\n📁 Select a sorting protocol to activate:")
            for idx, (name, _) in enumerate(methods, 1):
                print(f" {idx}. {name}")
            print(" 0. ⬅️ Return to Main Console")

            try:
                choice = int(input("\n🧠 Enter your selection: "))
                if choice == 0:
                    return
                _, func = methods[choice - 1]
                func()
                input("\n⏎ Press Enter to return to menu...")
            except (ValueError, IndexError):
                print("⚠️ Invalid input — please choose a valid option.")
                sleep(1.5)

    def bubble_sort(self):
        arr = self._get_input()
        print("\n🫧 Executing Bubble Sort Protocol...")
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(f"🔁 Swapped: {arr}")
                    sleep(0.01)
        print(f"\n✅ Sort Complete: {arr}")

    def selection_sort(self):
        arr = self._get_input()
        print("\n🎯 Activating Selection Sort...")
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"📍 Pass {i+1}: {arr}")
            sleep(0.01)
        print(f"\n✅ Ordered Output: {arr}")

    def insertion_sort(self):
        arr = self._get_input()
        print("\n📥 Launching Insertion Sort Module...")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"➡️ Inserted {key}: {arr}")
            sleep(0.01)
        print(f"\n✅ Final Output: {arr}")

    def merge_sort(self):
        arr = self._get_input()
        print("\n🔗 Merge Sort Initialized...")
        self._merge_sort(arr)
        print(f"\n📦 Merge Complete: {arr}")

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            print(f"📤 Dividing: {L} | {R}")
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
            print(f"🧬 Reassembled: {arr}")
            sleep(0.05)

    def quick_sort(self):
        arr = self._get_input()
        print("\n⚡ Activating Quick Sort Engine...")
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"\n🏁 Sorted: {arr}")

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        print(f"🎯 Current Pivot: {pivot}")
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(f"↔️ Swapped: {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = self._get_input()
        if not arr:
            print("⚠️ Empty input — nothing to sort.")
            return
        print("\n🪣 Segmenting buckets...")
        bucket_count = 10
        max_val, min_val = max(arr), min(arr)
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            idx = int((num - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[idx].append(num)
        for i, b in enumerate(buckets):
            b.sort()
            print(f"📂 Bucket {i}: {b}")
        sorted_arr = [num for b in buckets for num in b]
        print(f"\n✅ Bucket Merge Result: {sorted_arr}")

    def shell_sort(self):
        arr = self._get_input()
        print("\n⚙️ Engaging Shell Sort...")
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"📏 Gap {gap} ➝ {arr}")
            gap //= 2
        print(f"\n✅ Shell Sort Finished: {arr}")

    def comb_sort(self):
        arr = self._get_input()
        print("\n🧹 Initiating Comb Sort Sweep...")
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
                    print(f"🔁 Swap executed: {arr}")
        print(f"\n✅ Comb Sort Output: {arr}")

    def radix_sort(self):
        arr = self._get_input()
        print("\n📊 Initiating Radix Sort Routine...")
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort(arr, exp)
            print(f"🧮 After exp={exp}: {arr}")
            exp *= 10
        print(f"\n🏆 Final Sorted Output: {arr}")

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
        print("\n🌲 Tree Sort module is under development. Please wait for deployment...")

    def _get_input(self):
        try:
            return list(map(int, input("\n🔢 Provide a list of integers (space-separated): ").split()))
        except ValueError:
            print("🚫 Error: Invalid input — numbers only.")
            return self._get_input()
#endregion sorting

#region set theory
class SetTheory: 
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("🛠️ [System Boot] Initializing SetOps Engine...")
        sleep(1)
        self.run()

    def run(self):
        self.display_intro()
        self.get_sets()
        self.display_sets()
        self.perform_operations()

    def display_intro(self):
        print("📡 Welcome to SET-CORE v2.7")
        print("🔍 Initiating logical sequence between SET-A and SET-B...")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"\n📨 Input sequence for Set-{label} (space-delimited values): ")
        cleaned = set(raw.strip().split())
        print(f"✅ Data captured for Set-{label}: {cleaned}")
        return cleaned

    def display_sets(self):
        print("\n🗃️ Registered Datasets:")
        print(f"🅰️ Set-A » {self.set_a}")
        print(f"🅱️ Set-B » {self.set_b}")

    def perform_operations(self):
        print("\n⚙️ Processing Operations...\n")
        sleep(1)

        operations = [
            ("🔗 UNION", self._union),
            ("🔁 INTERSECTION", self._intersection),
            ("📤 DIFFERENCE (A - B)", self._difference),
            ("🧭 SUBSET CHECK (A ⊆ B)", self._subset_check),
            ("⚖️ EQUALITY CHECK (A == B)", self._equality_check),
        ]
        random.shuffle(operations)

        for label, func in operations:
            print(f"{label}")
            func()
            print("-" * 40)

    def _union(self):
        result = self.set_a.copy()
        for item in self.set_b:
            if item not in result:
                print(f"➕ Merging '{item}' into union dataset")
                result.add(item)
            else:
                print(f"🔁 Duplicate detected: '{item}' already exists")
        print(f"📊 [UNION RESULT] {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"✅ Shared entry: '{item}'")
                result.add(item)
            else:
                print(f"🗑️ '{item}' excluded – not in Set-B")
        print(f"📊 [INTERSECTION RESULT] {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"📤 Retained '{item}' — unique to Set-A")
                result.add(item)
            else:
                print(f"❌ Dropped '{item}' — exists in Set-B")
        print(f"📊 [DIFFERENCE RESULT] {result}")

    def _subset_check(self):
        print("🔎 Executing subset validation: Is A ⊆ B?")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"❌ Missing: '{item}' not present in Set-B")
                print("📢 Result: A is NOT a subset of B")
                return
            print(f"✔️ Verified: '{item}' exists in Set-B")
        print("📢 Result: A is a valid subset of B")

    def _equality_check(self):
        print("🧪 Comparing sets for strict equality...")
        all_items = self.set_a.union(self.set_b)
        equal = True
        for item in sorted(all_items):
            in_a = item in self.set_a
            in_b = item in self.set_b
            status = "✅" if in_a and in_b else "❌"
            print(f"{status} '{item}' — A: {in_a} | B: {in_b}")
            if in_a != in_b:
                equal = False
        print(f"📢 Equality Verdict: {'MATCH (A == B)' if equal else 'MISMATCH (A ≠ B)'}")
#endregion set theory

# region Searching
class Searching: 
    """An interactive explorer of popular search algorithms."""

    def __init__(self):
        clear_screen()
        print("🔍 [NeuroSearch AI] Booting algorithm panel...")
        sleep(1)
        self.menu()

    def menu(self):
        print("\n🧠 Choose search protocol to activate:")
        print(" 1. 📡 Interpolation Search")
        print(" 2. 🛰️ Linear Search")
        print(" 3. 💾 Binary Search")
        print(" 4. 🧮 Ternary Search")
        print(" 5. 🪜 Jump Search")
        print(" 6. 📶 Interval Search")
        
        try:
            choice = int(input("🕹️ Input your command (1–3): "))
        except ValueError:
            print("⚠️ Invalid input — numerical values only.")
            return self.menu()

        if choice == 2:
            self.linear_search()
        elif choice == 3:
            self.binary_search()
        elif choice == 1:
            self.interpolation_search()
        else:
            print("🚫 Operation not implemented. Redirecting...")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\n🔢 Input dataset (space-separated integers): ").split()))
            if sort_array:
                values.sort()
                print(f"📊 Sorted sequence: {values}")
            target = int(input("🎯 Target value to locate: "))
            return values, target
        except ValueError:
            print("⛔ Error: Please enter valid integer values.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔎 [Executing] Linear Search Protocol...\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"🧪 Scanning index {idx}: value = {val}")
            if val == target:
                print(f"✅ Match found — target {target} at index {idx}")
                return
            print("⏭️ No match. Continuing scan...")
        print(f"❌ Target {target} not located in data stream.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🧠 [Executing] Binary Search...\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"📍 Step {step}: L={left}, R={right}, M={mid} ({arr[mid]})")
            step += 1

            if arr[mid] == target:
                print(f"🎯 Match! Target {target} is at index {mid}")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} < {target} — scanning right half")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {target} — scanning left half")
                right = mid - 1

        print(f"❌ Target {target} not found in binary search space.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📡 Initiating Interpolation Search...\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎯 Located target at index {low}")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"📡 Step {step}: Low={low}, High={high}, Pos={pos}, Val={arr[pos]}")
            step += 1

            if arr[pos] == target:
                print(f"✅ Success — target {target} at index {pos}")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} < {target} — shifting right")
                low = pos + 1
            else:
                print(f"{arr[pos]} > {target} — shifting left")
                high = pos - 1

        print(f"❌ Target {target} unreachable via interpolation.")

    def ternary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🧮 Engaging Ternary Search Engine...\n")
        sleep(0.5)
        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            print(f"📘 Step {step}: mid1={mid1}({arr[mid1]}), mid2={mid2}({arr[mid2]})")
            step += 1
            if arr[mid1] == target:
                print(f"🎯 Target found at index {mid1}")
                return
            if arr[mid2] == target:
                print(f"🎯 Target found at index {mid2}")
                return
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        print(f"❌ Ternary sweep completed. {target} not present.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🪜 Initiating Jump Protocol...\n")
        sleep(0.5)
        import math
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n) - 1] < target:
            print(f"⛓️ Jumping from {prev} → {min(step, n) - 1}")
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                print("🛑 Exceeded data bounds.")
                return
        for i in range(prev, min(step, n)):
            print(f"🔬 Inspecting index {i}: {arr[i]}")
            if arr[i] == target:
                print(f"✅ Target found at index {i}")
                return
        print(f"❌ Target {target} not located after jumps.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📶 Executing Interval Search Algorithm...\n")
        sleep(0.5)
        if len(arr) == 0:
            print("📭 Dataset is empty. Aborting.")
            return
        if arr[0] == target:
            print("🎯 Target is at index 0")
            return
        index = 1
        while index < len(arr) and arr[index] <= target:
            print(f"⏩ Scanning index {index}: value={arr[index]}")
            index *= 2
        left = index // 2
        right = min(index, len(arr) - 1)
        print(f"📊 Running binary slice between {left} and {right}")
        while left <= right:
            mid = (left + right) // 2
            print(f"🔎 Inspecting mid={mid}: {arr[mid]}")
            if arr[mid] == target:
                print(f"✅ Match! Index {mid}")
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"❌ {target} not found in exponential scan.")
# endregion

# region Main Program Loop
def main():
    modules = [
        Sorting,
        Ciphers,
        SetTheory,
        Conversion,
        GCD_LCM,
        Prime,
        Searching,
    ]

    while True:
        clear_screen()
        print("James Ybrahim Arip Algorithm Explorer\n")
        print("🧩 Select a challenge to blossom your coding skills:")

        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. 🌼 {module.__name__}")
        print(" 0. 🚪 Exit the Garden")

        try:
            choice = int(input("\n🌟 What's your pick? (0 to exit): "))
        except ValueError:
            print("\n❌ Oops! That's not a number. Try once more with care.")
            sleep(1.5)
            continue

        if choice == 0:
            print("\n🌙 Goodbye, noble coder! Return whenever you're ready to bloom again.")
            break

        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            while True:
                clear_screen()
                print(f"🔧 Opening Module: {selected_module.__name__}\n")
                selected_module()

                again = input("\n🔄 Would you like to explore this module again? (y/N): ").strip().lower()
                if again != 'y':
                    break
        else:
            print("\n🚫 That's not one of the available petals. Choose wisely next time.")
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion

