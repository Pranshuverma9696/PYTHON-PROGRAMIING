# recursion in python :- recursion is the process pf defining something in terms of itself.

def factorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return(n*factorial(n-1))
  
n=int(input("Enter the number:-"))  
print(factorial(n))  