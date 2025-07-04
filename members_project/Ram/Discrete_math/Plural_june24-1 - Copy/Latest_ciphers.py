import os
import base64

def Caesar_cipher():
    print()
    print("Example: Plain text = 'HELLO', Key = 3")
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
            
    print()
    print("Original text: ", plain_text)
    print("Cipher Text: ", caesar_cipher_text)

def Rail_fence():
    print()
    print("Example: Plain text = 'HELLO WORLD', Key = 3")
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
    

def Vigenere_cipher():
    print()
    print("Example: Plain text = 'HELLO', Key = 'KEY'")
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

    print()
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def Playfair_cipher():
    print()
    print("Example: Plain text = 'HELLO', Key = 'KEYWORD'")
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

    print()
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
    
def Vernam_cipher():
    print()
    print("Example: Plain text = 'HELLO', Key = 'XMCKL'")
    plain_text = input("Input Plain text: ")
    key = input("Input key (same length as plain text): ")

    if len(plain_text) != len(key):
        print("Error: Key must be the same length as the plain text.")
        return

    # Encrypt: XOR each byte, then encode as base64 for printable output
    cipher_bytes = bytes([(ord(plain_text[i]) ^ ord(key[i])) for i in range(len(plain_text))])
    cipher_b64 = base64.b64encode(cipher_bytes).decode()

    print()
    print("Original text:", plain_text)
    print("Cipher Text (base64):", cipher_b64)

    # Optional: Demonstrate decryption from base64
    decoded_bytes = base64.b64decode(cipher_b64)
    decrypted_bytes = bytes([(decoded_bytes[i] ^ ord(key[i])) for i in range(len(decoded_bytes))])
    try:
        decrypted_text = decrypted_bytes.decode()
    except UnicodeDecodeError:
        decrypted_text = decrypted_bytes.decode(errors='replace')
    print("Decrypted:", decrypted_text)
    
def One_Time_Pad_cipher():
    print()
    print("Example: Plain text = 'HELLO', Key = 'XMCKL'")
    plain_text = input("Input Plain text: ")
    key = input("Input key (same length as plain text): ")

    if len(plain_text) != len(key):
        print("Error: Key must be the same length as the plain text.")
        return

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_char = chr((ord(plain_text[i]) + ord(key[i])) % 256)
        cipher_text += cipher_char

    print()
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def Hill_cipher():
    print()
    print("Example: Plain text = 'HELP', Key = '3 3 2 5' (for 2x2 matrix)")
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
    print()
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def Columnar_cipher():
    print()
    print("Example: Plain text = 'HELLO WORLD', Key = 'ZEBRAS'")
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

    print()
    print("Original text:", plain_text)
    print("Cipher Text:", cipher_text)
    
def AES_cipher():
    print()
    print("AES Cipher (Pure Python ECB Demo)")
    print("Example: Plain text = 'abcdefghijklmnop', Key = 'abcdefghijklmnop'")
    plain_text = input("Input Plain text (16 chars): ")
    key = input("Input key (16 chars): ")
    if len(plain_text) != 16 or len(key) != 16:
        print("Plain text and key must be exactly 16 characters.")
        return
    cipher = aes_encrypt_block(plain_text.encode('utf-8'), key.encode('utf-8'))
    print("Encrypted (hex):", cipher.hex())

# AES S-box
s_box = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
]

def xor_bytes(a, b):
    return [i ^ j for i, j in zip(a, b)]

def sub_bytes(state):
    return [s_box[byte] for byte in state]

def shift_rows(state):
    return [
        state[0], state[5], state[10], state[15],
        state[4], state[9], state[14], state[3],
        state[8], state[13], state[2], state[7],
        state[12], state[1], state[6], state[11],
    ]

def mix_columns(state):
    def mix_column(col):
        t = col[0] ^ col[1] ^ col[2] ^ col[3]
        return [
            col[0] ^ t,
            col[1] ^ t,
            col[2] ^ t,
            col[3] ^ t
        ]
    return sum([mix_column(state[i:i+4]) for i in range(0, 16, 4)], [])

def add_round_key(state, round_key):
    return xor_bytes(state, round_key)

def key_expansion(key):
    return [list(key)] * 11

def aes_encrypt_block(plaintext, key):
    assert len(plaintext) == 16
    assert len(key) == 16
    state = list(plaintext)
    round_keys = key_expansion(key)
    state = add_round_key(state, round_keys[0])
    for rnd in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[rnd])
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])
    return bytes(state)
    

def permute(bits, pattern):
    return [bits[i - 1] for i in pattern]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox_lookup(bits, sbox):
    row = (bits[0] << 1) | bits[3]
    col = (bits[1] << 1) | bits[2]
    val = sbox[row][col]
    return [val >> 1 & 1, val & 1]

