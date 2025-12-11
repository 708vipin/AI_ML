#Create a function calculator(a,b, operation) that performs addition, subtraction, multiplication or division based on the operation paramter.
# Operator can have values (+, -, /, *)

def calculator(a,b, operator):
    if operator == "+" :
        return (a+b)
    elif operator == "-" :
        return(a-b)
    elif operator == "*" :
        return (a*b)
    elif operator == "/" :
        return (a/b)
    else:
        print("Please enter one of the operator, +, -, *, /")                 
    
    