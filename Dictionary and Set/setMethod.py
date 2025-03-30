s={1,2,5,6,8}
s2={3,6,7}

# union method
# print(s.union(s2))

(s.update(s2))
print(s,s2)
print(s)

# intersection
# print(s.intersection(s2))

s={1,2,5,6,8}
s2={3,6,7}

print(s.symmetric_difference(s2))
print(s.difference(s2))

# set method are used to manipulation on the set

s={1,2,5,6,8}
s2={3,6,7}
print(s.isdisjoint(s2))
# if  comman element are present then it return false and return True

s={1,2,5,6,8,3,9}
s2={3,9}
print(s.isdisjoint(s2))
# issuperset() method

print(s.issuperset(s2))
print(s2.issubset(s))

s={1,2,5,6,8,3,9}

s.remove(2)
# s.remove(10)# show error
s.discard(30)# don't error 
print(s)

#pop method remove the remdom value
print(s.pop())


# del method delete the all set
# s={1,2,5,6,8,3,9}
# del s
# print(s)

# clear method remove the item from the set and print empty set

s={1,2,5,6,8,3,9}
s.clear()
print(s)

s={1,2,5,6,8,3,9}
if 5 in s:
  print("The number is present")

else:
  print("the number is not present")  
