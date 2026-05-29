def celsius_to_fahrenheit(C):
    '''This function converts Celsius to Fahrenheit'''
    fahrenheit = (C * 9/5) + 32
    return fahrenheit
    
def fahrenheit_to_celsius(F):
    '''This function converts Fahrenheit to Celsius'''
    celsius = (F - 32) * 5/9
    return celsius 

print("Welcome User!")  
    
while True:
    
    print("Please choose:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nOr 'X' to exit the program")
    option = input().strip().upper() 
    
    if option == "1":
        try:
          temp1 = int(input("Please enter your Celsius temperature(without the units °C): "))
          celsius_to_fahrenheit(temp1)
          print(f"{temp1} °C is {celsius_to_fahrenheit(temp1)} °F")
        except ValueError:
            print("Invalid Input!")
    elif option == "2":
        try:
            temp2 = int(input("Please enter your Fahrenheit temperature(without the units °F): "))
            fahrenheit_to_celsius(temp2)
            print(f"{temp2} °F is {fahrenheit_to_celsius(temp2)} °C")
        except ValueError:
            print("Invalid Input!")
    elif option == "X":
        print("Later!")
        break
    else:
        print("Invalid Input!")


#Old school project