# # a="Pranshu" # sting are immutable
# # print(a)
# # print(a.upper())
# # string method are no change in orignal string its can make new string and return new string 

# # rstrip function strip to end ! mark not in start

# # A="!!!Hello Python !!!!!!!!!!"
# # print(A)
# # print(A.rstrip("!"))

# A="Hello PythOn"
# # replace 
# print(A.replace("Python","Pransh"))

# #split function convert string to list

# print(A.split(" "))
# # captalize() convert the first string letter in to captial and convert the all character in to lower case

# a="pythOn"
# print(a.capitalize())

# #center method  align the string to the center as per parameter given by the user
# print(a)
# print(a.center(50))

# # count function returns the number of thimes the given value has occurred withi the given string
# s="Pranshu,Rohit,Pranshu, ram, shyam"
# print(s.count("Pranshu"))

# # ends with function return methon checks it the string ends with a given value. If yes then return true else return false.

# print(s.endswith("m"))
# print(s.endswith("Pran" ,0,4))

# # find() searches for the first occurence of the given value and the return the index where it is present. If given value is absent fron the string the return -1

# str="Hello Python"
# print(str.find("y"))
# print(str.find("m"))

# # index()  searches for the first occurrence of the given value and return the index where it is presen. If given value is absent from the string then eaise an exception

# # print(str.index("y"))
# # print(str.index("m"))

# #isalnum()  returns true only if the entire string only consists of  A-Z,a-z,0-9.if anly other character or punctuations are present then  it return false

# str2="Hello python"
# print(str2.isalnum())

# # isalpha() returns  true only if the entire string only consists of A-Z and a-z if other character or punctuations or number 0-9 are the it return false

# str2="Hellopython"
# print(str2.isalpha())

# # islower() all character are lower or not if lower returns ture otherwise return false

# str2="hello" 
# print(str2.islower())

# # isprintable returns true if all the values within the given string are printable if not then return false

# str2="hello\n"
# print(str2.isprintable())

# # isspace () returns true only  if the string contain white spaces else returns false

str2="   "
print(str2.isspace())

# istitle() returns true only if the first letter of each word of the string is capitinalize it returns false

str2="Hello Python"
print(str2.istitle())

# swapcase() changes the character casing of the string upper case converted to lower case and lower case convert to uppercase

str="Hii who are"
print(str.swapcase())