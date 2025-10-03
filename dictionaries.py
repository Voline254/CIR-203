# 1. Dictionary of 5 products
inventory = {"Laptop": 15, "Phone": 8, "Headphones": 20, "Charger": 5, "Mouse": 12}
print("Inventory:", inventory)

# 2. Add new product & update existing
inventory["Keyboard"] = 10
inventory["Phone"] = 12
print("\nUpdated Inventory:", inventory)

# 3. Function: stock < 10
def low_stock(inv):
    return {k: v for k, v in inv.items() if v < 10}

print("\nProducts with stock < 10:", low_stock(inventory))

# 4. Delete discontinued product
del inventory["Charger"]
print("\nAfter removing 'Charger':", inventory)

# 5. Loop with .items()
print("\nFinal Inventory:")
for product, qty in inventory.items():
    print(f"{product}: {qty}")