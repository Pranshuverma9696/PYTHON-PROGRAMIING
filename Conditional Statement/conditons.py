# if state ment
# a=int(input("Enter your age:-"))
# print("Your age is :-", a)
# if(a>18):
#   print("You can drive ")
# else:
#   print("You cannot drive")  

# example of elif statement
# num=int(input("Enter the number:-"))
# if(num>0):
#   print("Number is positive")
# elif(num==0):
#   print("Number is zero")
# else:
#   print("Number is negative")  

# nested elif example
num=int(input("Enter the number:-"))
if num<0:
  print("Number is negative")

elif(num>0):
  if(num<=10):
    print("Number is between 1-10")
  elif(num>10 and num<=20):
    print("The number is between   11 to 20")  
  else:
    print("Number is grater than 20") 
else:
  print("Number is zero")       