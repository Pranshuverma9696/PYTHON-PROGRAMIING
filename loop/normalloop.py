
# while i<=9:
#   print(i)
#   if(i==5):
#     break
#   i+=1
#  i=1

 
i = 1  

while i <= 10:
    if i % 2 == 0:
        i += 1    # Increment i before continue to avoid infinite loop
        continue
    print(i)
    i += 1
