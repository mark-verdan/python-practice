price = { "water" : 10, "milk" : 15, "bread" : 20, "iphone": 51}


def buy_item(item, current_money):
    """Buys an item from the shop if the user has enough money."""
    if item not in price:
        print("Item is not available.") 
        return current_money
        
    cost = price[item] 
    if current_money >= cost:
        current_money -= cost
        print(f"You have successfully bought {item} for {cost}$! Money remaining: {current_money}$") 
        user_inventory.append(item)
        return current_money
    else:
        print("You don't have enough money.")
        return current_money

def continue_shopping():
    """Asks the user if they want to continue shopping."""
    while True:
        choice = input("Do you want to continue shopping? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thank you for shopping with us!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

#game starts here

user_money = 50
user_inventory = [] 


while True:
    print(f"You currently have {user_money}$.")
    print(f"Your shopping cart: {user_inventory}") 
    print("Welcome to the shop! We have the following items for sale:")
    for item, cost in price.items():
        print(f"{item}: {cost}$") 
    
    selection = input("What would you like to buy?: ").strip().lower()
    user_money = buy_item(selection, user_money)
        

    if not continue_shopping():
        break