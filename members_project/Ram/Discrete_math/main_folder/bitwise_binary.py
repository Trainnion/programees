

def BITWISE(x,y, operation):
    x_str = x 
    y_str = y
    x = "0b" + x
    y = "0b" + y
    equation = x + operation + y  
    
    result = eval(equation) 
    
   
    max_len = len(x_str)
    y_str_aligned = y_str.rjust(max_len)
    binary_result_str = bin(result)[2:].rjust(max_len)
    
    
    print(operation)
    print(x_str)
    print(y_str_aligned)
    print("_" * len(x))
    print(binary_result_str)
    print("\n")
    
    

def BITWISE_OPERATIONS(x,y):  
    operations = ["|", "&" , "^" ]
    for operation in operations:
        BITWISE(x,y,operation)
        
    
    
    
    


print("BitWise Operations")
x = input("Input first binary: ")
y = input("Input second binary: ")

BITWISE_OPERATIONS(x,y)

