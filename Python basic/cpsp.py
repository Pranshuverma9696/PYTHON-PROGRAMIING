costprize=int(input("Enter the cost prize:-"))
print("The cost prize is :-",costprize)

sellprize=int(input("Enter the sell prize:-"))
print("The sell prize is :-",sellprize)

if(costprize<sellprize):
    profit=int(costprize-sellprize)
    print("the profit is :-",profit)

elif(costprize>sellprize):
    loss=int(sellprize-costprize)
    print("the loss is :-",loss)
else:
    print("No profit No loss")    

