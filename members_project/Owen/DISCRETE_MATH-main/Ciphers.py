from basic_math import bMath
from Advanced.encryption.playfair import PlayfairCipher
from TOOLS import TOOLS 
# from main import delay
import os
# TOOLS.set_delay(delay)  # Set a default delay for typewriter effect

class Ciphers:
    """a class to encrypt and decrypt text using various ciphers."""
    
    def __init__(self,):
        TOOLS.clear_screen()
        self.methods = [
            "Caesar Cipher",
            "Vigenère Cipher",
            "Playfair Cipher",
            "Vernam Cipher",
            "One Time Pad Cipher",
            "Hill Cipher",
            "Rail Fence Cipher",
            "Columnar Cipher"
        ]
        self.start()

    def start(self):
        TOOLS.print_type("pick your desired encryption method.")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        TOOLS.print_type("")
        choice = int(TOOLS.input_type("Enter the number of the method you want to use: ")) - 1
        TOOLS.print_type("")
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please run the program again.")
            exit()
        picked_method = self.methods[choice]
        TOOLS.print_type(f"You have selected: {picked_method}", "blue")
        match picked_method:
            case "Caesar Cipher":
                self._caesar()
            case "Vigenère Cipher":
                self._vigenere()
            case "Playfair Cipher":
                self._playfair()
            case "Vernam Cipher":
                self._vernam_cipher()
            case "One Time Pad Cipher":
                self._one_time_pad()
            case "Hill Cipher":
                self._hill_cipher()
            case "Rail Fence Cipher":
                self._rail_fence_cipher()
            case "Columnar Cipher":
                self._columnar_cipher()
            case _:
                TOOLS.print_type("This method is not implemented yet.")

#region caesar cipher
    def _caesar(self):
        text = TOOLS.input_type("Enter the text to encrypt: ")
        if any(char.isdigit() for char in text):
            TOOLS.print_type("Error: Text should not contain numbers.")
            return
        shift = int(TOOLS.input_type("Enter the shift value (1-25): "))
        if 1 <= shift <= 25:
            encrypted_text = self.caesar(text, shift)
            TOOLS.print_type(f"Encrypted text: {encrypted_text}", "yellow")
        else:
            TOOLS.print_type("Invalid shift value. Please enter a number between 1 and 25.")
    
    def caesar(self, text, shift):
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        encrypted_text = ""
        for char in text:
            if char in small:
                index = small.index(char)
                new_index = (index + shift) % 26
                encrypted_text += small[new_index]
            elif char in big:
                index = big.index(char)
                new_index = (index + shift) % 26
                encrypted_text += big[new_index]
            else:
                encrypted_text += char
        return encrypted_text
#endregion caesar cipher

#region vigenere cipher
    def _vigenere(self):
        text = TOOLS.input_type("Enter the text to encrypt: ")
        if any(char.isdigit() for char in text):
            TOOLS.print_type("Error: Text should not contain numbers.")
            return
        keyword = TOOLS.input_type("Enter the keyword: ")
        if any(char.isdigit() for char in keyword):
            TOOLS.print_type("Error: Keyword should not contain numbers.")
            return
        encrypted_text = self.vigenere(text, keyword)
        TOOLS.print_type(f"Encrypted text: {encrypted_text}", "yellow")

    def vigenere(self, text, keyword):
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
        encrypted_text = ""
        
        for i, char in enumerate(text):
            if char in small:
                index = small.index(char)
                shift = small.index(keyword_repeated[i].lower())
                new_index = (index + shift) % 26
                encrypted_text += small[new_index]
            elif char in big:
                index = big.index(char)
                shift = big.index(keyword_repeated[i].upper())
                new_index = (index + shift) % 26
                encrypted_text += big[new_index]
            else:
                encrypted_text += char
        
        return encrypted_text
#endregion vigenere cipher

#region playfair cipher
    def _playfair(self):
        text = TOOLS.input_type("Enter the text to encrypt: ")
        keyword = TOOLS.input_type("Enter the keyword: ")
        encrypted_text = self.playfair(text, keyword)
        TOOLS.print_type(f"Encrypted text: {encrypted_text}", "yellow")
    
    def playfair(self, text, keyword):
        cipher = PlayfairCipher(text,keyword)
        return cipher.ciphertext
#endregion playfair cipher

#region vernam cipher
    def _vernam_cipher(self):
        TOOLS.print_type("")
        text = TOOLS.input_type("Enter the text to encrypt: ")
        key = TOOLS.input_type("Enter the key: ")
        key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]
        encrypted_text = self.vernam_cipher(text, key_repeated)
        TOOLS.print_type(f"Encrypted text(ascii): {encrypted_text}","yellow")
        TOOLS.print_type(f"Encrypted text(hex): {encrypted_text.encode().hex()}", "magenta")

    def vernam_cipher(self, text, key):
        encrypted_text = ""
        for i in range(len(text)):
            encrypted_char = chr(ord(text[i]) ^ ord(key[i]))
            encrypted_text += encrypted_char
        return encrypted_text
#endregion vernam cipher

#region one time pad ciphers
    def _one_time_pad(self):
        text = TOOLS.input_type("Enter the text to encrypt: ")
        key = os.urandom(len(text))
        encrypted_bytes = bytearray()
        for char, key_byte in zip(text, key):
            encrypted_char = ord(char) ^ key_byte
            encrypted_bytes.append(encrypted_char)
        TOOLS.print_type(f"Random Key (hex): {key.hex()}", "blue")
        TOOLS.print_type(f"Encrypted text (hex): {encrypted_bytes.hex()}" "yellow")

    def one_time_pad(self, text, key):
        return bytes([ord(c) ^ k for c, k in zip(text, key)])
