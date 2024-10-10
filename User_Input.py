import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1 # full caps in variable like that val doesn't changed Like const in Js but small letters or mixed vals may be changed 
    PAPER = 2
    SCISSOR = 3

""" playAgain = True

while playAgain:

    # print(RPS(2))
    print(RPS.ROCK)
    print(RPS["ROCK"]) #[] accessing element
    print(RPS.ROCK.value) #

    try:
        print("")
        playerchoice = input(
            "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        #print(playerchoice)
        print(type(playerchoice))#

        player = int(playerchoice)

        if player < 1 or player > 3:
            print("You must enter 1,2, or 3.")
            continue
    except ValueError:
        print("INvalid input.Please enter a number between 1 and 3.")
        continue

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("")

    print("You chose " + str(RPS(player)).replace("RPS.",'') + ".") # () call func or constructor
    print("computer chose " + str(RPS(computer)).replace("RPS.",'') + ".")
    print("")

    if player == 1 and computer == 3:
        print("🌟 You win")
    elif player == 2 and computer == 1:
        print("🌟 You Win")
    elif player == 3 and computer == 2:
        print("🌟 You Win")
    elif player == computer:
        print("😫 Tie game!")
    else: print("💻 computer wins")

    playAgain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playAgain.lower() == "y":
        continue
    else:
        print("\n🙌😁💕🙌")
        print("Thank you for playing!\n")
        playAgain = False
sys.exit("Bye! 😅")
 """

# game_count = 0 // global val
def rps():
    game_count = 0 
    computer_wins = 0
    player_wins = 0
    Draw_Count = 0

    def rps_game():
        print("")
        playerchoice = input(
            "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
        
        if playerchoice not in ["1","2","3"]:
            print("You must enter 1,2, or 3.")
            return rps_game()

        # print(playerchoice)
        # print(type(playerchoice))#

        player = int(playerchoice)

            # if player < 1 or player > 3:
            #     print("You must enter 1,2, or 3.")
            # sys.exit("You must enter 1,2, or 3.")
    #  except ValueError:
    #         print("INvalid input.Please enter a number between 1 and 3.")
    #         continue

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print("")

        print(f"You chose {str(RPS(player)).replace("RPS.",'').title()}.") # () call func or constructor
        print(f"Computer chose {str(RPS(computer)).replace("RPS.",'').title()}.\n")

        def gameplay(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal Draw_Count
            if player == 1 and computer == 3:
                player_wins += 1
                return "🌟 You win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🌟 You Win"
            elif player == 3 and computer == 2:
                player_wins +=1 
                return "🌟 You Win"
            elif player == computer:
                Draw_Count += 1
                return "😫 Tie game!"
            else: computer_wins += 1 
            return "💻 computer wins"
        
        game_result = gameplay(player,computer)
        print(game_result)

        #global game_count
        nonlocal game_count
        game_count += 1

        print(f"\nGame_Count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nComputer wins: {str(computer_wins)}")
        print(f"\nCalculating Draw: {str(Draw_Count)}")


        while True:
            playAgain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

            if playAgain.lower() not in ["y","q"]:
                continue
            else:
                break
        if playAgain.lower() == "y":
            return rps_game()
        else:
            print("\n🙌😁💕🙌")
            print("Thank you for playing!\n")
            sys.exit("Bye! 😅")

    return rps_game()

if __name__ == "__main__":
    rps() # Modules in calling in other files while this func activates only by its name from other files, otherwise it shows filename of the func

#print(__name__) # prints __main__ (Special Value)