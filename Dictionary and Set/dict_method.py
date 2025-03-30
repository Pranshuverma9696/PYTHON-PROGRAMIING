student={
"name":"Pranshu",
"Age":29,
"Class":"BCA",
"University":"BBD"

}
# print(student)
# print(student.keys())

# print(student.values())

# print(student.items())
#print(student["name2"]) return error
print(student.get("name2"))  #return none

student.update({"City":"Delhi"})
print(student)


