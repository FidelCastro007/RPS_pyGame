import random
import sys
from enum import Enum

def rps (name='PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    draw_count = 0

    def rps_game():
        nonlocal name
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerChoice = input(f"\n{name}, please enter...\n1 for Rock,\n2 for Paper or \n3 for Scissors: \n\n")

        if playerChoice not in ["1","2","3"]:
            print(f"{name}, please enter 1,2, or 3.")
            return rps_game()

        computerChoice = random.choice("123")

        player = int(playerChoice)

        computer = int(computerChoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace("RPS.","").title()}.")
        print(f"Computer chose {str(RPS(computer)).replace("RPS.","").title()}.\n")

        def gameplay(player,computer):
            nonlocal name,player_wins,computer_wins,draw_count
            if player == 1 and computer == 3 :
                player_wins += 1
                return f"🌟 {name}, you win"
            elif player == 2 and computer == 2:
                player_wins += 1
                return f"🌟 {name}, you win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🌟 {name}, you win"
            elif player == computer:
                draw_count += 1 
                return f"😫 Tie game, {name}!"
            else: computer_wins += 1 
            return  f"💻 computer wins!\nSorry, {name}..😥"
        
        game_result = gameplay(player,computer)
        print(game_result)

        nonlocal  game_count 
        game_count += 1

        print(f"\nGame_Count: {str(game_count)}")
        print(f"\n{name}'s wins: {str(player_wins)}")
        print(f"\nComputer wins: {str(computer_wins)}")
        print(f"\ndraw count: {str(draw_count)}")
        print(f"\nPlay again: {str(name)}?")

        while True:
            playAgain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

            if playAgain.lower() not in ["y","q"]:
                continue
            else: 
                break
        if playAgain.lower() == "y":
            rps_game()
        else:
              print("\n🙌😁💕🙌")
              print("Thank you for playing!\n")
              if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋") # this main file exit immediately otherwise return this file or func
              else:
                return

    return rps_game

if __name__ == "__main__":  
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalised game experience."
    ) 

    parser.add_argument("-n", "--name", metavar="name", required=True,help= "The name of the person playing the game."
    )

    args = parser.parse_args()

rps_game= rps(args.name)
rps_game()
