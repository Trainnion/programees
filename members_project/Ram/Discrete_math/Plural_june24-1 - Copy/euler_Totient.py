
from math import gcd

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
    for k in range(1, original_n + 1):
        if gcd(k, original_n) == 1:
            coprimes.append(k)
    return result, coprimes

def main():
    print()
    print("Euler's Totient Function Calculator")
    n = int(input("Enter a positive integer: "))
    phi, coprimes = euler_totient(n)
    print(f"\nEuler's Totient Function φ({n}) = {phi}")
    print(f"Numbers coprime to {n}: {coprimes}")
    print(f"Total coprime numbers: {len(coprimes)}")

if __name__ == "__main__":
    main()
