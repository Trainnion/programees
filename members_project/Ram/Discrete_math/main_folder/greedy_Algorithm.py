print()

def greedy_knapsack():
    print("Greedy Algorithm: Fractional Knapsack Problem")
    n = int(input("Enter number of items: "))
    weights = []
    values = []
    for i in range(n):
        w = float(input(f"Enter weight of item {i+1}: "))
        v = float(input(f"Enter value of item {i+1}: "))
        weights.append(w)
        values.append(v)
    capacity = float(input("Enter knapsack capacity: "))
    # Calculate value/weight ratio and sort items with their original indices
    items = sorted([(values[i]/weights[i], weights[i], values[i], i+1) for i in range(n)], reverse=True)
    total_value = 0
    placed_items = []
    print("\nItems sorted by value/weight ratio (highest first):")
    for ratio, w, v, idx in items:
        print(f"Item {idx}: Value: {v}, Weight: {w}, Ratio: {ratio:.2f}")
    print()
    for ratio, w, v, idx in items:
        if capacity >= w:
            print(f"Taking full item {idx} (value: {v}, weight: {w})")
            capacity -= w
            total_value += v
            placed_items.append((idx, w, v, 1.0))
        else:
            if capacity > 0:
                print(f"Taking {capacity}/{w} fraction of item {idx} (value: {v}, weight: {w})")
                total_value += v * (capacity / w)
                placed_items.append((idx, capacity, v * (capacity / w), capacity / w))
                capacity = 0
            break
    print("\nItems placed in the knapsack:")
    for idx, w, v, frac in placed_items:
        if frac == 1.0:
            print(f"Item {idx}: Full (weight: {w}, value: {v})")
        else:
            print(f"Item {idx}: Fraction {frac:.2f} (weight: {w}, value: {v:.2f})")
    print(f"\nTotal value in knapsack: {total_value:.2f}")

def greedy_egyptian_fraction():
    print("Greedy Algorithm: Egyptian Fraction Representation")
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    if numerator == 0 or denominator == 0:
        print("Numerator and denominator must be non-zero.")
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

def diffie_hellman_demo():
    print("Diffie-Hellman Key Exchange Demo (Educational)")
    # Publicly agreed prime and base
    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root modulo p (g): "))
    print("\n-- Alice and Bob choose private keys --")
    a = int(input("Alice's private key (a, secret): "))
    b = int(input("Bob's private key (b, secret): "))
    # Compute public keys
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"\nAlice computes public key: A = g^a mod p = {g}^{a} mod {p} = {A}")
    print(f"Bob computes public key: B = g^b mod p = {g}^{b} mod {p} = {B}")
    print("\n-- Exchange public keys --")
    print(f"Alice sends A = {A} to Bob")
    print(f"Bob sends B = {B} to Alice")
    # Compute shared secret
    alice_secret = pow(B, a, p)
    bob_secret = pow(A, b, p)
    print(f"\nAlice computes shared secret: s = B^a mod p = {B}^{a} mod {p} = {alice_secret}")
    print(f"Bob computes shared secret: s = A^b mod p = {A}^{b} mod {p} = {bob_secret}")
    if alice_secret == bob_secret:
        print(f"\nShared secret established! s = {alice_secret}")
    else:
        print("\nError: Shared secrets do not match!")

def job_sequencing():
    print()
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

def activity_selection():
    print()
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

while True:
    print()
    print("Greedy Algorithms")
    print("1. Fractional Knapsack Problem")
    print("2. Egyptian Fraction Representation")
    print("3. Diffie-Hellman Key Exchange Demo")
    print("4. Job Sequencing with Deadlines")
    print("5. Activity Selection Problem")
    print("0. Exit")
    choice = input("Choose an algorithm: ")
    if choice == "1":
        greedy_knapsack()
    elif choice == "2":
        greedy_egyptian_fraction()
    elif choice == "3":
        diffie_hellman_demo()
    elif choice == "4":
        job_sequencing()
    elif choice == "5":
        activity_selection()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
    input("\nPress Enter to continue...")


