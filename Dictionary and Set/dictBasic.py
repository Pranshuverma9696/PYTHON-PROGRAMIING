# dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key value pairs that are seprated by commas and enclised within curly brackets{}

d={
  "Name": "Pranshu verma",
  "Age": 23,
  "Village":"Pareli"

}

# print(d)
# print(d["Name"])# if value is not present in the dictionary than it return error

# print(d.get("Name"))# get mehtod if value is not present in dictionary than it return none vaule

# # print(d["Age 2"])
# print(d.get("Age 2"))

# print(d.keys()) # return all key
# print(d.values())# return all value

print(d.items())