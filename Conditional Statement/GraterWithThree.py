num1=int(input("Enter the first number:-"))
num2=int(input("Enter the second number:-"))
num3=int(input("Enter the third number:-"))

if(num1>num2 and num1>num3):
    print("The number fist is grater")
elif(num2>num1 and num2>num3):
    print("the number second is grater")   
elif(num1==num2==num3):
    print("Both are equal")
else:
    print("The number third is grater")     