from functools import reduce

def chinese_remainder_theorem(remainders, moduli):
    """
    Solves the system of congruences using the Chinese Remainder Theorem:
        x ≡ remainders[i] mod moduli[i]
    Returns the smallest non-negative solution x.

    Parameters:
    - remainders: list of a_i
    - moduli: list of m_i (must be pairwise coprime)
    """
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

    def mod_inverse(a, m):
        g, x, _ = extended_gcd(a, m)
        if g != 1:
            raise ValueError(f"No modular inverse for {a} mod {m}")
        return x % m

    M = reduce(lambda a, b: a * b, moduli)
    x = 0

    for a_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        y_i = mod_inverse(M_i, m_i)
        x += a_i * M_i * y_i

    return x % M

if __name__ == "__main__":
    print("Chinese Remainder Theorem Solver")
    print("Example: For the system x ≡ 2 mod 3, x ≡ 3 mod 4, x ≡ 1 mod 5:")
    print("  Enter number of congruences: 3")
    print("  Enter modulus m[1]: 3")
    print("  Enter remainder a[1]: 2")
    print("  Enter modulus m[2]: 4")
    print("  Enter remainder a[2]: 3")
    print("  Enter modulus m[3]: 5")
    print("  Enter remainder a[3]: 1\n")
    k = int(input("Enter number of congruences: "))
    remainders = []
    moduli = []
    for i in range(k):
        m = int(input(f"Enter modulus m[{i+1}]: "))
        a = int(input(f"Enter remainder a[{i+1}]: "))
        moduli.append(m)
        remainders.append(a)
    print("\nSystem of congruences:")
    for i in range(k):
        print(f"x ≡ {remainders[i]} mod {moduli[i]}")
    try:
        solution = chinese_remainder_theorem(remainders, moduli)
        M = reduce(lambda a, b: a * b, moduli)
        print(f"\nSolution x ≡ {solution} mod {M}")
    except ValueError as e:
        print(f"\nError: {e}")
