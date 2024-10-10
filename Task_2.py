import random

def guess_number(name="PlayerOne"):
    def play_guess_number(name):
        while True:
            playerchoice = input(
                "\n"+ name +", guess which number I'm thinking of... 1, 2, or 3.\n\n")

            if playerchoice not in ["1", "2", "3"]:
                print(name +", please enter 1, 2, or 3.")
                continue

            computerchoice = random.choice("123")

            print(f"\n{name}, you chose {playerchoice}.")
            print(
                "I was thinking about the number "+ computerchoice +".\n"
            )

            player = int(playerchoice)

            computer = int(computerchoice)

            def decide_winner(player, computer):
                if player == computer:
                    return "🎉"+ name+ ", you win!"
                else:
                    return "Sorry "+ name +". Better luck next time. 😢"

            game_result = decide_winner(player, computer)

            print(game_result)
            
            playAgain = input("\nDo you want to play again?(Y to play again, any other key to quit): ").strip().lower()
            if playAgain != 'y':
               print("\n🎉🎉🎉🎉")
               print("Thank you for playing!\n")
               break
          
    play_guess_number(name)

   
        
guess_number("GGM")

""" import random
import threading

def guess_number(name="PlayerOne"):
    def play_guess_number(name):
        range_start = 1
        range_end = 3
        player_wins = 0
        time_limit = 5  # Set the time limit for each guess in seconds

        def input_with_timeout(prompt, timeout):
            # Wrapper function to handle input with a timeout
            def timed_input():
                nonlocal playerchoice
                playerchoice = input(prompt)
            
            playerchoice = None
            thread = threading.Thread(target=timed_input)
            thread.start()
            thread.join(timeout)
            
            if thread.is_alive():
                print(f"\nTime's up! You took too long to guess.")
                return None
            return playerchoice

        while True:
            print(f"\n{name}, guess which number I'm thinking of between {range_start} and {range_end}.")
            playerchoice = input_with_timeout(f"\nEnter a number between {range_start} and {range_end} (within {time_limit} seconds):\n\n", time_limit)

            if playerchoice is None:  # Player failed to input within the time limit
                print(f"Sorry {name}, you ran out of time! 😢")
                playAgain = input("\nDo you want to play again? (Y to play again, any other key to quit): ").strip().lower()
                if playAgain != 'y':
                    print("\n🎉🎉🎉🎉")
                    print("Thank you for playing!\n")
                    break
                else:
                    continue

            if not playerchoice.isdigit() or not (range_start <= int(playerchoice) <= range_end):
                print(f"{name}, please enter a valid number between {range_start} and {range_end}.")
                continue

            playerchoice = int(playerchoice)
            computerchoice = random.randint(range_start, range_end)

            print(f"\n{name}, you chose {playerchoice}.")
            print(f"I was thinking about the number {computerchoice}.\n")

            def decide_winner(player, computer):
                if player == computer:
                    return True, f"🎉 {name}, you win!"
                else:
                    return False, f"Sorry {name}. Better luck next time. 😢"

            is_winner, game_result = decide_winner(playerchoice, computerchoice)
            print(game_result)

            if is_winner:
                player_wins += 1
                range_end += 2
                print(f"\n{name}, your range has increased to {range_start} to {range_end}!")
            
            playAgain = input("\nDo you want to play again? (Y to play again, any other key to quit): ").strip().lower()
            if playAgain != 'y':
                print("\n🎉🎉🎉🎉")
                print("Thank you for playing!\n")
                break

    play_guess_number(name)

# Example of how to use the function
guess_number("GGM")
 """