
# exception handling is the process of responding tp unwanted or unexpected events when a computer runs. Exception handling deals with theese events to aviod the program or system srashin and without this process, exception would disrupt the operation of a program

# a=input("Enter  a number:")
# print( f"Multiplication table of {a} is :")


# try:
#  for i in range(1,11):
#    print(f"{int(a)}*{i}={(int(a)*i)}")
# except:
#   print("Please enter the valid input")

# print("Program has been ended")   

try:

 num=int(input("Enter the number:"))
 a=[4,3]
 print(a[num])

except ValueError:
 print("Number entered is not an integer")

except IndexError:
 print("Index error") 

