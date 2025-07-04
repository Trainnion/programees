print("Propositional Logic")
print("What type of Operation?")
x = input("[1] ∨ [2] ∧ [3] → [4] ↔  : ")
    
    
    
match x:
    case "1":
        first_Input = input("First Input: ")
        second_Input = input("Second Input: ")
        if first_Input == "1" or second_Input == "1":
            output = "1 or True"
        else:
            output = "0 or False"
            
        print(first_Input, " ∨ ",second_Input,": ", output)
        
    case "2":
        first_Input = input("First Input: ")
        second_Input = input("Second Input: ")
        if first_Input == "1" and second_Input == "1":
            output = "1 or True"
        else:
            output = "0 or False"
            
        print(first_Input, " ∧ ",second_Input,": ", output)
        
    case "3":
        first_Input = input("First Input: ")
        second_Input = input("Second Input: ")
        if first_Input == "1" and second_Input == "0":
            output = "0 or False"
        else:
            output = "1 or True"
            
        print(first_Input, " → ",second_Input,": ", output)
        
    case "4":
        first_Input = input("First Input: ")
        second_Input = input("Second Input: ")
        if first_Input == "1" and second_Input == "1" :
            output = "1 or True"
            
        elif first_Input == "0" and second_Input == "0":
            output = "1 or True"
            
        else:
            output = "0 or False"
            
        print(first_Input, " ↔ ",second_Input,": ", output)
        
        