import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    number = input("Please guess a number between 1 and {} : ".format(range))
    count = 1
    number = -1
    while int(number) != random_number:
            print("Sorry, you didn't get it right")
            if number > random_number:
                print("You guessed too high")
            if number < random_number:
                print("You guessed too low")
 
            number = input("Please guess a number between 1 and{}: ".format(range))
            number = int(number)
            count = count + 1
            print("Good Job")
            print("You guessed in {} tries" .format(count))
            play_again = input("Would you like to play again? (yes or no)?")
            play_again = play_again.lower()
            if play_again == "yes":
                quit = False
            if play_again == "no": 
                quit = True
print("thanks for playing")

   
    
    
