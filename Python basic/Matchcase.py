num=int(input("Enter the number:-"))
num2=int(input("Enter the second number:-"))
operator=input("Enter the operater (-,*,+,*):-")

match operator:
    case "+":
        print("Sum is:-",num+num2)
    case "-":
        print("Divsion is:-",num-num2)
    case "*":
        print("Multification is :-",num*num2)
    case "/":
        print("Division is:-",num/num2) 


        # ternary operator
        #vale=value1 if cont else value2              
    