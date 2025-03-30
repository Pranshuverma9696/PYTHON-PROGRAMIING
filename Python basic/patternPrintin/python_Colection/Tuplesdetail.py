# tuples used to store multiple items in a variable
# fruits=(w,e,r,t,t,y)
#priperties of tuples
# ordered 
# immutable
# Dublicates alloed 
# any datatype 
# mix of different data types

#major difference tuple and list list is mutable and tuples are not mutabe

color=("Red","Pink","Yellow")
print(type(color))
print(len(color))


#another way to make a tupe
#fruit=("Apples",)
# fruites=tuple(("Apples"))

# accessing item in tuples

# print(color[1])

# - indexing
print(color[-1])
print(color[1:])
print(color[-1:])


#if want if an item exits in tuple]
if "Yellow" in color:
    print("Yes present")

# #taverse tuple
# for i in color:
#     print(i)

    # # concadinate 2 tuples
    # more_color=("Blue","Brown")
    # co=more_color+color
    # print(co)
# unpacking of tuples

color1,color2,color3=color
print(color1,color2,color3) 

#Why we need tuple
# iteratin through a tuple  is faster than a list
# list are mutable where as tuples are inmmutable
# tuples that contain immutable elements can be used as a 
# key for a dictionary