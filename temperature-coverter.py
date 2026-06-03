def celsius_to_fahrenheit(C):
    """This function converts Celsius to Fahrenheit""" 
    fahrenheit = (C * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(F):
    """This function converts Fahrenheit to Celsius""" 
    celsius = (F - 32) * 5/9
    return celsius
    
def continue_or_not():
    """This function ask if the user wants to stop this program""" 
    while True:
        continue_block = input("Do you wish to continue? (yes/no): ").strip().lower()
        if continue_block == "yes":
            return True
        elif continue_block == "no":
            return False
        else:
            print("Invalid input! Please use yes or no!")
            continue

print("Welcome User!")  

while True:

    print("Please choose:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nOr 'X' to exit the program")
    option = input().strip().upper() 

    if option == "1":
        try:
            celsius_temperature = int(input("Please enter your Celsius temperature(without the units °C): "))
            celsius_to_fahrenheit(celsius_temperature) 
            print(f"{celsius_temperature} °C is {celsius_to_fahrenheit(celsius_temperature)} °F")
            if not continue_or_not():
                break
        except ValueError:
            print("Invalid Input!")
    elif option == "2":
        try:
            fahrenheit_temperature = int(input("Please enter your Fahrenheit temperature(without the units °F): "))
            fahrenheit_to_celsius(fahrenheit_temperature)
            print(f"{fahrenheit_temperature} °F is {fahrenheit_to_celsius(fahrenheit_temperature)} °C")
            if not continue_or_not():
                break
        except ValueError:
            print("Invalid Input!")
    elif option == "X":
        print("Later!")
        break
    else:
        print("Invalid Input! Please enter 1,2 or X to continue!")