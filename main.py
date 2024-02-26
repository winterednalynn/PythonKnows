#  using forloop , while loops - Target Self Service ; practice purposes

items = []
prices = []
totalprice = 0 #start as if nothing is in the cart , starting point : 0

while True:
    item = input("Enter an item to buy (type 'done' when all items scanned): ")
    if item.lower() == "done": #regardless if user types DONE , it will still be accepted as it will converted to lower
        break
    else:
        price = float(input(f"Enter the price of a {item}: $"))
        items .append(item) #Append is a built in method that collects the item inputs
        prices.append(price) #Append is a built in method that collects the price inputted

print("Items in your cart: ")
print("") #For spacing

for item in items: #The loop iterate for each user's desire items
    print(item)

for price in prices: #The loop iterates over each price that user's desire items and add += is used.
    totalprice += price

print()
print(f"Your total is: ${totalprice}") #Disclosing total
print("Please bag your following items, and leave.") #Sending paying customer away