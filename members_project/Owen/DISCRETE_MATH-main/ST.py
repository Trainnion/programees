#ST.py
#a class made for set theory
from TOOLS import TOOLS

class ST:
    """a class made for set theory"""
    
    def __init__(self):
        TOOLS.clear_screen()
        TOOLS.simulate_sleep(1, "opening set theory function")
        print("set theory function opened!")
        TOOLS.sleep(1)
        self.start()

    def start(self):
        print("Welcome to the Set Theory class!")
        print("This class provides various set operations.")
        print("You can perform union, intersection, difference, subset checks, and equality checks on sets.")
        
        self.perform_operations()

    def perform_operations(self):
        print("Let's begin by reading two sets from the user.")
        TOOLS.sleep(1)
        A = self.read_set('A')
        B = self.read_set('B')
        print("\nYou have entered:")
        print(f"Set A: {A}")
        print(f"Set B: {B}")

        TOOLS.simulate_sleep(1, "performing set operations")
        TOOLS.sleep(1)

        union_result = self.union(A, B)
        intersection_result = self.intersection(A, B)
        difference_result = self.difference(A, B)
        is_subset_result = self.is_subset(A, B)
        is_equal_result = self.is_equal(A, B)

        print("\nResults of set operations:")
        print(f"Union (A ∪ B): {union_result}")
        print(f"Intersection (A ∩ B): {intersection_result}")
        print(f"Difference (A - B): {difference_result}")
        print(f"Is A a subset of B? {'Yes' if is_subset_result else 'No'}")
        print(f"Are A and B equal? {'Yes' if is_equal_result else 'No'}")

    def read_set(self, name):
        elements = input(f"Enter the elements of set {name} (comma separated): ")
        return set(map(str.strip, elements.split(',')))
    
    @staticmethod
    def union(set1, set2):
        return set(set1).union(set2)

    @staticmethod
    def intersection(set1, set2):
        return set(set1).intersection(set2)

    @staticmethod
    def difference(set1, set2):
        return set(set1).difference(set2)

    @staticmethod
    def is_subset(subset, superset):
        return set(subset).issubset(superset)

    @staticmethod
    def is_equal(set1, set2):
        return set(set1) == set(set2)