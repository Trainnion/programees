from itertools import product

class TruthTable:
    def __init__(self, variables):
        self.variables = variables

    def evaluate(self, expr):
        # Prepare variable combinations
        combos = list(product([False, True], repeat=len(self.variables)))
        results = []
        for values in combos:
            env = dict(zip(self.variables, values))
            # Replace variable names and operators for eval
            eval_expr = expr
            for var in self.variables:
                eval_expr = eval_expr.replace(var, f'env["{var}"]')
            eval_expr = eval_expr.replace('~', 'not ')
            eval_expr = eval_expr.replace('^', ' and ')
            eval_expr = eval_expr.replace('or', ' or ')
            # Evaluate the expression
            result = eval(eval_expr)
            results.append((values, result))
        return results

    def print_table(self, expr):
        results = self.evaluate(expr)
        header = ' | '.join(self.variables) + ' | Result'
        print(header)
        print('-' * len(header))
        for values, result in results:
            row = ' | '.join(['T' if v else 'F' for v in values]) + f' |   {"T" if result else "F"}'
            print(row)

# # Example use case
# if __name__ == "__main__":
#     variables = ['p', 'q', 'r']
#     expr = "(~p^q)or(q^r)"
#     tt = TruthTable(variables)
#     tt.print_table(expr)

