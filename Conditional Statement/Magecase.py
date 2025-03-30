#match case
num=int(input("Enter the number:-"))
match num:
  case 0:
    print("num is zero")
  case 2 if num%2==0:
    print("Num  is even")
  case _:
    print("Num is odd")  
