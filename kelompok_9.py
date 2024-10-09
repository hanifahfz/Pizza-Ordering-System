print("== Topping Pizza ==")
print("1. Tuna Meat")
print("2. Meat Lovers")
print("3. Cheese Lovers")
print("4. Chicken Lovers")
print("5. American Favorite")
totalPrice = 0

toppingPizza = input("Topping Pizza: ").lower()
if toppingPizza == "tuna meat":
    totalPrice += 35000
elif toppingPizza == "meat lovers":
    totalPrice += 40000
elif toppingPizza == "cheese lovers":
    totalPrice += 35000
elif toppingPizza == "chicken lovers":
    totalPrice += 40000
elif toppingPizza == "american favorite":
    totalPrice += 40000
else:
    print("Topping not found")

print("== Crust Pizza ==")
print("1. CheesyBites")
print("2. Pan")
print("3. Stuffed Crust")
print("4. Crown Crust")
print("5. Stuffed Crust Cheese")

crustPizza = input("Crust Pizza: ").lower()
if crustPizza == "cheesyBites":
    totalPrice += 55000
elif crustPizza == "pan":
    totalPrice += 40000
elif crustPizza == "stuffed crust":
    totalPrice += 50000
elif crustPizza == "crown crust":
    totalPrice += 50000
elif crustPizza == "stuffed crust cheese":
    totalPrice += 50000
else:
    print("Crust not found")

print("== Size Pizza ==")
print("1. Personal")
print("2. Medium")
print("3. Large")

size = input("Size Pizza: ").lower()
if size == "personal":
    totalPrice += 30000
elif size == "medium":
    totalPrice += 50000
elif size == "large":
    totalPrice += 70000
else:
    print("Size not found")
    
cheese = input("Do you want extra cheese (Yes/No)? ").lower()
if cheese == "yes":
    totalPrice += 13000

print(f"Thank you for choosing Pizza Hut Deliveries! Your final bill is: Rp. {totalPrice}")