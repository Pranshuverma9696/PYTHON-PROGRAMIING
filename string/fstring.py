# string formattin in python :- string formatting can be done in python using the format method.
pra="Hey my name is {1} and I am from {0}"
name="pranshu"
country="India"

print(pra.format(country,name))

print(f"Hey my name is {name} and I am from {country}")

text="for only {price:.3f} dollars"
print(text.format(price=45.352))

print(type(f"{30*20}"))
