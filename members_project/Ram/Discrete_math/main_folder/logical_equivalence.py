import os

def logical_equivalence():
    print()
    print("Logical Equivalence Checker")
    print("Enter two logical expressions using variables (e.g., p, q, r) and operators (~ for NOT, & for AND, | for OR, -> for IMPLIES, <-> for IFF):")
    expr1 = input("Enter first expression: ")
    expr2 = input("Enter second expression: ")
    # Supported variables
    variables = sorted(set([c for c in expr1 + expr2 if c.isalpha()]))
    if not variables:
        print("No variables found in expressions.")
        return
    print(f"Variables detected: {', '.join(variables)}")
    # Generate all possible truth assignments
    from itertools import product
    def eval_expr(expr, vals):
        # Replace variables with their truth values
        for var, val in zip(variables, vals):
            expr = expr.replace(var, str(val))
        # Replace logical operators with Python equivalents
        expr = expr.replace("~", " not ")
        expr = expr.replace("&", " and ")
        expr = expr.replace("|", " or ")
        expr = expr.replace("->", " <= ")  # a -> b is (not a) or b, but for table, use implication
        expr = expr.replace("<->", " == ")
        # Evaluate
        try:
            return eval(expr)
        except Exception as e:
            print(f"Error evaluating: {expr}\n{e}")
            return None
    equivalent = True
    print("\nTruth Table:")
    print(" | ".join(variables) + " | Expr1 | Expr2")
    for vals in product([False, True], repeat=len(variables)):
        res1 = eval_expr(expr1, vals)
        res2 = eval_expr(expr2, vals)
        print(" | ".join(str(int(v)) for v in vals) + f" |   {int(res1)}   |   {int(res2)}")
        if res1 != res2:
            equivalent = False
    if equivalent:
        print("\nThe expressions are logically equivalent.")
    else:
        print("\nThe expressions are NOT logically equivalent.")

if __name__ == "__main__":
    logical_equivalence()