#endregion one time pad cipher

#region hill cipher
    def _hill_cipher(self):
        text = TOOLS.input_type("Enter the plaintext to encrypt: ")
        key_matrix_input = TOOLS.input_type("Enter the key matrix (3x3) as space-separated values (e.g., '1 2 3 4 5 6 7 8 9'): ")
        
        key_matrix = []
        try:
            key_matrix_values = list(map(int, key_matrix_input.split()))
            if len(key_matrix_values) != 9:
                raise ValueError("Key matrix must have 9 values for a 3x3 matrix.")
            key_matrix = [key_matrix_values[i:i+3] for i in range(0, 9, 3)]
        except ValueError as e:
            TOOLS.print_type(f"Invalid input for key matrix: {e}", "red", delay=0.001)
            return

        TOOLS.print_type("Using the following key matrix:", "cyan", delay=0.001)
        for row in key_matrix:
            TOOLS.print_type(" ".join(map(str, row)), "green", delay=0.001)

        TOOLS.print_type("Encrypting using Hill Cipher...", "cyan", delay=0.001)
        TOOLS.sleep(0.5)
        encrypted_text = self.hill_cipher(key_matrix, text)
        TOOLS.print_type(f"Encrypted text: {encrypted_text}", "yellow", delay=0.001)


    def hill_cipher(self,key_matrix, plaintext):
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        if len(key_matrix) != 3 or any(len(row) != 3 for row in key_matrix):
            raise ValueError("Key matrix must be 3x3.")

        filtered = [c for c in plaintext if c.isalpha()]
        while len(filtered) % 3 != 0:
            filtered.append('x')

        numbers = []
        for c in filtered:
            if c in small:
                numbers.append(small.index(c))
            elif c in big:
                numbers.append(big.index(c))
            else:
                numbers.append(0)

        ciphertext = ""
        for i in range(0, len(numbers), 3):
            block = numbers[i:i+3]
            result = []
            for col in range(3):
                value = 0
                for row in range(3):
                    value += key_matrix[row][col] * block[row]
                result.append(value % 26)
            for idx, num in enumerate(result):
                orig_char = filtered[i + idx]
                if orig_char in big:
                    ciphertext += big[num]
                else:
                    ciphertext += small[num]
        return ciphertext
#endregion hill cipher

#region rail fence cipher
    def _rail_fence_cipher(self):
        text = TOOLS.input_type("Enter the text to encrypt: ")
        if any(char.isdigit() for char in text):
            TOOLS.print_type("Error: Text should not contain numbers.", "red", delay=0.001)
            return

        rails = int(TOOLS.input_type("Enter the number of rails (2-10): "))
        if 2 <= rails <= 10:
            TOOLS.print_type("Encrypting using Rail Fence Cipher...", "cyan", delay=0.001)
            TOOLS.sleep(0.5)
            encrypted_text = self.rail_fence(text, rails)
            TOOLS.print_type(f"Encrypted text: {encrypted_text}", "yellow", delay=0.001)
        else:
            TOOLS.print_type("Invalid number of rails. Please enter a number between 2 and 10.", "red", delay=0.001)

    def rail_fence(self, text, rails):
        fence = [''] * rails
        rail = 0
        direction = 1

        for char in text:
            fence[rail] += char
            rail += direction

            if rail == 0 or rail == rails - 1:
                direction *= -1

        return ''.join(fence)
#endregion rail fence cipher

#region columnar cipher
    def _columnar_cipher(self):
        text = TOOLS.input_type("Enter the text to encrypt: ")
        TOOLS.print_type(f"Need {len(text)} cells for the given text.", "cyan", delay=0.001)
        
        rows = int(TOOLS.input_type("Enter the number of rows for the matrix: "))
        cols = int(TOOLS.input_type("Enter the number of columns for the matrix: "))
        
        key_input = TOOLS.input_type(f"Enter the key as {cols} numbers (1 to {cols}) separated by spaces (e.g., '3 1 2'): ")
        key = [int(k) for k in key_input.strip().split()]
        
        if len(key) != cols or sorted(key) != list(range(1, cols + 1)):
            TOOLS.print_type(f"Key must be {cols} unique numbers from 1 to {cols}.", "red", delay=0.001)
            return
        
        if rows <= 0 or cols <= 0:
            TOOLS.print_type("Rows and columns must be positive integers.", "red", delay=0.001)
            return

        TOOLS.print_type("Encrypting using Columnar Transposition Cipher...", "cyan", delay=0.001)
        TOOLS.sleep(0.5)
        encrypted_text = self.columnar_cipher(text, rows, cols, key)
        TOOLS.print_type(f"Encrypted text: {encrypted_text}", "yellow", delay=0.001)

    def columnar_cipher(self, text, rows, cols, key):
        padded_length = rows * cols
        padded_text = text.ljust(padded_length, 'x')[:padded_length]
        
        matrix = []
        idx = 0
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(padded_text[idx])
                idx += 1
            matrix.append(row)

        ciphertext = ""
        for k in key:
            col_idx = k - 1
            for r in range(rows):
                ciphertext += matrix[r][col_idx]
        return ciphertext

#endregion columnar cipher
