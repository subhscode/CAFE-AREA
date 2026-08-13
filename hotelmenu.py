menu = {
    "pizza": 120,
    "burger": 100,
    "fries": 50,
    "coffee":30,
    "pasta":60,
}

print("Welcome to our hotel menu!")
print("pizza: 120/-\nburger: 100/-\nfries: 50/-\ncoffee: 30/-\npasta: 60/-")

order_total=0

item_1=input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: {order_total}/-")
else:
    print(f"Sorry, {item_1} is not available yet.")
    another_item = input("Do you want to order another item? (yes/no): ")
    if another_item == "yes":
        item_2 = input("Enter the second item you want to order: ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"{item_2} added to your order. Current total: {order_total}/-")
        else:
            print(f"Sorry, {item_2} is not available yet.")
print(f"The total amount of your order to pay: {order_total}/-")
            
    