
while True:
    print("\n==============================")
    print("        TREASURE HUNT")
    print("==============================")

    name = input("\nEnter your name: ")

    health = 100
    gold = 0
    sword = False
    potion = 0

    print("\nWelcome", name, "!")
    print("You are a young adventurer.")
    print("One day, you find an old map in your house.")
    print("The map shows a hidden treasure in a forest.")
    print("You decide to go on an adventure.")

    input("\nPress ENTER to continue...")

    print("\nYou finally reach the forest.")
    print("There are two paths in front of you.")
    print("1. Go left")
    print("2. Go right")

    choice = input("Choose your path: ")

    if choice == "1":
        print("\nYou walk through a dark forest.")
        print("After some time, you find an old sword.")
        print("You pick up the sword.")
        sword = True

        print("\nSuddenly, a wild wolf appears!")
        print("1. Fight the wolf")
        print("2. Run away")

        choice = input("Your choice: ")

        if choice == "1":
            print("\nYou fight the wolf with your sword.")
            print("You defeat the wolf!")
            print("You lose 20 health.")
            health = health - 20
            gold = gold + 100
            print("You found 100 gold coins.")

        elif choice == "2":
            print("\nYou run away from the wolf.")
            print("You escape safely.")

        else:
            print("\nWrong choice!")

    elif choice == "2":
        print("\nYou find a small village.")
        print("An old merchant welcomes you.")

        print("\nThe merchant has two items.")
        print("1. Buy a sword (50 gold)")
        print("2. Buy a health potion (30 gold)")
        print("3. Leave the shop")

        choice = input("Your choice: ")

        if choice == "1":
            print("\nThe merchant gives you a sword.")
            sword = True

        elif choice == "2":
            print("\nYou bought a health potion.")
            potion = potion + 1

        elif choice == "3": 
            print("\nYou leave the village.")

        else:
            print("\nWrong choice!")

    else:
        print("\nYou got lost in the forest.")
        health = 0

    if health > 0:
        input("\nPress ENTER to continue...")

        print("\nAfter walking for hours,")
        print("you find a small abandoned house.")
        print("There is a box inside the house.")

        print("\n1. Open the box")
        print("2. Ignore the box")

        choice = input("Your choice: ")

        if choice == "1":
            print("\nYou open the box.")
            print("You find a health potion!")
            potion = potion + 1

        elif choice == "2":
            print("\nYou decide to leave the box.")

        else:
            print("\nWrong choice!")

    if health > 0:
        print("\nYou reach an old castle.")
        print("A huge dragon is sleeping near the entrance.")
        print("You need to get past it.")

        print("\nYour health:", health)
        print("Your gold:", gold)
        print("Your sword:", sword)
        print("Your potions:", potion)

        print("\n1. Fight the dragon")
        print("2. Sneak past the dragon")
        print("3. Use a health potion")

        choice = input("Your choice: ")

        if choice == "1":
            if sword == True:
                print("\nYou take out your sword.")
                print("The dragon wakes up and attacks!")
                print("You fight bravely and defeat it.")
                health = health - 40
                gold = gold + 500
                print("You found 500 gold coins!")

            else:
                print("\nYou have no sword!")
                print("The dragon attacks you.")
                health = 0

        elif choice == "2":
            print("\nYou slowly walk past the dragon.")
            print("Luckily, it does not wake up!")
            print("You reach the treasure room.")

        elif choice == "3":
            if potion > 0:
                print("\nYou drink a health potion.")
                health = health + 30
                potion = potion - 1
                print("Your health is now:", health)
            else:
                print("\nYou don't have any potions.")

        else:
            print("\nWrong choice!")

    if health > 0:
        input("\nPress ENTER to continue...")

        print("\nYou enter the treasure room.")
        print("There are three treasure chests.")
        print("One of them contains the real treasure!")

        print("\n1. Open the first chest")
        print("2. Open the second chest")
        print("3. Open the third chest")

        choice = input("Your choice: ")

        if choice == "2":
            print("\nCONGRATULATIONS!")
            print("You found the legendary treasure!")
            gold = gold + 2000
            print("You received 2000 gold coins!")

        else:
            print("\nOh no! The chest was empty.")
            print("You still survived the adventure.")

    print("\n==============================")
    print("         GAME RESULTS")
    print("==============================")

    print("Player:", name)
    print("Health:", health)
    print("Gold:", gold)
    print("Sword:", sword)
    print("Potions:", potion)

    if health <= 0:
        print("\nGAME OVER!")
        print("You couldn't complete your adventure.")
    else:
        print("\nCongratulations!")
        print("You completed your adventure!")

    print("\nThanks for playing", name, "!")

    restart = input("\nDo you want to play again? (y/n): ")

    if restart.lower() != "y":
        print("\nGoodbye!")
        break
