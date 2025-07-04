import math
import os

# Prime factorization of a number
def prime_factors(n):
    factors = []
    # Divide by 2 until odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

# Sieve of Eratosthenes: returns all primes <= n
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Fermat's Little Theorem: a^p ≡ a (mod p) for prime p
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

# Find primitive roots modulo n
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
        if math.gcd(g, n) == 1 and is_primitive_root(g, n, phi, factors):
            roots.append(g)
    return roots

def trial_division(n):
    """
    Returns a list of all divisors of n (excluding 1 and n itself).
    """
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# Menu-driven interface
if __name__ == "__main__":
    running = True
    while running:
        print()
        print("Number Theory Functions")
        print("1. Prime Factors")
        print("2. Sieve of Eratosthenes")
        print("3. Fermat's Little Theorem")
        print("4. Primitive Roots")
        print("5. Trial Division (find all divisors)")
        choice = input("Choose function: ")
        if choice == "1":
            n = int(input("Enter number to factor: "))
            print("Prime factors:", prime_factors(n))
        elif choice == "2":
            n = int(input("Find all primes up to: "))
            print("Primes:", sieve_of_eratosthenes(n))
        elif choice == "3":
            a = int(input("Enter a: "))
            p = int(input("Enter p (prime): "))
            result = fermats_little_theorem(a, p)
            print(f"Fermat's Little Theorem holds: {result}")
        elif choice == "4":
            n = int(input("Find primitive roots modulo: "))
            print("Primitive roots:", primitive_roots(n))
        elif choice == "5":
            n = int(input("Enter number to find divisors: "))
            print("Divisors (excluding 1 and n):", trial_division(n))
        else:
            print("Invalid choice.")
        restart = input("\nStart again? [y/n]: ")
        if restart.lower() == "n":
            running = False