def key_generation(key):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8  = [6, 3, 7, 4, 8, 5, 10, 9]
    key = permute(key, P10)
    left, right = key[:5], key[5:]
    left, right = left_shift(left, 1), left_shift(right, 1)
    K1 = permute(left + right, P8)
    left, right = left_shift(left, 2), left_shift(right, 2)
    K2 = permute(left + right, P8)
    return K1, K2

def fk(bits, key):
    EP  = [4, 1, 2, 3, 2, 3, 4, 1]
    P4  = [2, 4, 3, 1]
    S0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]
    S1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]
    left, right = bits[:4], bits[4:]
    temp = permute(right, EP)
    temp = xor(temp, key)
    s0 = sbox_lookup(temp[:4], S0)
    s1 = sbox_lookup(temp[4:], S1)
    temp = permute(s0 + s1, P4)
    return xor(left, temp) + right

def sdes_encrypt(plaintext, key):
    IP  = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
    K1, K2 = key_generation(key)
    bits = permute(plaintext, IP)
    bits = fk(bits, K1)
    bits = bits[4:] + bits[:4]  # Switch
    bits = fk(bits, K2)
    return permute(bits, IP_INV)

def sdes_decrypt(ciphertext, key):
    IP  = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
    K1, K2 = key_generation(key)
    bits = permute(ciphertext, IP)
    bits = fk(bits, K2)
    bits = bits[4:] + bits[:4]  # Switch
    bits = fk(bits, K1)
    return permute(bits, IP_INV)
    
def SDES_cipher():
    print()
    print("SDES Cipher (Simplified DES, 8-bit blocks, 10-bit key)")
    print("Example: Key = 1010000010, Plaintext = 10101011")
    key_str = input("Enter 10-bit key (e.g. 1010000010): ")
    if len(key_str) != 10 or any(c not in '01' for c in key_str):
        print("Key must be 10 bits (0/1 only)")
        return
    key = [int(b) for b in key_str]
    plain_str = input("Enter 8-bit plaintext (e.g. 10101011): ")
    if len(plain_str) != 8 or any(c not in '01' for c in plain_str):
        print("Plaintext must be 8 bits (0/1 only)")
        return
    plaintext = [int(b) for b in plain_str]
    cipher_bits = sdes_encrypt(plaintext, key)
    cipher_str = ''.join(str(b) for b in cipher_bits)
    print("Encrypted (ciphertext):", cipher_str)
    decrypted_bits = sdes_decrypt(cipher_bits, key)
    decrypted_str = ''.join(str(b) for b in decrypted_bits)
    print("Decrypted (plaintext):", decrypted_str)
    
