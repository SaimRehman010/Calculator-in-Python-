def add(n1 , n2 ):
    return n1+n2

def subtract(n1 , n2):
    return n1-n2

def multiplication(n1 , n2):
    return n1*n2

def division(n1 , n2):
    return n1/n2

operations = {"+" : add ,
             "-" : subtract ,
             "*" : multiplication ,
             "/" : division
            }

def calculator():
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick the symbol! ")
        num2 = float(input("What is the second number?: "))
        calculation_function = operations[operation_symbol]
        anwser = calculation_function(num1 , num2)

        print(f"{num1} {operation_symbol} {num2} = {anwser}")

        complete = input("Type 'y' to continue calculating with the {anwser} , or type 'n' to start again.: ")

        if complete == "y" :
            num1 = anwser
        elif complete == "n" :
            should_continue = False 
            calculator()

calculator()            
