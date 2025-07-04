import os

def tree_factorization(n):
    """
    Returns a nested list representing the factorization tree of n.
    Each node is [factor, subtree], where subtree is a list of further factorizations.
    """
    def factorize(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return [i, factorize(x // i)]
        return [x, []]
    return factorize(n)

def print_tree(tree, level=0):
    factor, subtree = tree
    print("  " * level + str(factor))
    for child in subtree:
        print_tree(child, level + 1)

def main():
    os.system("cls")
    print("Tree Factorization")
    n = int(input("Enter a positive integer: "))
    tree = tree_factorization(n)
    print(f"\nFactorization tree for {n}:")
    print_tree(tree)

if __name__ == "__main__":
    main()
