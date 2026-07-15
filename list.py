inventory = {
    "Belt": 10,
    "Cap": 5
}

inventory.update({"Belt": 8})

inventory.update({"Cap": 25})

item= input("enter item name: ")

quantity= int(input("enter quantity: "))

inventory.update({item: quantity})

search = input("enter item to search: ")

print(inventory.get("Belt"))

print(inventory.get(search))

print(inventory)

total = sum(inventory.values())
print("Total quantity:", total)
