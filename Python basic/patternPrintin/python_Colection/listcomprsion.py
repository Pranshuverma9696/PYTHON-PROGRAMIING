fruits=["Apple","banana","Orange","Mango"]
new_fruit=[fruits for fruits in fruits if "a" in fruits ]
print(new_fruit)

new_copy=fruits.copy()
print(new_copy)
new_fru=new_fruit+fruits
print(new_fru)

#nested list 
#list=[10,20,30,[03,40,04],50]
fruits.insert(2,["Kiwi","Papaya"])
print(fruits)
print(fruits[2][0])