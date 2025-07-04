import os

def input_set(prompt):
    s = input(prompt)
    return set(map(int, s.strip().split()))

def set_union(a, b):
    return a | b

def set_intersection(a, b):
    return a & b

def set_difference(a, b):
    return a - b

def set_symmetric_difference(a, b):
    return a ^ b

def main():
    os.system("cls")
    print("Set Theory Operations")
    print("Enter elements separated by spaces.")
    A = input_set("Enter Set A: ")
    B = input_set("Enter Set B: ")
    print(f"\nA = {A}")
    print(f"B = {B}")
    print(f"A ∪ B = {set_union(A, B)}")
    print(f"A ∩ B = {set_intersection(A, B)}")
    print(f"A - B = {set_difference(A, B)}")
    print(f"B - A = {set_difference(B, A)}")
    print(f"A Δ B = {set_symmetric_difference(A, B)}")

if __name__ == "__main__":
    main()
