items = ["perfume", "noodle", "toothpaste", "yoghurt", "ice cream"]
priceLst = {}
for item in items:
    price = int(input(f"Enter the price of {item}: "))
priceLst.update({item:price})
# for item in items:
#     priceLst[item] = price #To add to a dict.
# print({priceLst})
for item in priceLst:
    print(f"Supermarket Pricelist\n{item}\t#{priceLst[item]}")
print("update the price of an item")
itemUpdated = int(input("new price for ice ceam is: "))