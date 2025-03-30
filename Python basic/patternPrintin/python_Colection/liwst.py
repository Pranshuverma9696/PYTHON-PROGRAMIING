fruits=["apple","mango","banana","orange"]

# fruits[1]=["kiewi"]
# fruits[1:3]=["banana"]
# print(fruits)

# sorting a list
 
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits) 

fruits.reverse()
print(fruits)

#list comprehension
list=[fruits for fruits if "a" in fruits]