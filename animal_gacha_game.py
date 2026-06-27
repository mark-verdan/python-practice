import random
import time

animals = ["Garuda", "Phoenix", "T-Rex", "Dog", "Cat"]

def animal_gacha():
    animal_preference = random.choice(animals)
    print("Rolling...") 
    time.sleep(3)   #loading
    print("You got:", animal_preference) 
    return animal_preference
    
attempt_count = 0    
    
def attempt():
    global attempt_count
    attempt_count = attempt_count + 1 
    print("Attempt:", attempt_count)
    
random_animal = random.choice(animals)
    
print("Today's challenge:", "Get", random_animal)

while True:
    user_input = input("Do you wish to start? (yes/no): ").lower().strip() 
    if user_input == "yes":
      counter = attempt() 
        
      x = animal_gacha()
      if x == random_animal:
          print("You won!")
          print("Attempt taken:", attempt_count)
          break
      else:
          print("Try again..")
    else:
        print("Take your time!")  
        break