price = { "water" : 10, "milk" : 15, "bread" : 20 }

user_money = 50

shop_items = ["water", "milk", "bread"]

def buy_item(item):
    """Buys an item from the shop if the user has enough money."""
    if item in shop_items:
        global user_money
        if user_money >= price[item]:
            user_money -= price[item]
            print(f"You bought {item} for {price[item]} dollars. You have {user_money} dollars left.")
        else:
            print("You don't have enough money to buy that item.")
    else:
        print("That item is not available in the shop.")

def continue_shopping():
    """Asks the user if they want to continue shopping."""
    while True:
        choice = input("Do you want to continue shopping? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thank you for shopping with us!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

while True:
    print("Welcome to the shop! We have the following items for sale:")
    print(shop_items)
    buy_item(input("What would you like to buy?:  ").lower())

    if continue_shopping():
        continue
    else:
        break