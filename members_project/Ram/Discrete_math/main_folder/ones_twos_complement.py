import os

def ones_complement(n, bits=8):
    mask = (1 << bits) - 1
    return (~n) & mask

def twos_complement(n, bits=8):
    mask = (1 << bits) - 1
    return ((~n) + 1) & mask

def main():
    print()
    os.system("cls" if os.name == "nt" else "clear")
    print("1's and 2's Complement Calculator")
    num = int(input("Enter an integer: "))
    bits = int(input("Enter number of bits (default 8): ") or 8)
    print(f"\nBinary ({bits} bits): {format(num if num >= 0 else (1 << bits) + num, f'0{bits}b')}")
    one_c = ones_complement(num, bits)
    two_c = twos_complement(num, bits)
    print(f"1's complement: {format(one_c, f'0{bits}b')} (decimal: {one_c})")
    print(f"2's complement: {format(two_c, f'0{bits}b')} (decimal: {two_c})")

if __name__ == "__main__":
    main()
