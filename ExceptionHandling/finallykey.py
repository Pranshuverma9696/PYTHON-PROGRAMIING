#the finally code block is also a part of exception handling . When we handle exception usint try and except  block we can include a finally block at the end. The finally blick is aluways exceuted, so ti a geberall used fo a doing the concluding tasks like closind file resoures or closing datavase connection or may be ending the program exceution with a delightul message.

def fun():
  try:
   l=[1,2,3,4]
   i=int(input("Enter the index:"))
   print(l[i])
   return 1
  except:
   print("some error")
   return 0
  
  finally:
   print("I am always exceuted")    

x=fun()
print(x)   