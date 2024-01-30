def addition(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2
    

def div(n1, n2):
    return n1 / n2


while(True):

    number = int(input("enter 1 for addition ,enter 2 for subtraction, enter 3 for multiplication ,enter 4 for division, enter 5 to end the program : "))
    if number==5:
        break


    a=int(input("enter first number: "))
    b=int(input("enter secoind number: "))
    
        

    if number== 1:
        
        
        print(addition(a,b))

    elif number== 2:
        
        print(sub(a,b))
        
    elif number==3:
        
        print(mul(a,b))

    elif number ==4:
        
        print(div(a,b))
    
    else:
        print("enter number between 1 to 4")




    

    





