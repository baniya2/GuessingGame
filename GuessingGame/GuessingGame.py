import random

def display_heading():
    """Sandeep Baniya | CIS 261 | Guessing Game"""
    print("\n-------------------------------------")
    print(" Welcome to the Number Guessing Game!")
    print("---------------------------------------\n")
    
def play_game(limit):
    """Handles the core game logic, including input validation and clear messages."""
    random_number = random.randint(1,limit)
    print(f"I'm thinking of a number between 1 and {limit}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        if guess < 1 or guess > limit:
            print(f"Please guess a number withing the range 1 to {limit}.")
            continue
        if guess == random_number:
            print("Congratulations! You guessed it correctly!")
            break
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again")
            
def main():
    """Controls the overall game flow, including error handling and user experience."""
    while True:
        try:
            display_heading()
            limit = int(input("Enter the upper limit for the guessing range: "))
            play_game(limit)
        except ValueError:
            print("Invalid input. Please enter an integer for the limit.")
            continue
            
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() != 'y':
            break
    print("\nThanks for playing! Goodbye.")
   
if __name__ == "__main__":
    main()
   
