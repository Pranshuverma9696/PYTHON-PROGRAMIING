# #list are ordered collection of data items.
# #they store multiple items in a single variable.
# #list are immutable

# number=[1,2,3,4,"Apple","Mango"]

# # print(number[5])
# # print(number[3])

# #negative indexing
# # print(number[-3])
# # print(number[len(number)-3])

# # if(7) in number:
# #   print("Yes")
# # else:
# #   print("No")  
#   # same thing are applied on string

# # for i in number:
# #   print(i,end=" ")  

# print(number)
# print(number[1:])

#list method

l=[1,4,2,5,9]
# print(l)
# # append function are used for insert the element in the list in the last.
# l.append(35)
# print(l)

# # sort() function are used for sort the list
# l.sort()
# print(l)

# # if we want to sort in decending order
# l.sort(reverse=True)
# print(l)

# reverse() reverse the order of the list.

# l.reverse()
# print(l)


#index() this method return the index of the first occurence of the list item.
# print(l.index(1))

# #count function return the count of the number of item with the given value
# print(l.count(1))

# m=l.copy()
# m[0]=0
# print(l)
# print(m)

# #inset this method insert an item at the given index user has to spacify index and 

# l.insert(1,23)
# print(l)

# this mehtod adds an entire list or ohter collection datatypes to the existing list


l=[1,5,2,67]
m=[90,59,34]

l.extend(m)
print(l)

