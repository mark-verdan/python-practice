import random
import time

animals = ["Garuda", "Phoenix", "T-Rex", "Dog"]

def animal_gacha():
    animal_preference = random.choice(animals)
    print("Rolling...") 
    loading = time.sleep(3)
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
      attempt() 
        
      x = animal_gacha()
      if x == random_animal:
          print("You won!")
          break
      else:
          print("Try again..")
    else:
        print("Take your time!")  
        break