#  using forloop , while loops - Target Self Service ; practice purposes

first_purchase = None
another_purchase = []

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

    current_purchase = {"items": items, "prices": prices, "total_price": sum(prices)}

    if not first_purchase:  # If first_purchase is None, this is the first purchase
        first_purchase = current_purchase
    else:
        another_purchase.append(current_purchase)  # Append subsequent purchases to other_purchases list

print("Items in your cart: ")
print("") #For spacing

for item in items: #The loop iterate for each user's desire items
    print(item)

for price in prices: #The loop iterates over each price that user's desire items and add += is used.
    totalprice += price

print()
print(f"Your total is: ${totalprice}") #Disclosing total
print("Please bag your following items, and leave.") #Sending paying customer away

another_purchase = input("Would you like to make another purchase? (yes/no): ")
if another_purchase.lower() != "yes":
    print("Thank you for shopping with us!")
#Predomiately copy & pasting OG code to implement second purchase. B/C people tend to forget something and comeback
while True:
    item = input("Enter an item to buy (type 'done' when all items scanned): ")
    if item.lower() == "done": #regardless if user types DONE , it will still be accepted as it will converted to lower
        break
    else:
        price = float(input(f"Enter the price of a {item}: $"))
        items .append(item) #Append is a built in method that collects the item inputs
        prices.append(price) #Append is a built in method that collects the price inputted

    if not another_purchase:  # Check if it's the first purchase
        another_purchase = {"items": items, "prices": prices}

        for item in items:  # The loop iterate for each user's desire items
            print(item)

        for price in prices:  # The loop iterates over each price that user's desire items and add += is used.
            totalprice += price

UserQuestion = input("Would you like to see your purchase of your first & other purchase? 'enter yes or no' ")
if UserQuestion =="yes":
    print("Details of the first purchase:")
print("Items:", first_purchase["items"])
print("Prices:", first_purchase["prices"])
print("Total Price:", first_purchase["total_price"])
for idx, purchase in enumerate(another_purchase, start=1): # search all purchase item
    print("Items:", another_purchase["items"])
else:
    print("Have a great day")
