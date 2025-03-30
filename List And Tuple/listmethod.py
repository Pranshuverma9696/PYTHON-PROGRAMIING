student=[12,3,4,5]
student.append(3)
# print(student)
# # append attached value in the last of list

# # list .sort method sorts in acending order
# student.sort()
# print(student)

# list .sort (reverse =True sort in descending order)
student.sort(reverse=True)
print(student)

student.reverse()
print(student)

# inerst method insert the value in index wise

student.insert(3,90)
print(student)
# remove method  first occurrence of element
student.remove(3)
print(student)

# pop method is revmove element element index wise

student.pop(0)
print(student)