def RSA_encryption():
    print()
    print("RSA Encryption/Decryption")
    print("Example: p = 11, q = 13, message = 7")
    from math import gcd
    import random

    # Helper: Compute modular inverse using Extended Euclidean Algorithm
    def mod_inverse(e, phi):
        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y
        g, x, _ = egcd(e, phi)
        if g != 1:
            raise Exception("Modular inverse doesn't exist")
        return x % phi

    # Helper: Check if a number is prime (basic)
    def is_prime(num):
        if num <= 1: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: return False
        return True

    # Prompt user for primes
    while True:
        try:
            p = int(input("Enter a prime number p: "))
            q = int(input("Enter a different prime number q: "))
        except ValueError:
            print("Please enter valid integers.")
            continue
        if not (is_prime(p) and is_prime(q)):
            print("Both numbers must be prime.")
            continue
        if p == q:
            print("p and q must be different.")
            continue
        break

    n = p * q
    phi = (p - 1) * (q - 1)
    # Find e randomly
    possible_e = [i for i in range(2, phi) if gcd(i, phi) == 1]
    if not possible_e:
        print("No valid e found. Try different primes.")
        return
    e = random.choice(possible_e)
    d = mod_inverse(e, phi)
    public = (e, n)
    private = (d, n)
    print("Public Key:", public)
    print("Private Key:", private)
    print(f"(e was chosen randomly: {e})")
    try:
        message = int(input("Input a number to encrypt (as message): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    cipher = pow(message, e, n)
    decrypted = pow(cipher, d, n)
    print("Original Message:", message)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypted)






# Bitwise operations helpers
def permute(block, table):
    return [block[i - 1] for i in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def shift_left(bits, n):
    return bits[n:] + bits[:n]

# S-boxes (only 1 for simplicity here; real DES uses 8)
S_BOX = [
    [
        [14,4,13,1],
        [2,15,11,8],
        [3,10,6,12],
        [5,9,0,7]
    ],
]

# Expansion table (simplified)
EXPANSION_TABLE = [1, 2, 3, 4, 1, 2]  # Mock version

# Key schedule rotation amounts
SHIFT_SCHEDULE = [1] * 16  # Normally alternates 1s and 2s

# Initial Permutation (simplified)
IP = [2, 6, 3, 1, 4, 8, 5, 7]

# Final Permutation (simplified inverse of IP)
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

# Permutation function (mock)
P_BOX = [2, 4, 3, 1]

# Convert byte to bit list
def byte_to_bits(byte):
    return [int(bit) for bit in format(byte, '08b')]

# Convert bit list to byte
def bits_to_byte(bits):
    return int(''.join(str(b) for b in bits), 2)

# Round function F
def f(right, subkey):
    expanded = permute(right, EXPANSION_TABLE)
    xored = xor(expanded, subkey)
    row = (xored[0] << 1) | xored[-1]
    col = int(''.join(str(x) for x in xored[1:-1]), 2)
    sbox_value = S_BOX[0][row % 4][col % 4]
    sbox_bits = [int(b) for b in format(sbox_value, '04b')]
    return permute(sbox_bits, P_BOX)

# Key schedule
def generate_keys(key_bits):
    left, right = key_bits[:len(key_bits)//2], key_bits[len(key_bits)//2:]
    keys = []
    for shift in SHIFT_SCHEDULE:
        left = shift_left(left, shift)
        right = shift_left(right, shift)
        combined = left + right
        keys.append(combined[:6])  # Just first 6 bits as subkey (mock)
    return keys

# Encrypt 1 block
def des_encrypt_block(block_bits, key_bits):
    block = permute(block_bits, IP)
    left, right = block[:len(block)//2], block[len(block)//2:]
    keys = generate_keys(key_bits)
    for i in range(16):
        temp = right
        right = xor(left, f(right, keys[i]))
        left = temp
    pre_output = right + left
    return permute(pre_output, IP_INV)

# Text to bits
def text_to_bits(text):
    return [int(bit) for char in text for bit in format(ord(char), '08b')]

def bits_to_text(bits):
    return ''.join(chr(bits_to_byte(bits[i:i+8])) for i in range(0, len(bits), 8))

# Main encrypt function
def encrypt(plaintext, key):
    # Custom DES-like block encryption (no external imports)
    def pad(text):
        while len(text) % 8 != 0:
            text += ' '
        return text
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
    key_bits = text_to_bits(key[:8])  # Only 8 chars
    cipher_bits = []
    for block in blocks:
        bits = text_to_bits(block)
        encrypted_bits = des_encrypt_block(bits, key_bits)
        cipher_bits.extend(encrypted_bits)
    return cipher_bits

# Decryption: same as encryption but reverse keys
def decrypt(cipher_bits, key):
    blocks = [cipher_bits[i:i+64] for i in range(0, len(cipher_bits), 64)]
    key_bits = text_to_bits(key[:8])
    keys = generate_keys(key_bits)[::-1]
    plaintext = ""
    for block in blocks:
        block = permute(block, IP)
        left, right = block[:len(block)//2], block[len(block)//2:]
        for i in range(16):
            temp = right
            right = xor(left, f(right, keys[i]))
            left = temp
        pre_output = right + left
        decrypted_bits = permute(pre_output, IP_INV)
        plaintext += bits_to_text(decrypted_bits)
    return plaintext.rstrip()




def DES_cipher():
    print()
    print("DES Cipher (Custom Bitwise Implementation)")
    print("Example: Key = 'abcdefgh', Plain text = 'testtext'")
    key = input("Input key (8 characters): ")
    if len(key) != 8:
        print("Key must be exactly 8 characters (64 bits) for DES.")
        return
    plain_text = input("Input Plain text: ")
    # Encrypt and decrypt each character individually
    encrypted_chars = []
    decrypted_chars = []
    for char in plain_text:
        cipher_bits = encrypt(char, key)
        encrypted_chars.append(cipher_bits)
        decrypted = decrypt(cipher_bits, key)
        decrypted_chars.append(decrypted)
        print(f"Char: '{char}' -> Encrypted bits: {cipher_bits} -> Decrypted: '{decrypted}'")
    print("\nAll encrypted bits:", encrypted_chars)
    print("All decrypted chars:", ''.join(decrypted_chars))
    
    


ciphers = [ "Caesar Cipher",
            "Vigenère Cipher",
            "Playfair Cipher",
            "Vernam Cipher",
            "One Time Pad Cipher",
            "Hill Cipher",
            "Rail Fence Cipher",
            "Columnar Cipher",
            "AES Cipher",
            "DES Cipher",
            "SDES Cipher",
            "RSA Encryption"]
running = True
while(running):
    print()
    print("Ciphers")
    i = 1
    for cipher in ciphers:
        print(f"{i}.", cipher)
        i = i + 1 
        
    cipher = input("Choose Cipher: " )
    match cipher:
        case "1":
            Caesar_cipher()
        case "2":
            Vigenere_cipher()
        case "3":
            Playfair_cipher()
        case "4":
            Vernam_cipher()
        case "5":
            One_Time_Pad_cipher()
        case "6":
            Hill_cipher()
        case "7":
            Rail_fence()
        case "8":
            Columnar_cipher()
        case "9":
            AES_cipher()
        case "10":
            DES_cipher()
        case "11":
            SDES_cipher()
        case "12":
            RSA_encryption()

    restart = input("\nStart again? [y/n]: ")
    if restart == "n" or restart == "N":
        running = False


