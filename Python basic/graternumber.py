number1=int(input("Enter the first number:-"))
number2=int(input("Enter the second number:-"))
number3=int(input("Enter the third number:-"))
# if number1>number2 and number1>number3:
#     print("Number first in grater",number1)
# elif number2>number1 and number2>number3:
#     print("Number second is grater",number2)

# else:
#     print("Number third is grater")        

#using nested if else
if(number1>number2):
    if(number1>number3):
        print("Number 1st is grater")
    else:
         print("Number 3st is the graterest")   
    if(number2>number3):
        print("Number 3st is greater element")
    else:
        print("Number 3st is grater")          