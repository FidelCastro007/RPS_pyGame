def checkWeather():
    print('**********')
    while True:
        weather = input("\nEnter the weather  :").strip().lower()

        if weather not in ["sunny", "rainy"]:
            print("\nPlease enter sunny or rainy \n\nCan you provide the correct weather")
            continue

        while True:
            umbrella_input = input("\nDo you have an umbrella (yes/no)? \n").strip().lower()
            if umbrella_input not in ["yes", "no"]:
                print("\nPlease enter yes or no")
                continue

            break

        have_umbrella = umbrella_input == "yes"
      
        if weather == "rainy":
            if have_umbrella:
                return "\nGo outside"
            else:
                return "\nStay inside"
        elif weather == "sunny":
            if have_umbrella:
                return "\nTake the umberlla just in case"
            else:
                return "\nEnjoy the sunshine"

        #print("\ncheck the weather again")


print(checkWeather())

