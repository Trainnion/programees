from itertools import product
import os
print()

def evaluate(expr):
    variables = {"p": 0, "q": 0, "r": 0, "s": 0 }
    result = eval(expr, variables)
    
    
    expr_variables = ""
    
    #checker on how many var present in expression
    for i in range(len(expr)):
        for key in variables:
            if(expr[i] == key and (i == 0 or expr[i - 1] == " ")):
                expr_variables += expr[i]
            
    #Truth table printer  
    header = " | ".join(expr_variables) + " | Result"
    print(header)
    print("-" * len(header))  
        
    for values in product([0,1], repeat = len(expr_variables)):
        env = dict(zip(expr_variables, values))
        result = eval(expr, {}, env)
        row = " | ".join(str(env[var]) for var in expr_variables) + f" |   {int(result)}"
        print(row)
        
print("Truth tables")
print("Use: p, q, r & s")
print("Use: and, or, xor, biconditional")
expression = input()

evaluate(expression)

#could be improved