# Mastermind Game
import random

class MasterMind():
    """
    Playing the Mastermind game
    
    """
    def __init__(self, level: int) -> None:
        """
        Constructor for setting up the difficulty level, number of digits and iterations of the game
        """
        self.level = level
        if level == 1:
            print("You are required to guess a four digit number!")
            self.digits = 4
            self.attempts = 5
        elif level == 2:
            print("You are required to guess a five digit number!")
            self.digits = 5
            self.attempts = 8
        elif level == 3:
            print("You are required to guess a six digit number!")
            self.digits = 6
            self.attempts = 11
        else:
            print("Invalid input! Please enter values in [1,2,3]")
            quit()


    def checker(self, guess: int, digits: int) -> None:
        """
        checks if the guess of Player 2 matches the length of the set value
        """

        if len(str(guess)) != digits:
            print("You havent entered desired number of digits, hence you are disqualified from the game")
            quit()

    @staticmethod
    def random_digit_generator(digits: int) -> int:
        """
        Generates a random multi digit number from the Player 1's side
        """
        try:
            lower_limit = int("1"+"0"*(digits-1))
            upper_limit = int("9"*(digits))
            randomly_generated_value = random.randrange(lower_limit, upper_limit)
            return randomly_generated_value
        except Exception as e:
            print(e)


    def player2_turn(self, digits: int, set_value: int, attempts: int) -> None:
        """
        Attempts of the Player 2
        """
        print("Enter a number")
        guess = int(input(": "))
        self.checker(guess, digits)

        if guess == set_value:
            print("You are a mastermind! Guessed the number in the very first attempt!")
            quit()

        else:
            ctr = 1
            while ctr != attempts:
                guess = str(guess)
                set_value = str(set_value)
                count = 0
                output = ["X"]*digits

                for i in range(digits):
                    if guess[i] == set_value[i]:
                        output[i] = guess[i]
                        count += 1

                if count != 0 and count < digits:
                    print(f"Not quite the number! You did get {count} digit(s) right")
                    print(output)
                    print("\nEnter your next choice of numbers:")
                    guess = int(input(": "))
                    self.checker(guess, digits)

                elif count == 0:
                    print("None of the numbers in your input match")
                    print("\nEnter your next choice of numbers:")
                    guess = int(input(": "))
                    self.checker(guess, digits)

                elif count == digits:
                    print("You've become a mastermind!")
                    print(f"You guessed the number in {ctr} attempts")
                    quit()
                ctr += 1
            print("Game Over!")
            print(f"The number was {set_value}")

        
if __name__ == "__main__":
    print("Player 1 is the computer!\nYou are the second player!")
    print("Rules of the game:\n1. The number of attempts that you will get to guess the multi-digit number will depend on the difficulty level of the game that you will opt for")
    print("2. If your guess doesnt consist of the desired number of digits then you will be disqualified from the game")
    print("\nGood luck! Hope you turn up to be the Mastermind of the game!!")
    difficulty_level = int(input("Enter the difficulty level of the game as 1/2/3 for Easy/Moderate/Hard respectively: "))
    game = MasterMind(difficulty_level)
    game.random_digit_generator(game.digits)
    game.player2_turn(game.digits, game.random_digit_generator(game.digits), game.attempts)

    

